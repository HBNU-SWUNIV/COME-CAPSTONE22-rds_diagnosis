import matplotlib.pyplot as plt
import numpy as np
import os
import json
import glob
import csv
from utils import dcm2png, polygon_area, average_point_inside, sort_angular


visualization = True
dir_path = r'C:\dataset\medical_imaging\RDS_dataset_20220210'  # RDS dataset path
dataset_csv_path = './dataset_info.csv'
csv_columns = ['filepath', 'exist_json', 'roi_area', 'height', 'width']
csv.register_dialect('custom_dialect', delimiter=',', lineterminator='\n')
with open(dataset_csv_path, 'w') as file:
    writer = csv.writer(file, 'custom_dialect')
    writer.writerow(csv_columns)

for dcm_filepath in glob.iglob(os.path.join(dir_path, '**/*.dcm'), recursive=True):
    print(f'# current image: {dcm_filepath}')
    curr_dict = dict(zip(csv_columns, [dcm_filepath, 0, 0, 0, 0]))
    json_filepath = dcm_filepath[:-3] + 'json'

    if os.path.exists(json_filepath):
        curr_dict['exist_json'] = 1
    else:
        curr_dict['exist_json'] = 0
        curr_dict['roi_area'] = 0

    scaled_arr = dcm2png(dcm_filepath)
    plt.imsave(dcm_filepath[:-3] + "png", scaled_arr, cmap=plt.cm.bone)  # save image
    zeros_arr = scaled_arr.copy()
    zeros_arr[:] = 0

    curr_dict['height'] = scaled_arr.shape[0]
    curr_dict['width'] = scaled_arr.shape[1]

    if visualization and curr_dict['exist_json'] == 1:
        # convert json to position list
        f = open(f"{json_filepath}", encoding="UTF-8")
        result = json.loads(f.read())
        pos_list = result['ArrayOfannotation_info'][0]['xyvalue']['pos_list']
        points = []
        for pos in pos_list:
            points.append(list(pos.values()))

        # calculate roi area
        reference_point = average_point_inside(points)
        sorted_points = sort_angular(points, reference_point)
        curr_dict['roi_area'] = polygon_area(sorted_points)
        points_array = np.array(points, dtype=np.uint)

        # save annotated image
        fig, ax = plt.subplots()
        x = scaled_arr.shape[1] / fig.dpi
        y = scaled_arr.shape[0] / fig.dpi
        fig.set_figwidth(x)
        fig.set_figheight(y)

        plt.imshow(zeros_arr, cmap=plt.cm.bone)  # plot zeros image
        plt.axis('off')
        plt.axis('scaled')
        plt.fill(points_array[:, 0], points_array[:, 1], color='lightgreen', alpha=0.3)
        # plt.show()
        png_filename = dcm_filepath[:-4] + "_annotations.png"
        plt.savefig(png_filename, bbox_inches='tight', pad_inches=0)

        # save overlay image
        fig, ax = plt.subplots()
        x = scaled_arr.shape[1] / fig.dpi
        y = scaled_arr.shape[0] / fig.dpi
        fig.set_figwidth(x)
        fig.set_figheight(y)

        plt.imshow(scaled_arr, cmap=plt.cm.bone)  # plot medical image
        plt.axis('off')
        plt.axis('scaled')
        plt.fill(points_array[:, 0], points_array[:, 1], color='lightgreen', alpha=0.3)  # overlay annotations
        # plt.show()
        png_filename = dcm_filepath[:-4] + "_overlay.png"
        plt.savefig(png_filename, bbox_inches='tight', pad_inches=0)

        plt.close('all')

    with open(dataset_csv_path, 'a') as file:
        writer = csv.writer(file, 'custom_dialect')
        writer.writerow(list(curr_dict.values()))

