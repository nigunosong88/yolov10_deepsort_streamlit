import streamlit as st 
from PIL import Image, ImageDraw

def draw_line(uploaded_file):
        
    st.image(uploaded_file, caption='上傳的圖片', use_column_width=True)
    width, height = uploaded_file.size

    # 添加滑條來選擇線條的位置
    y_start = st.slider('選擇起始點Y坐標', min_value=0, max_value=height, value=height//4)

    # 在圖像上繪製線條
    draw = ImageDraw.Draw(uploaded_file)
    draw.line((width//4, y_start, 3*width//4, y_start), fill="red", width=8)
    
    # 顯示繪製線條後的圖像
    st.image(uploaded_file, caption='繪製線條後的圖片', use_column_width=True)
    return y_start