import streamlit as st
import os
import cv2
import numpy as np
from sklearn.svm import SVC
from sklearn.preprocessing import LabelEncoder
from sklearn.decomposition import PCA
import joblib
from mtcnn import MTCNN
import nbformat
from nbconvert import HTMLExporter

# Set the title of the app
st.title("Face ID with SVM")

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

# Load pre-trained models
model_filename = 'celebrity_face_recognition_model.pkl'
pca_filename = 'pca.pkl'
label_encoder_filename = 'label_encoder.pkl'

if os.path.exists(model_filename) and os.path.exists(pca_filename) and os.path.exists(label_encoder_filename):
    model = joblib.load(model_filename)
    pca = joblib.load(pca_filename)
    label_encoder = joblib.load(label_encoder_filename)
else:
    st.error("Model files not found. Please train the model first.")
    st.stop()

# Initialize MTCNN face detector
detector = MTCNN()

# Function to preprocess and predict face


def predict_face(image):
    # Convert image to RGB
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Detect face using MTCNN (or any other face detector)
    faces = detector.detect_faces(image_rgb)
    if faces:
        x, y, width, height = faces[0]['box']
        face = image_rgb[y:y+height, x:x+width]
        face = cv2.resize(face, (160, 160))

        # Extract features using PCA
        face_pca = pca.transform(face.reshape(1, -1))

        # Predict using SVC
        predicted_label = model.predict(face_pca)
        predicted_name = label_encoder.inverse_transform(predicted_label)[0]
        return predicted_name
    else:
        return None

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
                # Save the captured or uploaded image temporarily
                image_to_check = camera_image if camera_image else uploaded_image
                with open("temp_login_image.jpg", "wb") as f:
                    f.write(image_to_check.getvalue())

                # Load the image for prediction
                image = cv2.imread("temp_login_image.jpg")
                if image is None:
                    st.error("Failed to load the image.")
                    return

                # Predict the face
                predicted_name = predict_face(image)
                if predicted_name:
                    # Update session state
                    st.session_state.logged_in = True
                    st.session_state.user_name = predicted_name
                    st.session_state.database_image = f"celebrities/{predicted_name}.jpg"
                    st.session_state.login_image = image_to_check

                    st.success(f"Welcome back, {predicted_name}!")
                    st.rerun()  # Rerun the app to update the layout
                else:
                    st.error(
                        "No face detected or no match found in the database. Please register first.")
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
