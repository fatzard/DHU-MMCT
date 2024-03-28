import cv2
import os
import numpy as np
from os.path import join, exists, split


def get_mean_and_std(img):
	x_mean, x_std = cv2.meanStdDev(img)
	x_mean = np.hstack(np.around(x_mean, 2))
	x_std = np.hstack(np.around(x_std, 2))
	return x_mean, x_std


def color_transfer(sc, dc):
	sc = cv2.cvtColor(sc, cv2.COLOR_BGR2LAB)
	s_mean, s_std = get_mean_and_std(sc)
	dc = cv2.cvtColor(dc, cv2.COLOR_BGR2LAB)
	t_mean, t_std = get_mean_and_std(dc)
	img_n = ((sc-s_mean)*(t_std/s_std))+t_mean
	np.putmask(img_n, img_n > 255, 255)
	np.putmask(img_n, img_n < 0, 0)
	dst = cv2.cvtColor(cv2.convertScaleAbs(img_n), cv2.COLOR_LAB2BGR)
	return dst


target_img_path = "/mnt/disk/shuanghong/dataset/scene_version_2/1/A/jpg/000001.jpg"
img_tmp = cv2.imread(target_img_path)
img_dir = "/mnt/disk/shuanghong/dataset/scene_version_2/1/C/jpg"
dir_top = "/mnt/disk/shuanghong/dataset/scene_version_2/1/C/"
create_path = os.path.join(dir_top + "transfer" )
if not exists(create_path):
	os.mkdir(create_path)
img_list = os.listdir(img_dir)
for i in img_list:
	if i.endswith(".jpg"):
		# print("i", i)
		img = cv2.imread(os.path.join(img_dir, i))
		dst = color_transfer(img, img_tmp)
		uav_save_path = os.path.join(create_path +'/'+ i)
		cv2.imwrite(uav_save_path,dst)

print("done!")

# class_list= os.listdir('D://University1652//test//query_satellite//')
# for i in class_list:
# 	create_path = os.path.join('C://Users//33513//Desktop//code//transgeo//query_drone//'+ i )
# 	os.mkdir(create_path)
# 	sat_path = os.path.join('D://University1652//test//query_satellite//'+ i + '//')
# 	uav_path = os.path.join('D://University1652//test//query_drone//'+ i + '//')
# 	sat_list = os.listdir(sat_path)
# 	uav_list = os.listdir(uav_path)
# 	sat_img_path = os.path.join('D://University1652//test//query_satellite//'+ i + '//'+sat_list[0])
# 	img = cv2.imread(sat_img_path)
# 	for j in uav_list:
# 		uav_img_path = os.path.join('D://University1652//test//query_drone//'+ i + '//'+j)
# 		img_tmp = cv2.imread(uav_img_path)
# 		dst = color_transfer(img_tmp, img)
# 		# uav_save_path = os.path.join('../autodl-tmp/University1652/train/drone/'+ i + '/'+j)
# 		uav_save_path = os.path.join('C://Users//33513//Desktop//code//transgeo//query_drone//'+ i + '//'+j)
# 		cv2.imwrite(uav_save_path,dst)