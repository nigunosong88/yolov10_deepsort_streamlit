import torch
from absl import app, flags
from deep_sort_pytorch.deep_sort import DeepSort
from util.config import FLAGS
# 處理單幀
def process_frame(frame, model,deepsort):
    """
        讀取影片每一偵，寫入追蹤器，
        回傳output~
    """
    # 處理單幀
    xywh_bboxs = [] # 框框
    confs = [] # 置信度
    clss = [] # 分類
    outputs = []
    im0 = frame.copy()
    results = model(im0, verbose=False)[0] # 只會框到一個
    for det in results.boxes:
        
        if FLAGS.class_id == None:
            x_c, y_c, bbox_w, bbox_h = xyxy_to_xywh(*det.xyxy[0])
            xywh_obj = [x_c, y_c, bbox_w, bbox_h]
            xywh_bboxs.append(xywh_obj)
            confs.append([det.conf.item()])
            clss.append(int(det.cls.item()))
        elif (det.cls.item()) == FLAGS.class_id:
            x_c, y_c, bbox_w, bbox_h = xyxy_to_xywh(*det.xyxy[0])
            xywh_obj = [x_c, y_c, bbox_w, bbox_h]
            xywh_bboxs.append(xywh_obj)
            confs.append([det.conf.item()])
            clss.append(int(det.cls.item()))
        

    xywhs = torch.Tensor(xywh_bboxs)
    confss = torch.Tensor(confs)

    outputs = deepsort.update(xywhs, confss, clss, im0)
    return outputs

def xyxy_to_xywh(*xyxy):
    """"從絕對像素值計算相對邊界框。"""
    bbox_left = min([xyxy[0].item(), xyxy[2].item()])
    bbox_top = min([xyxy[1].item(), xyxy[3].item()])
    bbox_w = abs(xyxy[0].item() - xyxy[2].item())
    bbox_h = abs(xyxy[1].item() - xyxy[3].item())
    x_c = (bbox_left + bbox_w / 2)
    y_c = (bbox_top + bbox_h / 2)
    w = bbox_w
    h = bbox_h
    return x_c, y_c, w, h