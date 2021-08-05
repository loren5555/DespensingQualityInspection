import numpy as np

import common.arguments as args
import common.utils as utils
from runner import  Runner
# import algorithms as algs

# 定义参数
args = args.Args(debug_e=True, debug_w=False, scale=False, fewer_img_num=False)
# 初始化目录
args.init()

runner = Runner(args)
# read imgs from folder
imgs, img_names = utils.get_imgs(args)

binary_imgs, edged_imgs, width_map, all_contours = runner.generate_width_map(imgs)
colored_imgs = runner.detect_connected_domain(binary_imgs, all_contours)

# 保存结果
utils.save_imgs(width_map, args, args.result_dir)
utils.save_imgs(binary_imgs, args, args.binary_dir)
utils.save_imgs(edged_imgs, args, args.edged_dir)
utils.save_imgs(colored_imgs, args, args.colored_dir)
print("The program exits normally")
