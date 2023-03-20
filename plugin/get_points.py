import cv2
import numpy as np

pts = []


# 用鼠标获取点坐标，并加入数组
def onmouse_draw_rect(event, x, y, flags, draw_rects):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x, y)
        pts.append([x, y])


    if event == cv2.EVENT_LBUTTONUP:
        cv2.circle(frame, (x, y), 1, (0, 0, 255), 2)


# 判断pts是否为空
# pts=[[86, 422], [387, 224], [623, 416], [559, 571], [144, 573]]
cap = cv2.VideoCapture("rtsp://admin:yyit86536280@192.168.1.111/cam/realmonitor?channel=1&subtype=1")
# 循环取视频内容
# 调用鼠标参数选择区域
while True:
    if not pts:  # 如果pts里是空的，就读取视频第一帧，等待用户交互
        # 读取视频流的第一帧，并等待
        ret, frame = cap.read()
        cv2.namedWindow("frame")
        cv2.setMouseCallback("frame", onmouse_draw_rect)
        cv2.imshow("frame", frame)
        # 开始利用鼠标进行回调
        c = cv2.waitKey(0)
        # 获取完点坐标后保存到数组
        if c == ord("q"):
            cv2.destroyAllWindows()
    else:  # 存在就开始绘制，绘制需要无限循环
        pts_array = np.array(pts, np.int32)

        ret, frame = cap.read()
        cv2.polylines(frame, [pts_array], True, (0, 0, 255), 2)
        cv2.imshow("frame", frame)

        # 将选中的区域变成ROI区域 选中区域为白色，非选中为黑色
        frame_copy = frame.copy()
        frame_copy = cv2.fillPoly(frame_copy, [np.array(pts)], (255, 255, 255))
        cv2.imshow("frame_copy", frame_copy)

        ret, thresh1 = cv2.threshold(frame_copy, 1, 255, cv2.THRESH_BINARY)

        cv2.imshow("thresh1", thresh1)
        cv2.waitKey(0)
        break
        # c = cv2.waitKey(1)
        # if c == ord('q'):
        #     break
cap.release()
cv2.destroyAllWindows()

