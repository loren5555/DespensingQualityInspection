import numpy as np

import common.utils as utils


def edgedetection(imgs, args):
    """检测胶路边缘"""
    # 提取蓝色
    utils.blend_imgs(imgs, args)
    # 图像平滑
    utils.smooth_imgs(imgs, args)
    # 图像增强
    utils.enhance_imgs(imgs, args)
    # 图像分割
    utils.threshold_img(imgs, args)
    # 形态学处理
    utils.morphology_handle(imgs, args)
    # 去除小的区域
    binary_imgs, all_contours = utils.remove_small_objects(imgs, args)
    # 边缘检测
    imgs_cpy = np.copy(imgs)
    edged_imgs = utils.edge_img(imgs_cpy, args)
    print("Edge detection complete")
    return binary_imgs, edged_imgs, all_contours
