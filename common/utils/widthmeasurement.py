import cv2
import scipy.ndimage.morphology as morph
import numpy as np
from skimage import morphology


import algorithms as algs
import common.arguments as args


from skimage.feature import hessian_matrix, hessian_matrix_eigvals
# def detect_ridges(gray, sigma=3.0):
#     hxx = hessian_matrix(gray, sigma)
#     i1, i2 = hessian_matrix_eigvals(hxx)
#     return i1, i2
#
#
# def mat2gray(img, minRange=0, maxRange=255):
#     if len(img.shape) == 3:
#         img = np.mean(img, axis=2)
#         # Convert matrix to grayscale with the defined range
#     minImg = np.min(img)
#     maxImg = np.max(img)
#     return (img - minImg) * (maxRange - minRange) / (maxImg - minImg) + minRange


if __name__ == "__main__":
    img_path = r"C:\Users\Loren\Documents\Workzone\PycharmProjects\DespensingQualityInspection\results\imgs_removed_holes\Image__2021-06-02__11-07-54.bmp"
    # img_path = r"C:\Users\Loren\Documents\Workzone\PycharmProjects\DespensingQualityInspection\results\imgs_enhanced\Image__2021-06-02__11-02-12.bmp"

    img = cv2.imread(img_path, 0).astype(np.float64)
    img0 = cv2.imread(img_path, 0)
    img = img/255
    M, N = img.shape
    bwPadding = np.zeros(shape=(M + 10, N + 10))
    for i in range(5, 5 + M):
        for j in range(5, 5 + N):
            bwPadding[i, j] = img[i - 5, j - 5]

    D = morph.distance_transform_edt(bwPadding)
    cv2.imshow("1", D)
    cv2.waitKey(0)
    # D = bwPadding

    # D = cv2.GaussianBlur(D, (3, 3), sigmaX=10, sigmaY=10)
    # # D = cv2.normalize(D, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)
    # E, F = detect_ridges(D)
    # E = cv2.normalize(E, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)
    # F = cv2.normalize(F, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)
    # # cv2.imshow("IDX1", F.astype(np.uint8))
    # G = np.copy(F)
    # idx = np.where(F < 50)
    # l = len(idx[0])
    # for i in range(l):
    #     G[idx[0][i], idx[1][i]] = 255
    # cv2.threshold(G, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU, G)


    # h, w = D.shape[:2]
    E = cv2.Laplacian(D, -1, None, 3, None, 0)
    F = cv2.normalize(E, None, 0, 255, cv2.NORM_MINMAX)
    G = np.zeros_like(F)
    idx = np.where(F < 100)
    l = len(idx[0])
    for i in range(l):
        G[idx[0][i], idx[1][i]] = 255
    # cv2.threshold(G, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU, G)
    kernal = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    # G = cv2.morphologyEx(G, cv2.MORPH_OPEN, kernal, iterations=1)
    # H = cv2.Sobel(D, -1, 0, 1, None, 5, delta=127)
    # H = cv2.normalize(H, None, 0, 255, cv2.NORM_MINMAX)
    # I = cv2.Sobel(H, -1, 0, 1, None, 5, delta=0)
    # cv2.imshow(img_path, D)
    cv2.imshow("D", D.astype(np.uint8))
    cv2.imshow("E", E.astype(np.uint8))
    cv2.imshow("F", F.astype(np.uint8))
    cv2.imshow("G", G.astype(np.uint8))
    # cv2.imshow("H", H.astype(np.uint8))
    # cv2.imshow("I", I.astype(np.uint8))
    cv2.waitKey(0)
    cv2.destroyAllWindows()
