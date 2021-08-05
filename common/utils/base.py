import cv2 as cv
import os
import shutil

import numpy as np


def cv_imread(file_path):
    cv_img = cv.imdecode(np.fromfile(file_path, dtype=np.uint8), cv.IMREAD_COLOR)
    return cv_img


def get_imgs(args):
    """读取文件夹中的图片"""
    args.img_names = os.listdir(args.source_dir)
    args.imgs_num = len(args.img_names)
    if args.fewer_img_num:
        args.imgs_num = 2
    imgs = [0] * args.imgs_num
    for i in range(0, args.imgs_num):
        imgs[i] = cv_imread(os.path.join(args.source_dir, args.img_names[i]))
    # for debug， view more imgs in one screen
    if args.scale_imgs:
        scale_imgs(imgs, args)
        print("Images are scaled")
    print("Images loaded from %s" % args.source_dir)
    return imgs, args.img_names


def save_imgs(imgs, args, save_dir):
    """保存图像"""
    for i in range(args.imgs_num):
        save_path = os.path.join(save_dir, args.img_names[i])
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)
        cv.imwrite(save_path, imgs[i])


def scale_imgs(imgs, args):
    """缩放文件夹中图片"""
    for i in range(0, args.imgs_num):
        imgs[i] = cv.resize(imgs[i], None, fx=0.25, fy=0.25, interpolation=cv.INTER_AREA)
    if args.debug_edgedetection:
        save_imgs(imgs, args, args.scaled_dir)


def clear_folder(args):
    """删除旧有结果"""
    paths = []
    for attr in dir(args):
        if attr[-4:] == "_dir" and attr != "source_dir":
            paths.append(getattr(args, attr))
    for path in paths:
        if os.path.exists(path):
            shutil.rmtree(path)
    print("folder cleared")


def show(img, name="show window"):
    cv.imshow(name, img.astype(np.uint8))
    cv.waitKey(0)
    cv.destroyAllWindows()
