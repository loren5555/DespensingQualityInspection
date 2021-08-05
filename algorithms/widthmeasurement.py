import numpy as np

import common.utils as utils
import cv2


def widthmeasurement(imgs, args):
    """测量胶路宽度"""
    # 进行距离变换
    dist = utils.distance_transform(imgs, args)

    # 进行骨架提取
    utils.imgs_thinning(imgs, args)

    # 加入距离信息
    dist_map = utils.imgs_add_distance(imgs, dist, args)
    # utils.show(dist_map[1])

    print("Width measurement tobe completed")
    return np.copy(dist_map)
