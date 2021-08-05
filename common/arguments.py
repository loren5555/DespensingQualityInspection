import os
import common.utils as utils


class Args:
    def __init__(self, debug_e=False, debug_w=False, scale=False, fewer_img_num=False):
        self.debug_edgedetection = debug_e
        self.debug_widthmeasruement = debug_w
        self.scale_imgs = scale
        self.fewer_img_num = fewer_img_num

        self.imgs_num = 0
        self.img_names = []
        # self.imgs = []

        self.source_dir = "res\\imgs"
        self.result_dir = "results\\results\\output"
        self.binary_dir = "results\\results\\binary"
        self.edged_dir = "results\\results\\edge"
        self.blend_dir = "results\\imgs_blended"
        self.scaled_dir = "results\\imgs_scaled"
        self.enhance_dir = "results\\imgs_enhanced"
        self.smooth_dir = "results\\imgs_smoothed"
        self.threshold_dir = "results\\imgs_threshold"
        self.morphology_dir = "results\\imgs_morphology"
        self.edge_dir = "results\\imgs_edged"
        self.removeholes_dir = "results\\imgs_removed_holes"
        self.widthmeasure_dir = "results\\imgs_widthmap"
        self.colored_dir = "results\\results\\colored_imgs"

        self.measure_dir = "results\\imgs_measured"

        self.color_lists = [(100, 0, 0), (0, 100, 0), (0, 0, 100), (100, 100, 0), (0, 100, 100), (100, 0, 100)]

    def init(self):
        """删除就有目录并新建需要的目录"""
        utils.clear_folder(self)

        if self.debug_edgedetection or self.debug_widthmeasruement:
            for attr in dir(self):
                if attr[-4:] == "_dir":
                    if not os.path.exists(getattr(self, attr)):
                        os.makedirs(getattr(self, attr))

        if not os.path.exists(self.result_dir):
            os.makedirs(self.result_dir)

        print("Arguments inited")
