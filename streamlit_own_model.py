from tensorflow.keras.applications.vgg16 import VGG16, preprocess_input
import streamlit as st
import tensorflow as tf
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications import VGG16
import numpy as np
import os
from PIL import Image
import nbformat
from nbconvert import HTMLExporter

# Load the TensorFlow model
model = tf.keras.models.load_model("celebrity_face_classifierv47.keras")

# Set the title of the app
st.title("Face ID with Fine-Tuned VGG16")

# Initialize session state variables
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "login_image" not in st.session_state:
    st.session_state.login_image = None
if "registered" not in st.session_state:
    st.session_state.registered = False
if "user_name" not in st.session_state:
    st.session_state.user_name = None
if "database_image" not in st.session_state:
    st.session_state.database_image = None

st.session_state.prediction = None
st.session_state.predicted_class_index = None


# Register dialog
@st.dialog("Register")
def register():
    if st.session_state.registered:
        st.info("You are already registered")
        return

    name = st.text_input("Full Name", placeholder="Enter your name")
    picture = st.camera_input("Take a picture")
    if st.button("Submit"):
        if len(name) < 3:
            st.error("Name must be at least 3 characters")
        elif not picture:
            st.error("Please take a picture")
        else:
            try:
                # Save the picture to the celebrities folder
                os.makedirs("celebrities", exist_ok=True)
                with open(f"celebrities/{name}.jpg", "wb") as f:
                    f.write(picture.getvalue())
                st.success(f"You are registered as {name}")
                st.warning("You can now close this dialog and log in")
                st.session_state.registered = True
            except Exception as e:
                st.error(f"An error occurred: {e}")

# Login dialog


@st.dialog("Log in")
def login():
    # Video camera
    camera_image = st.camera_input("Take a picture")

    st.divider()

    # Upload image
    uploaded_image = st.file_uploader("Upload an image")

    # Submit button to check if there is a camera image or an uploaded image
    if st.button("Submit"):
        if camera_image or uploaded_image:
            try:
                # Initialize the VGG16 feature extractor
                image_size = (128, 128)  # VGG16 input size
                feature_extractor = VGG16(weights='imagenet', include_top=False, input_shape=(
                    image_size[0], image_size[1], 3))
                feature_extractor.trainable = False  # Freeze the feature extractor
                # Save the captured or uploaded image temporarily
                image_to_check = camera_image if camera_image else uploaded_image
                with open("temp_login_image.jpg", "wb") as f:
                    f.write(image_to_check.getvalue())

                # Load and preprocess the image for VGG16
                img = image.load_img("temp_login_image.jpg",
                                     target_size=image_size)
                img_array = image.img_to_array(img)
                img_array = np.expand_dims(
                    img_array, axis=0)  # Add batch dimension
                img_array = preprocess_input(img_array)  # Preprocess for VGG16

                # Extract features using VGG16
                features = feature_extractor.predict(img_array)
                features = features.reshape(1, -1)  # Flatten the features

                # Predict the class of the image using the classification model
                prediction = model.predict(features)
                predicted_class_index = np.argmax(prediction, axis=1)[0]

                st.session_state.prediction = prediction
                st.session_state.predicted_class_index = predicted_class_index

                # Map the predicted class index to the user's name
                class_to_name = {
                    i: name.split(".")[0] for i, name in enumerate(sorted(os.listdir("celebrities")))
                }

                if predicted_class_index in class_to_name:
                    name = class_to_name[predicted_class_index]
                    database_image = f"celebrities/{name}.jpg"

                    # Update session state
                    st.session_state.logged_in = True
                    st.session_state.user_name = name
                    st.session_state.database_image = database_image
                    st.session_state.login_image = image_to_check

                    st.success(f"Welcome back, {name}!")
                    st.rerun()  # Rerun the app to update the layout
                else:
                    st.error(
                        "No match found in the database. Please register first.")
            except Exception as e:
                st.error(f"An error occurred: {e}")
        else:
            st.error("Please take a picture or upload an image")


# Display login or register buttons if not logged in
if not st.session_state.logged_in:
    # Display exclusive content message
    st.write("This content is exclusive for registered users")
    left, right = st.columns(2)
    if left.button("Register", type="primary", use_container_width=True):
        register()
    if right.button("Log in", type="secondary", use_container_width=True):
        login()

# Display the body after logging in
if st.session_state.logged_in:
    st.sidebar.write(
        f"Welcome to the exclusive content!")
    st.sidebar.write(f"**{st.session_state.user_name}**")
    st.sidebar.button("Log out", on_click=lambda: st.session_state.clear())
    st.write(f"Welcome, {st.session_state.user_name}!")
    col1, col2 = st.columns(2)
    with col1:
        st.image(st.session_state.database_image,
                 caption="Your Profile Picture", use_container_width=True)
    with col2:
        st.image(st.session_state.login_image,
                 caption="Image Taken", use_container_width=True)

    st.subheader("Demo Gif")
    st.image('demo.gif')

    def convert_notebook_to_html(notebook_path):
        # Load the notebook
        with open(notebook_path, 'r', encoding='utf-8') as f:
            notebook_content = nbformat.read(f, as_version=4)

        # Convert to HTML
        html_exporter = HTMLExporter()
        html_body, _ = html_exporter.from_notebook_node(notebook_content)

        return html_body

    # Streamlit app

    def main():
        st.title("Jupyter Notebook Viewer")

        # Path to the Jupyter notebook
        notebook_path = "face_recognition.ipynb"

        if os.path.exists(notebook_path):
            # Convert notebook to HTML
            html_content = convert_notebook_to_html(notebook_path)

            # Display the HTML content in Streamlit
            st.components.v1.html(html_content,
                                  height=1200, scrolling=True)
        else:
            st.error(f"Notebook file not found: {notebook_path}")

    if __name__ == "__main__":
        main()
