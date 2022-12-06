"""
수동으로 gt_cls image로 부터 뼈 부분만 검정색으로 변경하고
해당 이미지를 다시 segmentation 수행을 위한 label image 생성
모든 이미지에 대해서 수행, docker 환경에서 작업하는 코드
"""

import cv2
import pandas as pd
import numpy as np

from tqdm import tqdm

data_0 = pd.read_csv("RDS_dataset_20220222/dataset_fold_0_5.csv", engine='python',encoding='CP949') #train #60 >> ~U~\~@ 깨~P ~W~@ ~Y~U~]
data_1 = pd.read_csv("RDS_dataset_20220222/dataset_fold_1_5.csv", engine='python',encoding='CP949')
data_2 = pd.read_csv("RDS_dataset_20220222/dataset_fold_2_5.csv", engine='python',encoding='CP949')
data_3 = pd.read_csv("RDS_dataset_20220222/dataset_fold_3_5.csv", engine='python',encoding='CP949') #valid
data_4 = pd.read_csv("RDS_dataset_20220222/dataset_fold_4_5.csv", engine='python',encoding='CP949') #test

re_label_df = pd.concat([data_0, data_1, data_2, data_3, data_4], ignore_index=True)

for i in range(len(re_label_df['filepath'])):
    re_label_df['filepath'][i] = re_label_df['filepath'][i].replace("호흡보조", "breathing assistance") #~U~\~@ ~]~K~] ~U~H ~U~D~\ ~@경
    re_label_df['filepath'][i] = re_label_df['filepath'][i].replace('\\', "/")
    re_label_df['filepath'][i] = re_label_df['filepath'][i].replace("C:/dataset/medical_imaging/", "")
    re_label_df['filepath'][i] = re_label_df['filepath'][i].replace(".dcm", "_RM.png")

cnt = 0

for i in tqdm(range(len(re_label_df['filepath']))):
    ori_path = re_label_df['filepath'][i]
    
    label_path = ori_path.replace("_RM.png", 'mask.png')
    
    ori_label_path = ori_path.replace("_RM.png", '_annotations.png')
    
    try:
        img = cv2.imread(ori_path)
        ori_label = cv2.imread(ori_label_path)
    
    
   # ori_label = cv2.imread(ori_label_path)
    
       # print("remove image shape : ", img.shape)
       # print("original label shape : ", ori_label.shape)

        if type(img) == type(None):
            print("None type : ", ori_path)
            pass
        else:
            make_label = img.copy()
            make_label[:] = 0
            zero_arr = np.array([0,0,0])
            fill_arr = np.array([255,255,255])

            for p in range(img.shape[0]):
                for q in range(img.shape[1]):
                    for r in range(3):
                        if img[p][q][r] == zero_arr[r]:
                            #make_label[p][q][r] = zero_arr[r]
#                           print("p : ", p , "q : ", q, img[p][q][r], ori_label[p][q][r])
                            pass
                        elif ori_label[p][q][r] == zero_arr[r]:
                            pass
                        else:
                            make_label[p][q] = fill_arr

            cv2.imwrite(label_path, make_label)

            img_label = cv2.imread(label_path)
        
            print(ori_path)
            print(img.shape)
            print(img_label.shape)
    
    except FileNotFoundError():
        print(ori_path)
        cnt += 1

print("File Not Found Count : ", cnt)
