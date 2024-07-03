import cv2
# 繪製跟踪路徑及統計資訊
def draw_tracks(frame, outputs, class_names, colors, class_counters,num_counters, track_class_mapping, offset=(0, 0)):
   
    for track in outputs:
        if not len(track)>0:
            continue

        track_box = track[:4] # 框
        num_id = track[4]
        class_id = track[5]  

        x1, y1, x2, y2 = map(int, track_box) # 將框數據轉為4個座標
        color = colors[class_id]
        B, G, R = map(int, color)
        
        if num_id not in track_class_mapping:
            class_counters[class_id] += 1  # 有新的num id 時 class_counters 會加1
            track_class_mapping[num_id] = class_counters[class_id]  # 再丟入我的追蹤內的相對id
            
        class_specific_id = track_class_mapping[num_id]
        text = f"{class_specific_id} - {class_names[class_id]}"

        # 背景大小設定
        (text_width, text_height), _ = cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX, 0.5, 2)

        # 背景文字座標
        text_offset_x = x1 + 5
        text_offset_y = y1 - 18
        background_top_left = (text_offset_x, text_offset_y - text_height)
        background_bottom_right = (text_offset_x + text_width, text_offset_y + text_height)

        # 畫背景
        cv2.rectangle(frame, background_top_left, background_bottom_right, (B, G, R), cv2.FILLED)
        # 畫框
        cv2.rectangle(frame, (x1, y1), (x2, y2), (B, G, R), 2)
        cv2.putText(frame, text, (x1 + 5, y1 - 18), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
       
    return frame