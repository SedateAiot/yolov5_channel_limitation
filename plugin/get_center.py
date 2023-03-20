# 根据xyxy坐标，返回车辆中间的坐标集
def get_centerBox(xyxy):
    left_top_x = xyxy[0].item()
    left_top_y = xyxy[1].item()
    re_bottom_x = xyxy[2].item()
    re_bottom_y = xyxy[3].item()

    w = re_bottom_x - left_top_x  # 宽
    h = re_bottom_y - left_top_y  # 高

    left_center_box_x = int(left_top_x + w / 4)
    left_center_box_y = int(left_top_y + h / 4)

    re_center_box_x = int(re_bottom_x - w / 4)
    re_center_box_y = int(re_bottom_y - h / 4)

    center_box = [[int(left_center_box_x), int(left_center_box_y)], [int(re_center_box_x), int(re_center_box_y)]]
    return center_box