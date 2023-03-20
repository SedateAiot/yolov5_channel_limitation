# 本插件用来将目标框选单位和蒙版进行与操作，并返回结果
import cv2


# 将两个区域进行与操作
def area_merge(frame_1, frame_2):
    dst = cv2.bitwise_and(src1=frame_1, src2=frame_2)

    cv2.imshow("dst", dst)
    # 与操作之后，图像没有重叠的话，就全黑
    # 有重叠的话，就有部分是白色
    # 用均值的判断方式判断
    # mean => (1.0, 0.0, 0.0, 0.0)
    mean = cv2.mean(dst)[0]

    if mean <= 1: # 说明区域内没有人在
        print("mean: ", mean)
        return False
    else:
        print("mean: ", mean)
        return True