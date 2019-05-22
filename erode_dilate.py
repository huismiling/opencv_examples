#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: xiao
# Created Time : 2019-05-22
# File Name: erode_dilate.py
# Description:
"""

import cv2
import numpy as np 



if __name__=='__main__':
    imgfn = 'test.jpg'
    img = cv2.imread(imgfn)
    for k in range(3,8):
        kernel = np.ones((k,k),np.uint8)  
        erosion = cv2.erode(img,kernel,iterations = 1)
        dilation = cv2.dilate(img,kernel,iterations = 1)
        closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
        opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
        new_img = np.vstack([erosion, dilation, closing, opening])
        cv2.imshow('newimg_k_{}'.format(k), new_img)
        cv2.waitKey()
