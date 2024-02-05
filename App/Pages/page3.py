import streamlit as st

def show():
    st.title("Google Cloud Platform (GCP) Account Setup")

    st.markdown("""
- First you'll need a Google account. If you don't have one, create one
  [here](https://support.google.com/accounts/answer/27441?hl=en).
                
    -  Google Cloud offers $300 dollars in free credits, so if you've already exhausted these
  with your current Google account (or simply prefer to manage your GCP
  separately from your main Google account), I would suggest creating a new
  one.
                
    Whether or not you choose to utilize the free credits, it is necessary to input
    payment information. However, rest assured that the likelihood of incurring
    charges is minimal when using a small dashboard app, provided you do not exert
    substantial computing power. You have the option to deactivate the app from the
    console, preventing access, and can configure notifications to alert you about
    any potential charges. The free $300 in credits will go a long way!
"""
    )

    st.image("Images/free_cred.png", caption="Google Cloud Credits", width=300)

    st.markdown("""
- Once you have a Google account, sign in to the [Google Cloud Console](https://console.cloud.google.com/).
- Click on the "Select a project" drop-down menu at the top left of the page and select "New Project".

"""
    )

    st.image("Images/create_new.png", caption="Creating a New Project", width=1000)

    st.markdown("""
- Add a project name and click "CREATE" (You can ignore the Location option)
                
- You should get a notification that your project has been created.

"""
    )