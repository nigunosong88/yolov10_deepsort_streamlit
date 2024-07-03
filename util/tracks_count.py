import cv2

def tracks_num(frame,outputs,class_names,track_class_line,num_counters,box_counters,track_class_box,y_line,coordinates):

    height, width, _ = frame.shape 
    for track in outputs:
        if not len(track)>0:
            continue
        
        track_box = track[:4] # 框
        num_id = track[4]
        class_id = track[5]  
        
        x1, y1, x2, y2 = map(int, track_box)
        x_c = (x1 + x2) // 2
        y_c = (y1 + y2) // 2
        if y_line !=0 :
        
            cv2.line(frame, (100, y_line), (1050, y_line), (46,162,112), 3)  # 繪製門檻線
        
            # 畫線計算
            if  y1 < y_line and y2 > y_line:
                cv2.line(frame, (100, y_line), (1050, y_line), (255,255,255), 3)  # 繪製門檻線
                if num_id not in track_class_line:
                    num_counters[class_id] += 1  # 有新的num id 時 class_counters 會加1
                    track_class_line[num_id] = num_counters[class_id]  # 再丟入我的追蹤內的相對id


            for idx, (key, value) in enumerate(num_counters.items()):
                class_name = class_names[key]  
                cnt_str = str(class_name) + ":" +str(value)
                cv2.line(frame, (width - y_line,25), (width,25), [85,45,255], 40)
                cv2.putText(frame, f'Number of Vehicles Entering', (width - y_line, 35), 0, 1, [225, 255, 255], thickness=2, lineType=cv2.LINE_AA)
                cv2.line(frame, (width - 150, 65 + (idx*40)), (width, 65 + (idx*40)), [85, 45, 255], 30)
                cv2.putText(frame, cnt_str, (width - 150, 75 + (idx*40)), 0, 1, [255, 255, 255], thickness = 2, lineType = cv2.LINE_AA)
        else:
            
            (x_one, y_one, x_two, y_two) = coordinates

            cv2.rectangle(frame, (x_one, y_one), (x_two, y_two), (255, 255, 255), 2) # 繪製框框
    
            # 計算框的車輛
            if y_one < y_c < y_two and x_one < x_c < x_two :
                if num_id not in track_class_box:
                    # 車輛進入框
                    track_class_box[num_id] = 'in'
                    box_counters[class_id] += 1
            else:
                if num_id in track_class_box and track_class_box[num_id] == 'in':
                    # 車輛離開框
                    box_counters[class_id] -= 1
                    del track_class_box[num_id]  # 字典中删除

            for idx, (key, value) in enumerate(box_counters.items()):
                class_name = class_names[key]
                cnt_str = f"{class_name}: {value}"
                cv2.line(frame, (100, 20 + idx * 40), (300, 20 + idx * 40), [85, 45, 255], 40)
                cv2.putText(frame, cnt_str, (100, 30 + idx * 40), cv2.FONT_HERSHEY_SIMPLEX, 1, [255, 255, 255], thickness=2, lineType=cv2.LINE_AA)
    return frame