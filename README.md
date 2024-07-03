# yolov10_deepsort_streamlit

# 系統說明
本系統使用 streamlit 做出一個簡易介面，可以任意調整框的大小或者是線的Y軸，實踐出yolov10的跟蹤功能，跟蹤使用deepsort

## 初始畫面
![image](https://github.com/nigunosong88/yolov10_deepsort_streamlit/blob/main/images/1.jpg)

## 基礎使用畫面
![image](https://github.com/nigunosong88/yolov10_deepsort_streamlit/blob/main/images/2.jpg)

## 無使用EfficientSAM基礎使用畫面
![image](https://github.com/nigunosong88/yolov10_deepsort_streamlit/blob/main/images/2nosam.jpg)

## 無使用EfficientSAM yoloworld 輸入dog 基礎使用畫面
![image](https://github.com/nigunosong88/yolov10_deepsort_streamlit/blob/main/images/dog.jpg)

## 使用EfficientSAM yoloworld 輸入dog 基礎使用畫面
![image](https://github.com/nigunosong88/yolov10_deepsort_streamlit/blob/main/images/dogsam.jpg)



# 專案運行方式
安裝環境後，確認文件內容路徑無誤，即可run app.py
# 資料夾說明
- utils
  - 主要架構 yoloworld 與 EfficientSAM
- images
  - 放置實際操作畫面
- yolo_world
  - yolo_world官方其他副程式
# 使用技術
# 主要庫版本
Gradio: 4.26.0  \
EfficientSAM: 版本未指定 \
Segment Anything  \
Yoloworld: 版本未指定 
# 使用版本
python=3.8 \
cuda=11.7 \
gradio=4.16.0 \
inference-gpu=0.9.16 \
mmcv=2.0.0 \
mmdeploy=0.14.0 \
mmengine=0.10.3 \
mmyolo=0.6.0 \
pytorch=1.12.1 \
supervision=0.20.0 
