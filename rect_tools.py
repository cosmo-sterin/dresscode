"""
MIT License

Copyright (c) 2017 Tristan Cosmo Stérin

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
import numpy as np
import cv2

'''
    Our rectangle notation convention is (x,y,w,h).
    With (x,y) top left corner.
    The following functions are some useful routines to 
    manipulate rectangles.

'''

def get_rect_img(img):
    return (0,0,img.shape[1],img.shape[0])
def get_img_crop(img,crop):
    x,y,w,h = crop
    return img[y:y+h,x:x+w,:]
# center of rect
def get_mil_rect(rect):
    a,b,c,d = rect
    return (int((a+(a+c))/2),int((b+(b+d))/2))
# random sub rect in rect
def get_rand_subrect(rect,size):
    rand_x = np.random.randint(rect[0],rect[0]+rect[2])
    rand_y = np.random.randint(rect[1],rect[1]+rect[3])
    return (rand_x,rand_y,size,size)
# right bottom point
def get_end_point(rect):
    return (rect[0]+rect[2],rect[1]+rect[3])
# quarter plan inequality
def le_pt(a,b):
    return a[0] <= b[0] and a[1] <= b[1]
# is a valid rect
def valid_rect(rect_whole,rect_query):
    return le_pt(rect_whole[:2], rect_query[:2]) and le_pt(get_end_point(rect_query),get_end_point(rect_whole))
#draws a rectangle on an images
def draw_rectangle(img, rect, color=(255,0,0), thick=2):
    cv2.rectangle(img,rect[:2],get_end_point(rect),color,thick)