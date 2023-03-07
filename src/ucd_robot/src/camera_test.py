#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 11:42:50 2023
@author: qiang
"""

import cv2
import os
import time

capture = cv2.VideoCapture(6)
capture.set(3, 640)
capture.set(4, 480)
#%%
capture.set(cv2.CAP_PROP_FPS, 30)
#%%
fps = capture.get(cv2.CAP_PROP_FPS)
ret, frame = capture.read()
frame = cv2.flip(frame, 1)
#%%
while(True):
    t1 = time.time()
    fps = capture.get(cv2.CAP_PROP_FPS)
    # print(fps)
    ret, frame = capture.read()#摄像头读取,ret为是否成功打开摄像头,true,false。 frame为视频的每一帧图像
    # frame = cv2.flip(frame, 1)#摄像头是和人对立的，将图像左右调换回来正常显示。
    print('made it ')
    cv2.imshow("video", frame)
    c = cv2.waitKey(50)
    print(time.time()-t1)
    if c == 27:
        break