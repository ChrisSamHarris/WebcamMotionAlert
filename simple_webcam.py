import cv2
import streamlit as st 

st.set_page_config(page_title="Motion Detector", page_icon="📸")

st.title("Motion Detector")
placeholder = st.empty()
start = placeholder.button('Start Camera', key="start")

def webcam():
    stop = placeholder.button('Stop Camera', key="stop")
    streamlit_image = st.image([])
    camera = cv2.VideoCapture(0)

    while True:
        if stop:
            start = placeholder.button('Start Camera', key="start_regen")
            break
        check, frame = camera.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        cv2.putText(img=frame, text="Hello", org=(50, 50),
                    fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=2, color=(20,100,200),
                    thickness=2, lineType=cv2.LINE_AA)
        
        streamlit_image.image(frame)

if start:
    webcam()
    