import cv2
import os
from collections import OrderedDict

def get_images_by_id(image_folder,id_getter,file_selecter,to_ignore_file=""):
    '''
        Returns a dictionary of images name in image_folder.
        image_folder: where to find the images.
        id_getter: how to extract an id from an img name.
        file_selecter: which file to select at first in image_folder.
        to_ignore_file: file which ids we want to ignore (ill-formated files etc...).
    '''
    
    to_ignore = []
    if to_ignore_file != "":
        f = open(to_ignore_file,"r")
        raw_s = f.read()
        f.close()
        to_ignore = list(map(int,filter(lambda x: x != '',raw_s.split(','))))
        print("`"+image_folder+"` id ignored:", to_ignore)
    
    all_jpg = [image_folder+f for f in os.listdir(image_folder) if  file_selecter(f)]
    all_jpg.sort(key=id_getter)
    to_return = OrderedDict()
    for image_path in all_jpg:
        image_id = id_getter(image_path)
        if not image_id in to_ignore:
            to_return[image_id] = image_path
    return to_return

'''
    Getter and selecter for our catalogue and our queries.
'''
# We have multiple snapshots per item in the catalogue
# we want to select the _0 ones also we look only at jpgs
def id_select_cat(image_path):
    if not 'jpg' in image_path:
        return False
    sub_id = int(image_path.split('_')[-1].split('.')[0])
    return sub_id == 0
def id_getter_cat(image_path):
    return int(image_path.split('/')[-1].split('_')[0])
def id_select_quer(image_path):
    if not 'jpg' in image_path:
        return False
    return True
def id_getter_quer(image_path):
    return int(image_path.split('/')[-1].split('.')[0])

'''
    Routines for opening images.
'''
# get numpy HxWx3 image in RGB
def img_getter(image_path):
    print("opening", image_path)
    img = cv2.imread(image_path)
    return cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
def img_getter_gray(image_path):
    img = img_getter(image_path)
    return cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

'''
    Linking classes to ids and ids to classes.
'''
def get_id_class_correspondance(imgs_by_id):
    class_of_id = {}
    for i,k in enumerate(imgs_by_id.keys()):
        class_of_id[k] = i
    id_of_class = {}
    for i,k in enumerate(imgs_by_id.keys()):
        id_of_class[i] = k
    return class_of_id,id_of_class