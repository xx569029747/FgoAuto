#!/bin/env python
# encoding:utf-8

import time
import aircv as ac
import cv2


# 查询子图片在截图的位置
def find_position(src, obj):
    time.sleep(1)
    src_img = ac.imread(src)
    obj_img = ac.imread(obj)
    pos = ac.find_template(src_img, obj_img)
    if pos is not None:
        return pos['result']
    else:
        return None


# print circle_center_pos
def draw_circle(pos):
    img_src = ac.imread('../tmp.png')
    cv2.circle(img_src, pos, 50, (0, 255, 0), 5)
    cv2.imshow('objDetect', img_src)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    position = find_position('../tmp.png', '../img/skill1.png')
    # position = (30, 30)
    print position
    draw_circle(position)
