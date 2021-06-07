import os
import streamlit as st
import cv2
import subprocess
from PIL import Image

def main():
    readme_text = st.markdown(open("README.md", 'r').read())

    st.sidebar.title("What to do")
    app_mode = st.sidebar.selectbox(
        "Choose the app mode", ["Show readme", "Run the app"]
        )
    if app_mode == "Show readme":
        st.sidebar.success('To continue select "Run the app".')
    elif app_mode == "Run the app":
        readme_text.empty()
        run_the_app()

def run_the_app():
    st.title("Interact with the app.")
    TEXT = """
    The video below shows exactly what the model does.
    """
    st.markdown(
        f'<p style="font-family:san-serif; font-size:24px">{TEXT}</p>',
        unsafe_allow_html=True
        )
    video_file = open('cow2.mp4', 'rb')
    video_bytes = video_file.read()
    st.video(video_bytes)
    st.write("Try with a custom image.")
    uploaded_file = st.file_uploader("Upload an image file...", type=[".png", ".jpg"])
    if uploaded_file:
        img = Image.open(uploaded_file)
        img.save("./images/test.jpg")
        img.close()
        command = "python detect.py --source ./images/test.jpg --weights runs/train/cow_det7/weights/best.pt --conf 0.2 --name output --img-size 600"
        subprocess.call(command, shell=True)
        img = Image.open("./output/test.jpg")
        st.image(img, caption="prediction")    

if __name__ == "__main__":
    main()
