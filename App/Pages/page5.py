import streamlit as st

def show():
    st.title("Create a Dockerfile")

    st.markdown("""
- Open a text editor on your computer (like Notepad on Windows, TextEdit on
  macOS, or any code editor like VSCode).
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

# Make port 8501 available to the world outside this container
EXPOSE 8501

# Define environment variable
ENV NAME World

# Run app.py when the container launches
CMD ["streamlit", "run", "app.py"]
```
- Save this file in the root directory of your Streamlit app with the name Dockerfile (make sure it's not saved with a .txt extension).
"""
    )

    st.image("Images/dockerfile.png", caption="Dockerfile Contents (VSCode)", width=800)
    st.image("Images/dockerfile_explorer.png", caption="The Dockerfile Within Your App.py Root Directory", width=800)

    st.markdown("""
Next we will need to create a requirements.txt. This will provide the
  required packages to run your app.
- Open a text editor on your computer.
- Write the name of any packages required to run your app (streamlit, pandas,
  etc) and their specific versions if necessary. It
  should look something like this:
                
"""
    )
    st.image("Images/requirements-txt.png", caption="The Requirements.txt's Contents", width=400)

    st.markdown("""
- Verify it is saved within your App's root directory:
                
"""
    )

    st.image("Images/requirements.png", caption="The Requirements.txt Within Your App.py Root Directory", width=800)

    st.markdown("""
Now that you have the Dockerfile and requirements.txt ready, we can build a
Docker Image.
                
"""
    )