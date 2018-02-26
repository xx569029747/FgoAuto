#!/bin/env python
# encoding:utf-8
import unittest

import wda
import time
from utils import ImageUtils

# 定义图片存储位置
img_path = 'img'
tmp_file = 'tmp.png'

# 启动ios客户端进程
c = wda.Client('http://localhost:8100')
s = c.session('com.bilibili.fatego')


def screen_shot_and_find_location(src, timeout=2, ignore=False):
    time.sleep(timeout)
    count = 0
    while True:
        c.screenshot(tmp_file)
        time.sleep(1)
        pos = ImageUtils.find_position(tmp_file, img_path + "/" + src)
        count = count + 1
        if pos is not None:
            print '[' + str(count) + ']' + str(pos)
            tap(pos[0], pos[1])
            time.sleep(2)
            return pos
        else:
            print '[' + str(count) + ']Not Found'
            if count == 4:
                if not ignore:
                    raise RuntimeError
                else:
                    return None


def tap(x, y, timeout=2):
    if timeout != 0:
        time.sleep(timeout)
    s.tap(x, y)
    print 'tap on ' + str(x) + ', ' + str(y)


def fix_location_and_tap_on_right(x, y, timeout=2):
    if timeout != 0:
        time.sleep(timeout)
    tap(x + 20, y + 60)


def fix_location_and_tap_on_left(x, y, timeout=2):
    if timeout != 0:
        time.sleep(timeout)
    tap(x - 60, y + 150)


def sleep(timeout):
    time.sleep(timeout)


def kong_ming_skill():
    # skill1 - 孔明(鉴识眼)
    fix_location_and_tap_on_right(160, 700, 0)
    # select 伯爵
    fix_location_and_tap_on_right(400, 300, 0)
    # skill2 - 孔明(忠言)
    fix_location_and_tap_on_right(160, 770, 0)
    # skill3 - 孔明(指挥)
    fix_location_and_tap_on_right(160, 840, 0)


def edmund_skill():
    # skill1 - 伯爵
    fix_location_and_tap_on_left(90, 150, 0)
    # skill2 - 伯爵
    fix_location_and_tap_on_left(160, 150, 0)


def attack(count):
    # attack
    screen_shot_and_find_location('attack.png')
    # role 1
    fix_location_and_tap_on_left(120, 150, 0)
    if count == 1:
        # Strokes 1
        fix_location_and_tap_on_right(500, 400, 0)
    elif count == 2:
        # Strokes 1
        fix_location_and_tap_on_right(500, 550, 0)
    elif count == 3:
        # Strokes 2
        fix_location_and_tap_on_right(500, 400, 0)
    # role 2
    fix_location_and_tap_on_left(300, 150, 0)


def replace_kong_ming():
    screen_shot_and_find_location('master_skill.png')
    # replace skill
    fix_location_and_tap_on_right(400, 1050, 0)
    # 孔明1
    fix_location_and_tap_on_right(400, 560, 0)
    # 孔明2
    fix_location_and_tap_on_right(400, 760, 0)
    # replace
    fix_location_and_tap_on_right(100, 660, 0)


def login():
    tap(200, 200, 6)
    tap(200, 200, 3)
    tap(200, 200, 3)
    screen_shot_and_find_location('close.png', 2, True)
    # task1
    fix_location_and_tap_on_right(342, 853, 1)
    # task2
    fix_location_and_tap_on_right(523, 926, 1)
    # task3
    fix_location_and_tap_on_right(520, 905, 1)
    # find support 孔明
    screen_shot_and_find_location('support.png', 1)
    # start
    fix_location_and_tap_on_right(46, 1153, 1)
    sleep(16)
    edmund_skill()
    attack(1)
    sleep(24)
    kong_ming_skill()
    replace_kong_ming()
    sleep(3)
    kong_ming_skill()
    attack(2)
    sleep(22)
    attack(3)
    sleep(26)
    tap(200, 200, 4)
    tap(200, 200, 4)
    screen_shot_and_find_location('next.png', 4)


login()

if __name__ == '__main__':
    unittest.main()
