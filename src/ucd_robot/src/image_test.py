#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import numpy as np
import cv2
from matplotlib import pyplot as plt
import matplotlib
import glob


filename = os.path.realpath('images.npy')
print(filename)
filename = "/home/rob/UCD_robot_ws_v2/src/ucd_robot/images/images_data/images.npy"
print(filename)
img_array = np.array(np.load(filename, allow_pickle=True)).item(0)['images']

print(img_array.values())

for i in img_array.values():
    plt.imshow(i,cmap='gray')
    plt.show()
