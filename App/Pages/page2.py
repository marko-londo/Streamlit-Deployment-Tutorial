import streamlit as st

def show():
    st.title("Docker Installation")
    st.markdown("""

    - Navigate to the [Docker Desktop download page](https://www.docker.com/products/docker-desktop/)
    - Click Download for Windows (or hover for other options), and download the **Docker Desktop Installer**.
        """)
    st.image("Images/download.png", caption="Docker Download", width=300)

    st.markdown("""
        - Run the installer.
        - Once installation is complete, you'll have to restart your PC.
        - After restarting, open the Docker Desktop app and complete the installation by accepting the terms and selecting "Use recommended settings" and clicking finish.
        """)
    st.image("Images/complete_installation.png", caption="Complete Installation", width=1000)

    st.markdown("""
        - Create a new account or sign in to Docker using GitHub.
        - Once logged in your Docker account, your docker app should look something like this:
        """)
    st.image("Images/logged_in.png", caption="Docker App", width=600)

    st.markdown("""
        - Open a terminal or command prompt and verify that Docker is properly installed by running:
        ```cmd
        docker --version
        ```
        You should see something like this:
        """)
    st.image("Images/docker_version.png", caption="Docker Version", width=400)

    st.markdown("""
        - Test Docker by running the following command:
        ```cmd
        docker run hello-world
        ```
        You should see something like this:
        """)
    st.image("Images/hello-world.png", caption="Hello World", width=1000)
