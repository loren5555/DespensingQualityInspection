import cv2


global point1, point2
global img


def on_mouse(event, x, y, flags, param):
    global point1, point2, img
    img = param
    img2 = img.copy()
    if event == cv2.EVENT_LBUTTONDOWN:
        point1 = (x, y)
        cv2.circle(img2, point1, 10, (0, 255, 0), 5)
        cv2.imshow("image", img2)
    elif event == cv2.EVENT_MOUSEMOVE and (flags & cv2.EVENT_FLAG_LBUTTON):
        cv2.rectangle(img2, point1, (x, y), (255, 0, 0), 5)
        cv2.imshow("image", img2)
    elif event == cv2.EVENT_LBUTTONUP:
        point2 = (x, y)
        cv2.rectangle(img2, point1, point2, (0, 0, 255), 5)
        cv2.imshow("image", img2)
        min_x = min(point1[0], point2[0])
        min_y = min(point1[1], point2[1])
        width = abs(point1[0] - point2[0])
        height = abs(point1[1] - point2[1])
        cut_img = img[min_y:min_y+height, min_x:min_x+width]
        img = img2.copy()
        cv2.imwrite("roi.jpg", cut_img)


def main():
    global img
    img = cv2.imread(r"C:\Users\Loren\Desktop\try\in\1.jpg")
    cv2.namedWindow("image")
    cv2.setMouseCallback("image", on_mouse, img)
    cv2.imshow("image", img)
    cv2.waitKey(0)
    img_cutted = cv2.imread("roi.jpg")
    cv2.imshow("cutted_img", img_cutted)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    print(point2)


if __name__ == "__main__":
    main()
