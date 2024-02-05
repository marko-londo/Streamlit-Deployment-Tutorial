import streamlit as st

def show():
    image_url = "https://github.com/marko-londo/Streamlit-Deployment-Tutorial/blob/main/App/Images/shaolin_ai_logo.png?raw=true"
    
    # Center the image using custom CSS
    st.write(
        f'<div style="display: flex; justify-content: center;"><img src="{image_url}" width="400"></div>'"<br><br>",
        unsafe_allow_html=True,
    )

    # Add a centered subheader
    st.write(
        '<div style="text-align: center;"><h1>Streamlit App Deployment Tutorial</h1></div>'"<br><br>",
        unsafe_allow_html=True,
    )

    st.write(
        '<div style="text-align: center;"><h4><i>Learn how to deploy your Streamlit app to the web using Google Cloud Platform and Docker.</i></h4></div>',
        unsafe_allow_html=True,
    )    
