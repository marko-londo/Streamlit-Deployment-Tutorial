import streamlit as st

def show():
    st.title("Tag and Push the Docker Image to Google Container Registry")

    st.markdown("""
- While still within the directory where your Dockerfile is located, run the
  following command:
```cmd
gcloud auth login

```
- Log in, and then in the run the following command:
```cmd
gcloud auth configure-docker

```
- Hit "y" when prompted.                  

- Tag your Docker image with the Google Container Registry (GCR) URL:
```cmd
docker tag your-image-name:tag gcr.io/your-project-id/your-image-name:tag

```
(Replace "your-image-name : tag" with the image name and tag you used in the previous step, and "your-project-id" with your actual GCP project ID.)
"""
    )
    
    st.image("Images/tagging.png", caption="Run the Tagging Command", width=800)

    st.markdown("""
- Run the following command:
```cmd
docker push gcr.io/your-project-id/your-image-name:tag

```
If successful it should look something like this:
                """
    )

        
    st.image("Images/successful_push.png", caption="docker push gcr.io/shaolin-streamlit-app-demo/shaolin-demo:latest", width=800)