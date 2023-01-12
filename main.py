import streamlit as st
import cv2
import datetime as dt


st.title("Monitor Detector")

start = st.button("Start Camera")


if start:
    streamlit_image = st.image([])
    camera = cv2.VideoCapture(0)

    while True:
        today = dt.datetime.now()
        day_name = today.strftime("%A")
        clock = today.strftime("%H:%M:%S")
        check, frame = camera.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        cv2.putText(img=frame, text=day_name, org=(50, 50),
                    fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=2,
                    color=(20, 100, 200), thickness=2, lineType=cv2.LINE_AA)
        
        cv2.putText(img=frame, text=clock, org=(500, 450),
                    fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=2,
                    color=(255, 0, 0), thickness=2, lineType=cv2.LINE_AA)
        
        streamlit_image.image(frame)