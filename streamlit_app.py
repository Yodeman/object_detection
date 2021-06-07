import os
import streamlit as st
import cv2

def main():
    readme_text = st.markdown(open("README1.md", 'r').read())

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

if __name__ == "__main__":
    main()
