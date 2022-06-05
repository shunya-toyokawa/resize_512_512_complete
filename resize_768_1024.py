import numpy as np
import cv2

def resize(src_file, dst_file, width, height):
    src_img = cv2.imread(src_file)
    h, w, c = src_img.shape

    # アス比固定, padding
    scale_w = width / w
    scale_h = height / h

    ret_scale = 1.0
    # Down Convert
    if(scale_w < 1.0 or scale_h < 1.0):
        if(scale_w < scale_h): 
            resize_img = cv2.resize(src_img, dsize=None, fx=scale_w, fy=scale_w, interpolation = cv2.INTER_AREA)
            ret_scale = scale_w
        else:
            resize_img = cv2.resize(src_img, dsize=None, fx=scale_h, fy=scale_h, interpolation = cv2.INTER_AREA)
            ret_scale = scale_h
    else:
        resize_img = src_img

    # dst_img 生成
    dst_img = np.zeros((height, width, 3), dtype = np.uint8)

    # dst_imgにresize_imgを合成
    top = 0
    left = 0
    #dst_img[top:height + top, left:width + left] = resize_img
    h, w, c = resize_img.shape
    dst_img[0:h, 0:w] = resize_img

    cv2.imwrite(dst_file, dst_img)

    return  ret_scale
resize("./out_crop.png","results_resize_768_1024/out_768_1024.jpg",512,512)

