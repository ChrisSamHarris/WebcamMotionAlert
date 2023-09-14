import cv2
import streamlit as st 
from datetime import datetime

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
            break
        time_live = datetime.now().strftime("%H:%M:%S")
        check, frame = camera.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        cv2.putText(img=frame, text=time_live, org=(80, 1050),
                    fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=4, color=(57,255,20),
                    thickness=2, lineType=cv2.LINE_AA)
        
        streamlit_image.image(frame)

if start:
    webcam()