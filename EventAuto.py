#!/bin/env python
# encoding:utf-8
import unittest

from threading import Thread
import wda
import time
import sys
from utils import ImageUtils

# 定义图片存储位置
img_path = 'img'
tmp_file = 'tmp.png'
apple_num = 11

# 启动ios客户端进程
c = wda.Client('http://localhost:8100')
s = c.session('com.bilibili.fatego')


def check_exit(src, limit=4):
    count = 0
    while True:
        c.screenshot(tmp_file)
        time.sleep(1)
        pos = ImageUtils.find_position(tmp_file, img_path + "/" + src)
        count = count + 1
        if pos is not None:
            print '[' + str(count) + ']' + str(pos)
            return pos
        elif count == limit:
            print '[' + str(count) + '] %s Not Found' % src
            return None


def screen_shot_and_find_location(src, timeout=1, ignore=False):
    pos = check_exit(src)
    if pos is not None:
        tap(pos[0], pos[1])
        time.sleep(timeout)
        return pos
    elif ignore:
        return None
    else:
        raise RuntimeError


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


def attack():
    # attack
    fix_location_and_tap_on_right(98, 1123, 0)
    pos = check_exit('bisha1.png', 1)
    if pos is None:
        # role 1
        fix_location_and_tap_on_left(120, 150, 1)
    else:
        tap(pos[0], pos[1], 0)
    pos = check_exit('bisha2.png', 1)
    if pos is None:
        # role 2
        fix_location_and_tap_on_right(160, 700, 0)
    else:
        tap(pos[0], pos[1], 0)
    pos = check_exit('bisha3.png', 1)
    if pos is None:
        # role 3
        fix_location_and_tap_on_left(300, 150, 0)
    else:
        tap(pos[0], pos[1], 0)



def stop():
    tap(42, 200, 4)
    tap(42, 200, 4)
    # tap on 42, 1148
    pos = screen_shot_and_find_location('next.png', 4, True)
    while pos is None:
        tap(42, 200, 4)
        tap(42, 200, 4)
        pos = screen_shot_and_find_location('next.png', 4)


def start_task():
    select_apple()
    # select support
    fix_location_and_tap_on_right(419, 276, 1)
    # start
    fix_location_and_tap_on_right(46, 1153, 2)
    # click no use item
    # screen_shot_and_find_location('use_items_no.png')
    while True:
        try:
            pos = check_exit('attack.png', 10)
            tap(42, 200)
            if pos is None:
                pos = check_exit('attack.png', 10)
                tap(42, 200)
            if pos is None:
                pos = check_exit('attack.png', 5)
                if pos is None:
                    stop()
                    break
            attack()
        except RuntimeError, e:
            stop()
            break


def select_apple():
    # select apple
    pos = screen_shot_and_find_location('golden_apple.png', 1, True)
    if pos is not None:
        # enter
        screen_shot_and_find_location('apple_enter.png', 1)
        # click task3 one more time
        fix_location_and_tap_on_right(520, 905, 1)
        global apple_num
        apple_num = apple_num - 1
        if apple_num == 0:
            sys.exit()


def begin():
    tap(200, 200, 6)
    tap(200, 200, 3)
    tap(200, 200, 3)
    screen_shot_and_find_location('close.png', 2, True)
    # close friend warning
    fix_location_and_tap_on_left(180, 150, 1)
    # task1
    fix_location_and_tap_on_right(350, 853, 1)
    count = 0
    while True:
        if count != 0:
            sleep(3)
            # close friend warning
            fix_location_and_tap_on_left(180, 150, 1)
        # task2
        fix_location_and_tap_on_right(523, 926, 1)
        count = count + 1
        start_task()
        print 'end ' + str(count) + ' times'
        sleep(28)


begin()

if __name__ == '__main__':
    unittest.main()
