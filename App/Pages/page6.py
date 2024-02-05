import streamlit as st

def show():
    st.title("Build a Docker Image")

    st.markdown("""
- Open a terminal or command prompt.
- Navigate to the directory where your Dockerfile and requirements.txt are
  located. You can use the cd command to change directories:
```cmd
cd /path/to/your/app
```
- Build the Docker image using the following command:
```cmd
docker build -t your-image-name .
```
(Replace your-image-name with a unique name for your Docker image. This command
tells Docker to build an image using the Dockerfile in the current directory.)

Once completed, you should see something like this:
                
                """
    )
    st.image("Images/docker_image.png", caption="Succesfully Created Docker Image", width=800)

    st.markdown("""
Verify the image exists and view it's tag by running
```cmd
docker images
```
                
                """)
    
    st.image("Images/docker_image_tag.png", caption="Run Docker Image", width=800)