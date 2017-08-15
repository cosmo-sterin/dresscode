import numpy as np

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
