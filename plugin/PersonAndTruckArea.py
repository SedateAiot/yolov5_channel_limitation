# 此插件用来绘制人和卡车的活动区域，并生成两个蒙版，用于与目标框进行与操作
import cv2
import numpy as np

# pts_person = [[383, 107], [325, 114], [371, 182], [450, 173]]

pts_person = [[159, 78], [228, 69], [431, 568], [200, 569]]
pts_truck = [[355, 78], [262, 87], [532, 573], [697, 420]]


def draw_warning(frame):
    global pts_person, pts_truck

    # 1. 基于原始图片的大小，制作两个蒙版图片，用来绘制不同的告警区域
    frame_shape = frame.shape  # (576, 704, 3)
    # print("frame_shape: ", frame_shape)
    x = frame_shape[0]
    y = frame_shape[1]
    frame_ones_person = np.ones(shape=(x, y), dtype=np.uint8)
    frame_ones_truck = frame_ones_person.copy()

    # 2. 绘制人的禁区
    pts_person = np.array(pts_person, np.int32)
    cv2.polylines(frame_ones_person, [pts_person], True, 255)
    cv2.fillPoly(frame_ones_person, [pts_person], (255, 255, 255))

    # 绘制卡车的禁区
    pts_truck = np.array(pts_truck, np.int32)
    cv2.polylines(frame_ones_truck, [pts_truck], True, 255)
    cv2.fillPoly(frame_ones_truck, [pts_truck], (255, 255, 255))

    # 在原图绘制区域边界
    cv2.polylines(frame, [pts_person], True, (0, 0, 255))
    cv2.polylines(frame, [pts_truck], True, (0, 0, 255))

    return frame_ones_person, frame_ones_truck


