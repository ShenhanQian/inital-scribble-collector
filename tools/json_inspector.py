import argparse
import json
import os
import os.path as ops
import time
# import shutil

import cv2
import numpy as np

def init_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--scribbles_dir', type=str, help='The path of scribble JSON file', default=None)
    parser.add_argument('--image_dir', type=str, help='The path of image file', default=None)

    return parser.parse_args()

def inspect_json(scribbles_dir, image_dir):
    """
    :param scribbles_dir:
    """
    assert ops.exists(scribbles_dir), '{:s} not exist'.format(scribbles_dir)
    assert ops.exists(image_dir), '{:s} not exist'.format(image_dir)
    
    file_list = np.sort(os.listdir(scribbles_dir))

    user_num = 0
    user_label_stat = [0, 0, 0, 0, 0, 0, 0]
    for f_name in file_list:
        if f_name[-5:] == '.json':  # user_log.json
            user_num += 1
            # json_list.append(f_name)

            json_path = os.path.join(scribbles_dir, f_name)
            with open(json_path, 'r') as file:
                line = file.readline()
                info_dict = json.loads(line)

                wrong_seq = info_dict['Error Sequences']
                labeled_seq = info_dict['Labeled Sequences']

                print(f'{f_name}:')
                print(f'    Error Sequences: {len(wrong_seq)}')
                print(f'    Labeled Sequences: {len(labeled_seq)}')
        else:  # scribble json
            json_dir = os.path.join(scribbles_dir, f_name)
            json_list = os.listdir(json_dir)

            count = 0
            for json_name in json_list:
                user_id = int(json_name.split('.')[0])
                json_path = os.path.join(scribbles_dir, f_name, json_name)

                # print(f'{f_name}/{json_name}: ', end='')

                with open(json_path, 'r') as file:
                    line = file.readline()
                    info_dict = json.loads(line)
                    for frame in info_dict['scribbles']:
                        if len(frame) != 0:
                            # print('Scribble get!')
                            user_label_stat[user_id-1] += 1

            # print(f'    {count} scribbles confirmed.')


    print('%d users in total.' % user_num)
    print(user_label_stat)



    # scribbles_dir, json_name = ops.split(scribbles_dir)
    # seq_name = scribbles_dir.rsplit('\\')[-1]
    # frame_idx = []
    #


    # print('frame:', frame_idx)

    # image_path = os.path.join(image_dir, seq_name,'%05d.jpg' %frame_idx)
    #
    # print(image_path)

    # img = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)
    # img_h, img_w, _ = img.shape

    # print('size:', img_h, img_w)
    # cv2.imshow('0', img)

    # for idx, stroke in enumerate(scribbles):
    #     for pt in stroke['path']:
    #         pt_x = int(img_w * pt[0])
    #         pt_y = int(img_h * pt[1])
    #         cv2.circle(img, (pt_x, pt_y), 1, (0,255,0))
    #         cv2.imshow('0', img)
    #         cv2.waitKey(1)
    #
    #
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()


if __name__ == '__main__':
    args = init_args()
    inspect_json(args.scribbles_dir, args.image_dir)