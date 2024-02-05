import streamlit as st
from Pages import page1,page2, page3, page4, page5, page6, page7, page8

favicon = "Images/favicon.ico"

st.set_page_config(
    page_title="ShaolinAI Streamlit-Deployment-Tutorial",
    page_icon=favicon,
    layout="wide",
    menu_items=None,
)


no_sidebar_style = """
    <style>
        div[data-testid="stSidebarNav"] {display: none;}
    </style>
"""
st.markdown(no_sidebar_style, unsafe_allow_html=True)


def main():
    st.sidebar.title("Navigation")
    page_options = [
        "Home",
        "Docker Installation",
        "Google Cloud Platform (GCP) Account Setup",
        "Configure Google Cloud SDK",
        "Create a Dockerfile",
        "Build a Docker Image",
        "Tag and Push the Docker Image to Google Container Registry",
        "Deploy the Streamlit App on Google Cloud Run"
        ]
    selected_page = st.sidebar.radio("Select Page", page_options)

    if selected_page == "Home":
        page1.show()
    elif selected_page == "Docker Installation":
        page2.show()
    elif selected_page == "Google Cloud Platform (GCP) Account Setup":
        page3.show()
    elif selected_page == "Configure Google Cloud SDK":
        page4.show()
    elif selected_page == "Create a Dockerfile":
        page5.show()
    elif selected_page == "Build a Docker Image":
        page6.show()
    elif selected_page == "Tag and Push the Docker Image to Google Container Registry":
        page7.show()
    elif selected_page == "Deploy the Streamlit App on Google Cloud Run":
        page8.show()

if __name__ == "__main__":
    main()
