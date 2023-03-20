import cv2
import numpy as np


# 绘制区域
def mask_foot(frame, foot_box):
    # 左上角坐标
    x_min = foot_box[0][0]
    y_min = foot_box[0][1]
    # 右下角坐标
    x_max = foot_box[1][0]
    y_max = foot_box[1][1]

    # 读取画面尺寸
    frame_shape = frame.shape  #
    x = frame_shape[0]
    y = frame_shape[1]
    frame_ones = np.ones(shape=(x, y), dtype=np.uint8)

    # 画出蒙版之后，将区域画成一个白色的矩形
    cv2.rectangle(frame_ones, foot_box[0], foot_box[1], 255, -1)
    cv2.imshow("frame_ones_mask", frame_ones)
    return frame_ones