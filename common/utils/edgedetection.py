from .base import *


def blend_imgs(imgs, args):
    """图像灰度化"""
    for i in range(args.imgs_num):
        b, g, r = cv.split(imgs[i])
        blend = cv.subtract(b, cv.addWeighted(g, 0.5, r, 0.5, 0))
        imgs[i] = cv.add(blend, blend)
    if args.debug_edgedetection:
        save_imgs(imgs, args, args.blend_dir)
        print("Imgs blended")


def smooth_imgs(imgs, args):
    """图像平滑"""
    # guid = imgs[:]
    for i in range(0, args.imgs_num):
        # cv.GaussianBlur(imgs[i], (21, 21), 2, imgs[i])    # 高斯平滑
        # cv.blur(imgs[i], (9, 9), imgs[i])   # 均值平滑
        # cv.medianBlur(imgs[i], 11, imgs[i])  # 中值平滑
        imgs[i] = cv.bilateralFilter(imgs[i], 9, 75, 75)  # 双边滤波
        # cv.ximgproc.guidedFilter(imgs[i], imgs[i], 30, 50, imgs[i])    # 导向滤波
    if args.debug_edgedetection:
        save_imgs(imgs, args, args.smooth_dir)
        print("Images smoothed")


def enhance_imgs(imgs, args):
    """图像增强"""
    for i in range(args.imgs_num):
        cv.normalize(imgs[i], imgs[i], 255, 0, cv.NORM_INF)
    if args.debug_edgedetection:
        save_imgs(imgs, args, args.enhance_dir)
        print("Images enhanced")


def morphology_handle(imgs, args):
    """形态学处理"""
    for i in range(args.imgs_num):
        kernal = cv.getStructuringElement(cv.MORPH_RECT, (5, 5))
        # imgs[i] = cv.morphologyEx(imgs[i], cv.MORPH_GRADIENT, kernal, iterations=1)
        imgs[i] = cv.morphologyEx(imgs[i], cv.MORPH_CLOSE, kernal, iterations=1)
        imgs[i] = cv.morphologyEx(imgs[i], cv.MORPH_OPEN, kernal, iterations=1)
    if args.debug_edgedetection:
        save_imgs(imgs, args, args.morphology_dir)
        print("Morphological processed")


def threshold_img(imgs, args):
    """二值化"""
    ret = np.zeros_like(range(args.imgs_num))
    for i in range(args.imgs_num):
        # cv.adaptiveThreshold(imgs[i], 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 1001, 0, imgs[i])
        # cv.threshold(imgs[i], 50, 255, cv.THRESH_BINARY, imgs[i])
        ret[i], _ = cv.threshold(imgs[i], 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU, imgs[i])

    if args.debug_edgedetection:
        # print("Otsu rets: ", ret)
        save_imgs(imgs, args, args.threshold_dir)
        print("Images segmented")


def remove_small_objects(imgs, args, threshold = 10000):
    """去除小的区域"""
    # TODO: 此处应设置可变阈值 但还未想好如何设置
    all_contours = []
    for i in range(args.imgs_num):
        cv_contours = []
        contours, _ = cv.findContours(imgs[i], cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
        for contour in contours:
            area = cv.contourArea(contour)
            if area <= threshold:
                cv_contours.append(contour)
        cv.fillPoly(imgs[i], cv_contours, (255, 255, 255))

        cv_contours = []
        contours, _ = cv.findContours(imgs[i], cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
        for contour in contours:
            area = cv.contourArea(contour)
            if area <= threshold:
                cv_contours.append(contour)
        cv.fillPoly(imgs[i], cv_contours, (0, 0, 0))

        contours, _ = cv.findContours(imgs[i], cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
        all_contours.append(contours)

    if args.debug_edgedetection:
        save_imgs(imgs, args, args.removeholes_dir)
        print("Small objects removed")
    return np.copy(imgs), all_contours


def edge_img(imgs, args):
    for i in range(args.imgs_num):
        # cv.Sobel(imgs[i], -1, 1, 1, imgs[i], 3)
        # scharr_edge_x = cv.Scharr(imgs[i], ddepth=cv.CV_32F, dx=1, dy=0)
        # scharr_edge_x = cv.convertScaleAbs(scharr_edge_x)
        # scharr_edge_y = cv.Scharr(imgs[i], ddepth=cv.CV_32F, dx=0, dy=1)
        # scharr_edge_y = cv.convertScaleAbs(scharr_edge_y)
        # cv.addWeighted(scharr_edge_x, 0.5, scharr_edge_y, 0.5, 0, imgs[i])  # 两者等权叠加
        # imgs[i] = cv.Canny(imgs[i], threshold1=180, threshold2=230)
        cv.Laplacian(imgs[i], -1, imgs[i])
        cv.GaussianBlur(imgs[i], (3, 3), 1, imgs[i])
    if args.debug_edgedetection:
        save_imgs(imgs, args, args.edge_dir)
        print("Image edged")
    return np.copy(imgs)
