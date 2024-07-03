from deep_sort_pytorch.utils.parser import get_config
from deep_sort_pytorch.deep_sort import DeepSort
import os
import cv2
import logging
import torch
import streamlit as st
from ultralytics import YOLOv10  # type: ignore
from PIL import Image

# 設定日誌記錄
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# 初始化追踪器
def init_tracker():
    """
        初始化追蹤器
    """
    cfg_deep = get_config()
    cfg_deep.merge_from_file("deep_sort_pytorch/configs/deep_sort.yaml")
    global deepsort
    deepsort = DeepSort(
        cfg_deep.DEEPSORT.REID_CKPT,
        max_dist=cfg_deep.DEEPSORT.MAX_DIST,
        min_confidence=cfg_deep.DEEPSORT.MIN_CONFIDENCE,
        nms_max_overlap=cfg_deep.DEEPSORT.NMS_MAX_OVERLAP,
        max_iou_distance=cfg_deep.DEEPSORT.MAX_IOU_DISTANCE,
        max_age=cfg_deep.DEEPSORT.MAX_AGE,
        n_init=cfg_deep.DEEPSORT.N_INIT,
        nn_budget=cfg_deep.DEEPSORT.NN_BUDGET,
        use_cuda=True
    )
    return deepsort

# 初始化視頻捕捉
def initialize_video_capture(video_input):
    """
        參數解釋：
        video_input：輸入參數可以是字符串或數字。如果是字符串，通常表示的是一個文件路徑（例如一個視頻文件）。如果是數字，通常表示的是連接到計算機的攝像頭的索引（例如 0 通常是計算機預設的攝像頭）。
        
        返回值：
        返回值：函數返回創建的 cv2.VideoCapture 物件。這個物件可以用來在後續代碼中通過調用 .read() 方法來逐幀讀取視頻。
    """

def initialize_video_capture(video_input):
    if isinstance(video_input, st.runtime.uploaded_file_manager.UploadedFile):
        # 保存上傳的影片文件到臨時文件
        video_path = "output/temp_video.mp4"
        with open(video_path, "wb") as f:
            f.write(video_input.read())
        cap = cv2.VideoCapture(video_path)
    elif isinstance(video_input, str) and video_input.isdigit():
        # 處理攝像頭輸入
        cap = cv2.VideoCapture(int(video_input))
    else:
        # 處理影片文件輸入
        cap = cv2.VideoCapture(video_input)
    return cap

def initialize_video_image(cap):
    
    ret, frame = cap.read()
    if ret:
        # 將 BGR 圖像轉換為 RGB 圖像
        img_RGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        # 將 numpy 數組轉換為 PIL 圖像以在 Streamlit 中顯示
        img = Image.fromarray(img_RGB)
        return img
    else:
        st.error("無法讀取視頻的第一幀")
        
    
# 初始化模型
def initialize_model():
    """
        讀取且初始化 YOLOV10 載入權重
    """
    model_path = "./weights/yolov10x.pt"
    if not os.path.exists(model_path):
        logger.error(f"模型權重文件不存在於 {model_path}")
        raise FileNotFoundError("模型權重文件未找到")
    
    model = YOLOv10(model_path)
    if torch.cuda.is_available():
        device = torch.device("cuda")
    elif torch.backends.mps.is_available():
        device = torch.device("mps")
    else:
        device = torch.device("cpu")
    
    model.to(device)
    logger.info(f"使用 {device} 進行處理")
    return model

# 加載類別名稱
def load_class_names():
    """
        載入COCO 類別名稱
    """
    classes_path = "./data/coco.names"
    if not os.path.exists(classes_path):
        logger.error(f"類別名稱文件未找到於 {classes_path}")
        raise FileNotFoundError("類別名稱文件未找到")
    
    with open(classes_path, "r") as f:
        class_names = f.read().strip().split("\n")
    return class_names
