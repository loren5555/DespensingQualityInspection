import numpy as np

import algorithms as algs
import cv2 as cv


class Runner:
    def __init__(self, args):
        self.args = args

    def generate_width_map(self, imgs):
        # edge detection
        binary_imgs, edged_imgs, all_contours = algs.edgedetection(imgs, self.args)
        # width measurement
        width_map = algs.widthmeasurement(imgs, self.args)
        return binary_imgs, edged_imgs, width_map, all_contours

    def detect_connected_domain(self, imgs, all_contours):
        colored_imgs = []
        for i in range(self.args.imgs_num):
            r = np.copy(imgs[i])
            g = np.copy(imgs[i])
            b = np.copy(imgs[i])
            contours = all_contours[i]
            clen = len(contours)
            for j in range(clen):
                k = j % 6
                cv.fillPoly(r, [contours[k]], self.args.color_lists[k][0])
                cv.fillPoly(g, [contours[k]], self.args.color_lists[k][1])
                cv.fillPoly(b, [contours[k]], self.args.color_lists[k][2])
            colored_img = cv.merge((r, g, b))
            colored_imgs.append(colored_img)
        return colored_imgs
