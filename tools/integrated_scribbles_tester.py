import argparse
import json
import os
import os.path as ops
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
    return parser.parse_args()


if __name__ == '__main__':
    args = init_args()
    args.dataset_dir = 'E:\Documents\SIST\Projects\Davis_challenge\dataset\Youtube-VOS'
    args.user_id = 3
    args.list_id = 4

    scribble_dir = os.path.join(args.dataset_dir, 'temp', 'Scribbles')
    # scribble_dir = os.path.join(args.dataset_dir, 'Scribbles')
    image_dir = os.path.join(args.dataset_dir, 'JPEGImages', )

    assert ops.exists(scribble_dir), '{:s} not exist'.format(scribble_dir)
    assert ops.exists(image_dir), '{:s} not exist'.format(image_dir)


    if json_absence_check.inspect_json(scribble_dir, args.user_id, args.list_id):

        video_generator_Youtube_VOS.generate_video(image_dir, scribble_dir, args.user_id, args.list_id)