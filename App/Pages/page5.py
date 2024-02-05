import streamlit as st

def show():
    st.title("Create a Dockerfile")

    st.markdown("""
- Open a text editor on your computer (like Notepad on Windows, TextEdit on
  macOS, or any code editor like VSCode). **Recommended**: VSCode will automatically detect the
  following code as a Dockerfile, and prompt you to install the Docker
  extension for easy use.
- Copy and paste the following content into the text editor:
```
# Use an official Python runtime as a parent image
FROM python:3.8

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 8050 available to the world outside this container
EXPOSE 8050

# Define environment variable
ENV NAME World

# Run app.py when the container launches
CMD ["streamlit", "run", "app.py"]
```
- Save this file in the root directory of your Streamlit app with the name Dockerfile (make sure it's not saved with a .txt extension).
"""
    )

    st.image("Images/dockerfile.png", caption="Dockerfile Contents (VSCode)", width=800)
    st.image("Images/dockerfile_explorer.png", caption="The Dockerfile Within Your App.py Folder", width=800)