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


def screen_shot_and_find_location(src, timeout=1, ignore=False):
    count = 0
    while True:
        c.screenshot(tmp_file)
        time.sleep(2)
        pos = ImageUtils.find_position(tmp_file, img_path + "/" + src)
        count = count + 1
        if pos is not None:
            print '[' + str(count) + ']' + str(pos)
            tap(pos[0], pos[1])
            time.sleep(timeout)
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
    tap(x + 20, y + 60, timeout)


def fix_location_and_tap_on_left(x, y, timeout=2):
    tap(x - 60, y + 150, timeout)


def sleep(timeout):
    time.sleep(timeout)


def mei_lin_skill():
    # skill1 - 梅林(梦幻魅力)
    fix_location_and_tap_on_right(160, 700, 2)
    # skill2 - 梅林(幻术)
    fix_location_and_tap_on_right(160, 770, 2)


def kong_ming_skill():
    # skill1 - 孔明(鉴识眼)
    fix_location_and_tap_on_right(160, 700, 1)
    # select 伯爵
    fix_location_and_tap_on_right(400, 300, 1)
    # skill2 - 孔明(忠言)
    fix_location_and_tap_on_right(160, 770, 2)
    # skill3 - 孔明(指挥)
    fix_location_and_tap_on_right(160, 840, 2)


def edmund_skill():
    # skill1 - 伯爵
    fix_location_and_tap_on_left(90, 150, 2)
    # skill2 - 伯爵
    fix_location_and_tap_on_left(160, 150, 2)


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


def start_task():
    # task3
    fix_location_and_tap_on_right(520, 905, 1)
    select_apple()
    # select support
    fix_location_and_tap_on_right(419, 276, 1)
    # start
    fix_location_and_tap_on_right(46, 1153, 1)
    sleep(16)
    edmund_skill()
    attack(1)
    sleep(28)
    mei_lin_skill()
    replace_kong_ming()
    sleep(3)
    kong_ming_skill()
    attack(2)
    sleep(26)
    attack(3)
    sleep(28)
    tap(200, 200, 4)
    tap(200, 200, 4)
    # tap on 42, 1148
    pos = screen_shot_and_find_location('next.png', 4, True)
    if pos is None:
        tap(42, 200, 4)
        tap(42, 200, 4)
        screen_shot_and_find_location('next.png', 4)


def select_apple():
    # select apple
    pos = screen_shot_and_find_location('golden_apple.png', 2, True)
    if pos is not None:
        # enter
        screen_shot_and_find_location('apple_enter.png', 2)
        # click task3 one more time
        fix_location_and_tap_on_right(520, 905, 1)


def begin():
    tap(200, 200, 6)
    tap(200, 200, 3)
    tap(200, 200, 3)
    screen_shot_and_find_location('close.png', 2, True)
    # close friend warning
    fix_location_and_tap_on_left(180, 150, 1)
    # task1
    fix_location_and_tap_on_right(342, 853, 1)
    # task2
    fix_location_and_tap_on_right(523, 926, 1)
    count = 1
    while True:
        if count != 1:
            sleep(3)
            # close friend warning
            fix_location_and_tap_on_left(180, 150, 1)
        count = count + 1
        start_task()
        print 'end ' + str(count) + ' times'


begin()

if __name__ == '__main__':
    unittest.main()
