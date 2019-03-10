import argparse
import json
import os
import time
import json_absence_check
import video_generator_Youtube_VOS

import cv2
import numpy as np

def init_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--dataset_dir', type=str, help='The path of dataset', default=None)
    parser.add_argument('--user_id', type=int, default=None)
    parser.add_argument('--list_id', type=int, default=None)
    parser.add_argument('--debug', type=bool, default=False)
    return parser.parse_args()


if __name__ == '__main__':
    args = init_args()
    args.dataset_dir = 'E:\Documents\SIST\Projects\Davis_challenge\dataset\Youtube-VOS'
    args.user_id = 6
    args.list_id = 3
    args.debug = True

    if args.debug == True:
        scribble_dir = os.path.join(args.dataset_dir, 'temp', 'Scribbles')
    else:
        scribble_dir = os.path.join(args.dataset_dir, 'Scribbles')

    image_dir = os.path.join(args.dataset_dir,'train', 'JPEGImages', )

    assert os.path.exists(scribble_dir), '{:s} not exist'.format(scribble_dir)
    assert os.path.exists(image_dir), '{:s} not exist'.format(image_dir)


    if json_absence_check.inspect_json(scribble_dir, args.user_id, args.list_id):
        video_generator_Youtube_VOS.generate_video(image_dir, scribble_dir, args.user_id, args.list_id)