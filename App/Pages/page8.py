import streamlit as st

def show():
    st.title("Deploy the Streamlit App on Google Cloud Run")

    st.markdown("""

- Open the [Google Cloud Console](https://console.cloud.google.com/)
- In the left-hand navigation menu, click on "Cloud Run."
- Click the "Create Service" button.
- Select your project and region.
- Select "CPU is only allocated during request processing"
- Allow unauthenticated invocations
- Hit create
"""
    )
    st.image("Images/cloud_run.png", caption="Cloud Run", width=800)

    st.markdown("""
Congratulations! You've successfully deployed your first Streamlit App!
"""
    )