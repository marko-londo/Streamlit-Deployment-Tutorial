import streamlit as st

def show():
    st.title("Configure Google Cloud SDK")

    st.markdown("""
- Navigate to the [gcloud CLI
  documentation](https://cloud.google.com/sdk/docs/install) and download the
  Google Cloud CLI installer.
- Install the Google Cloud CLI. Make sure bundle Python is selected.
- After installation, run the following command to initialize the SDK:
                ```cmd
                gcloud init
                ```                
- When prompted, hit "y" and then enter to log in. A browswer window will open
  prompting you to log in. Use the account you created your GCP project with,
  and then hit "Continue" and "Allow".
- You will be asked to select a cloud project to use. Type in the number next
  to the name of the one you've created for this deployment (if you only have
  one, it should just be 1), and hit enter. This will configure your Google
  Cloud SDK.
                """
    )
    st.image("Images/google_sdk_login.png", caption="Select Your Project", width=600)