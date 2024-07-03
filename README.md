# yolov10_deepsort_streamlit

# 系統說明
本系統使用 streamlit 做出一個簡易介面，可以任意調整框的大小或者是線的Y軸，實踐出yolov10的跟蹤功能，跟蹤使用deepsort

## 初始畫框畫面
![image](https://github.com/nigunosong88/yolov10_deepsort_streamlit/img/1.jpg)

## 基礎畫線畫面
![image](https://github.com/nigunosong88/yolov10_deepsort_streamlit/img/2.jpg)

## 畫框結果
![image](https://github.com/nigunosong88/yolov10_deepsort_streamlit/output/box.git)

## 畫線結果
![image](https://github.com/nigunosong88/yolov10_deepsort_streamlit/output/line.git)




# 專案運行方式
安裝環境後，確認文件內容路徑無誤，即可streamlit run app.py
# 資料夾說明
- utils
- img
  - 放置實際操作畫面
- deep_sort_pytorch
  - deepsort 副程式
- weights
  - 權重檔
# 使用技術
# 主要庫版本
參考requirements.txt
