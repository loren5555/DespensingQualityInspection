import cv2
import scipy.ndimage.morphology as morph
from skimage.feature import hessian_matrix, hessian_matrix_eigvals

from .base import *
from .edgedetection import remove_small_objects


def detect_ridges(gray, sigma=3.0):
    hxx = hessian_matrix(gray, sigma)
    i1, i2 = hessian_matrix_eigvals(hxx)
    return i1, i2


def mat2gray(img, minRange=0, maxRange=255):
    if len(img.shape) == 3:
        img = np.mean(img, axis=2)
        # Convert matrix to grayscale with the defined range
    minImg = np.min(img)
    maxImg = np.max(img)
    return (img - minImg) * (maxRange - minRange) / (maxImg - minImg) + minRange


def distance_transform(imgs, args):
    """图像宽度变换"""
    for i in range(args.imgs_num):
        h, w = imgs[i].shape
        img_padding = np.zeros((h + 10, w + 10))
        for j in range(5, 5 + h):
            for k in range(5, 5 + w):
                img_padding[j, k] = imgs[i][j - 5, k - 5]
        imgs[i] = morph.distance_transform_edt(img_padding)
    return imgs[:]


def imgs_thinning(imgs, args):
    for i in range(args.imgs_num):
        imgs[i] = cv2.Laplacian(imgs[i], -1, None, 3, None, 0)
        imgs[i] = cv2.normalize(imgs[i], None, 0, 255, cv2.NORM_MINMAX)
        idx = np.where(imgs[i] < 100)
        imgs[i] = np.zeros_like(imgs[i])
        l = len(idx[0])
        for j in range(l):
            imgs[i][idx[0][j], idx[1][j]] = 255
        imgs[i] = imgs[i].astype(np.uint8)
    remove_small_objects(imgs, args, threshold=100)


def imgs_add_distance(imgs, dist, args):
    dist_map = imgs[:]
    for i in range(args.imgs_num):
        dist_map[i] = cv2.add(dist[i], np.zeros_like(imgs[i], dtype=np.float64), mask=imgs[i])
    if args.debug_widthmeasruement:
        save_imgs(dist_map, args, args.widthmeasure_dir)
        print("distance measured")
    return dist_map
