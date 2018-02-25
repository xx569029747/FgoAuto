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


def screen_shot_and_find_location(src, timeout=2):
    time.sleep(timeout)
    count = 0
    while True:
        c.screenshot(tmp_file)
        time.sleep(2)
        pos = ImageUtils.find_position(tmp_file, img_path + "/" + src)
        count = count + 1
        if pos is not None:
            print '[' + str(count) + ']' + str(pos)
            return pos
        else:
            print '[' + str(count) + ']Not Found'
            if count == 4:
                raise RuntimeError


def tap(x, y, timeout=2):
    time.sleep(timeout)
    s.tap(x, y)
    print 'tap on ' + str(x) + ', ' + str(y)


def fix_location_and_tap(x, y, timeout=2, need_fix=True):
    if need_fix:
        tap(x + 20, y + 60)
    else:
        tap(x, y)
    time.sleep(timeout)


def sleep(timeout):
    time.sleep(timeout)


def login():
    tap(200, 200, 6)
    tap(200, 200, 4)
    tap(200, 200, 4)
    pos = screen_shot_and_find_location('close.png')
    if pos is not None:
        tap(pos[0], pos[1])
    sleep(2)
    # task1
    fix_location_and_tap(342, 853, 1)
    # task2
    fix_location_and_tap(523, 926, 1)
    # task3
    fix_location_and_tap(520, 905, 1)
    # find support 孔明
    pos = screen_shot_and_find_location('support.png')
    if pos is not None:
        tap(pos[0], pos[1])
    sleep(2)
    # start
    fix_location_and_tap(46, 1153, 16)
    # skill1
    fix_location_and_tap(145, 170, 1, False)
    # skill2
    fix_location_and_tap(145, 92, 1, False)
    # attack
    pos = screen_shot_and_find_location('attack.png')
    if pos is not None:
        tap(pos[0], pos[1])
    sleep(2)
    # fix_location_and_tap(180, 65)
    # fix_location_and_tap(493, 401)
    # fix_location_and_tap(240, 368)
    sleep(16)
    c.screenshot(tmp_file)


login()

if __name__ == '__main__':
    unittest.main()
