import streamlit as st
import nbformat
from nbconvert import HTMLExporter
import os

# Function to convert Jupyter notebook to HTML
# To be used on Streamlit app


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
    notebook_path = "testv4 copy 2.ipynb"

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
