import pandas as pd
from PIL import Image
import streamlit as st
from streamlit_drawable_canvas import st_canvas

def draw_rect(bg_image):
    canvas_result = st_canvas(
    fill_color="rgba(255, 165, 0, 0.3)",  # 设置填充颜色和透明度
    stroke_width=3,
    background_color="#eee",
    background_image=(bg_image) if bg_image else None,  # 照片
    drawing_mode="rect",  # 设置为只能画矩形
    key="canvas",
    )
    target_width,target_height=bg_image.size
    scale_width = target_width / 600
    scale_height = target_height / 400
    
    if canvas_result.json_data is not None:
        objects = pd.json_normalize(canvas_result.json_data["objects"])  # 轉換 json_data-> DataFrame
        
        if not objects.empty:
            
            latest_rect = objects.iloc[-1]
            x1 = latest_rect['left']
            y1 = latest_rect['top']
            x2 = x1 + latest_rect['width']
            y2 = y1 + latest_rect['height']

            x1_scaled = x1 * scale_width
            x2_scaled = x2 * scale_width
            y1_scaled = y1 * scale_height
            y2_scaled = y2 * scale_height

            coordinates = (int(x1_scaled), int(y1_scaled), int(x2_scaled), int(y2_scaled))
            
            return coordinates
    