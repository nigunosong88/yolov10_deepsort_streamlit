import cv2
from absl import app, flags
from collections import defaultdict
from util.tracks_count import tracks_num
from util.process_frame import process_frame
from util.draw_tracks import draw_tracks
from util.initialize import init_tracker,initialize_model,initialize_video_capture,load_class_names,initialize_video_image
import numpy as np

# 定義命令行參數
FLAGS = flags.FLAGS

def yolov10_deepsort(coordinates,y_line,deepsort):

    cap = initialize_video_capture("output/temp_video.mp4")
    model = initialize_model()
    class_names = load_class_names()

    # 存影片
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    writer = cv2.VideoWriter(FLAGS.output, fourcc, fps, (frame_width, frame_height))
    
    colors = np.random.randint(0, 255, size=(len(class_names), 3))
    class_counters = defaultdict(int) # 用於分配 id
    num_counters = defaultdict(int) # 用於計算 id
    box_counters = defaultdict(int) 
    track_class_mapping = {}
    track_class_line = {}  
    track_class_box = {}  

    while True:
        ret, frame = cap.read() #ret 是顯示有無被讀取到
        if not ret:    #如果沒有讀取到 跳出迴圈
            break
        tracks = process_frame(frame, model,deepsort)
        frame = draw_tracks(frame, tracks, class_names, colors, class_counters,num_counters, track_class_mapping)
        numf = tracks_num(frame,tracks,class_names,track_class_line,num_counters,box_counters,track_class_box,y_line,coordinates)
        writer.write(numf)

    cap.release()
    writer.release()