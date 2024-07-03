import streamlit as st
import numpy as np
from PIL import Image, ImageDraw
from absl import app, flags

from util.initialize import initialize_video_capture,initialize_video_image,init_tracker
from util.draw_line import draw_line
from util.yolov10_deepsort import yolov10_deepsort
from util.config import FLAGS
from util.draw_box import draw_rect
import subprocess
def convert_video(input_file, output_file, crf=23):
    command = [
        'ffmpeg',
        '-y',
        '-i', input_file,
        '-vcodec', 'libx264',
        '-crf', str(crf),
        output_file
    ]
    subprocess.run(command, check=True)


def main(_argv):
    coordinates=[]
    y_line=0
    uploaded_file = st.file_uploader("選擇一個影片", type=["mp4","jpg", "jpeg", "png"])
    deepsort = init_tracker()
    if uploaded_file is not None:
        cap = initialize_video_capture(uploaded_file)
        
        tab1, tab2 = st.tabs(["📈 BOX", "🗃 LINE"])
        one_image=initialize_video_image(cap)
        two_img=one_image
        
        with tab1:
            # 設置頁面標題
            st.title('Streamlit 在圖像上畫框')
            coordinates=draw_rect(one_image)

            if st.button('開始跟蹤記數-BOX'):
                FLAGS.output = "output/box.mp4"
                yolov10_deepsort(coordinates,0,deepsort)
                convert_video('output/box.mp4', 'output/output.mp4')
                video_file = open("output/output.mp4" ,"rb")
                video_bytes = video_file.read()
                st.video(video_bytes)


        with tab2:
            # 設置頁面標題
            st.title('Streamlit 在圖像上畫線')
            y_line = draw_line(two_img)
        
            if st.button('開始跟蹤記數-LINE'):
                FLAGS.output = "output/line.mp4"
                yolov10_deepsort(coordinates,y_line,deepsort)
                convert_video('output/line.mp4', 'output/output.mp4')
                video_file = open("output/output.mp4" ,"rb")
                video_bytes = video_file.read()
                st.video(video_bytes)
                
if __name__ == "__main__":
    app.run(main)

