#!/bin/env python
# encoding:utf-8

from PIL import Image, ImageFilter
import time
import aircv as ac


def gray(src):
    image = Image.open(src)
    image = image.convert('L')
    image = image.filter(ImageFilter.SHARPEN)
    image.save(src)


def gray1(src):
    image = Image.open(src)
    image = image.convert('1')
    image.save(src + '.png')


# 查询子图片在截图的位置
def find_position(src, obj):
    gray(src)
    time.sleep(1)
    src_img = ac.imread(src)
    obj_img = ac.imread(obj)
    pos = ac.find_template(src_img, obj_img)
    if pos is not None:
        return pos['result']
    else:
        return None


# gray1("/Users/blue/Downloads/tmp.png")
