from utils import *

# choose model
model_name = "FCN"
# choose platform
pf = "windows"    # windows / linux
# timestamp
time_now = time.strftime("_%Y_%m_%d__%H_%M")
print("*" * 10 + time_now + "*" * 10)
# itrs & steps
itrs = 200#4600
steps = 100
batchs = 5
# Choose Devices
os.environ["CUDA_VISIBLE_DEVICES"] = "0"
run_mode = "train"   # train / train_GPUs / test
mult_thread = False
# test
test_mode = 'auto'    # manual / auto
overlay = 0.5
if test_mode == 'manual':
    global_test_image_num = 18
    global_test_itr = 18
save_mode = "full"    # single / full
# Image Setting
dataset = 'IAILD'   # select dataset
read_image_mode = 'path'  # from path or file to read images
global_image_size = 256    # source image size
global_image_channels = 3   # source image channels (RGB = 3/RGBN = 4)
global_image_mode = 'rgb'   # source image mode (rgb / ?)
global_label_classes = 2    # label classes
global_label_mode = 'grayscale'  # label image mode (grayscale / rgb)
# Image Path
if dataset == 'IAILD':
    train_data_dir = "DataSet/IAILD/train"
    valid_data_dir = "DataSet/IAILD/test_" + str((int)(overlay*100))   # /media/tyk/汤昱焜的移动硬盘/SDFCN-base-on-unet-code/IAILD/test_875
    big_image_path = "origin_Dataset/testing"
    big_label_path = "origin_Dataset/testing_label"
elif dataset == 'GID':
    src_image_data_dir = "DataSet/IAILD/image_RGB"
    src_label_data_dir = "DataSet/IAILD/label_5classes"
    train_data_dir = "DataSet/IAILD/train_RGB"
    valid_data_dir = "DataSet/IAILD/vaild_RGB"
    label_data_dir = "DataSet/IAILD/label_RGB"
# log
log_dir = "G:\Aerial_Image_seg_v1.0\logs\log_final_MRDFCN"     #   "logs/log_final_" + model_name  # + time_now
#
saved_model = "model_save/" + model_name + "_final_" + str(global_image_size) + ".hdf5"

file_exist(run_mode, saved_model)

saved_results_path = "result/" + model_name + "_" + time_now
#
print(saved_model)
#

# training images preprocess args
data_gen_args = dict(rotation_range=45,  # 随机角度 应为整数
                     # width_shift_range=0.05, #水平平移
                     # height_shift_range=0.05,#垂直平移
                     # shear_range=0.05,
                     # zoom_range=0.05,
                     horizontal_flip=True,  # 随机水平翻转
                     vertical_flip=True,  # 随机垂直翻转
                     brightness_range=[0.6,1.4],  # 选择亮度偏移值的范围。
                     fill_mode='constant')
