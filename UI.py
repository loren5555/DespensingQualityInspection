import sys
import cv2 as cv

from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QFileDialog
from UI import Ui_MainWindow

import common.arguments as args
import common.utils as utils
from runner import Runner


class MyWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.addimgbutton.clicked.connect(self.read_file)
        self.adddirbutton.clicked.connect(self.write_file)
        self.OK.clicked.connect(self.process)
        self.showimg.clicked.connect(self.display_img)

        self.img = None
        self.img2 = None
        self.img_for_display = None

        self.filepath = None
        self.folderpath = None

    def read_file(self):
        filename, filetype = QFileDialog.getOpenFileName(self, "选取文件", r"C:/Users/Loren/Desktop/try/in",
                                                         "所有文件(*);;JPEG(*.jpg);;位图文件(.bmp);;PNG(.png)")
        print(filename, filetype)
        self.picdir.setText(filename)
        self.img = cv.imread(filename)
        self.img_for_display = QtGui.QImage(filename)


    def write_file(self):
        foldername = QFileDialog.getExistingDirectory(self, "选取文件夹", r"C:/Users/Loren/Desktop/try/out")
        print(foldername)
        self.outputdir.setText(foldername)

    def process(self):
        try:
            folderpath = self.outputdir.text()
            # self.img2 = cv.add(self.img, self.img)
            # cv.imwrite(folderpath + r'\output.jpg', self.img2)
            # self.img2 = QtGui.QImage(folderpath + r'\output.jpg')
            # self.img_for_display = self.img2
            arg = args.Args(debug_e=False, debug_w=False, scale=False, fewer_img_num=False)
            arg.init()
            arg.imgs_num = 1
            runner = Runner(arg)
            img_name = self.picdir.text()
            binary_imgs, edged_imgs, width_map, all_contours = runner.generate_width_map([self.img])
            self.colored_imgs = runner.detect_connected_domain(binary_imgs, all_contours)
            cv.imwrite(folderpath + r'\output.jpg', self.colored_imgs[0])
            self.img2 = QtGui.QImage(folderpath + r'\output.jpg')
            self.img_for_display = self.img2
            change_result = r"成功"

        except:
            change_result = r"失败"

        self.label_wait.setText(change_result)

    def display_img(self):
        self.imgviewer.size()
        self.imgviewer.setPixmap(QtGui.QPixmap.fromImage(self.img_for_display))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = MyWindow()
    ui.show()
    sys.exit(app.exec())
