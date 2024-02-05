import streamlit as st
from Pages import page1,page2, page3, page4, page5

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
        "ML"
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
    elif selected_page == "ML":
        page5.show()

if __name__ == "__main__":
    main()
