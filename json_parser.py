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
    parser.add_argument('--json_path', type=str, help='The path of scribble JSON file', default=None)
    parser.add_argument('--image_dir', type=str, help='The path of image file', default=None)

    return parser.parse_args()

def parse_json(json_path, image_dir):
    """
    :param json_path:
    """
    assert ops.exists(json_path), '{:s} not exist'.format(json_path)
    assert ops.exists(image_dir), '{:s} not exist'.format(image_dir)

    json_dir, json_name = ops.split(json_path)
    seq_name = json_dir.rsplit('\\')[-1]
    frame_idx = []

    with open(json_path, 'r') as file:
        line = file.readline()
        info_dict = json.loads(line)

        for idx, frame in enumerate(info_dict['scribbles']):
            if len(frame) > 0:
                frame_idx = idx
                scribbles = frame


    print('frame:', frame_idx)
    # for DAVIS
    # image_path = image_dir + seq_name + '\\' + '%05d' %frame_idx + '.jpg

    # for Youtube_VOS
    image_path = os.path.join(image_dir, seq_name,'%05d.jpg' %frame_idx)

    print(image_path)

    img = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)
    img_h, img_w, _ = img.shape

    print('size:', img_h, img_w)
    # cv2.imshow('0', img)

    for idx, stroke in enumerate(scribbles):
        for pt in stroke['path']:
            pt_x = int(img_w * pt[0])
            pt_y = int(img_h * pt[1])
            cv2.circle(img, (pt_x, pt_y), 1, (0,255,0))
            cv2.imshow('0', img)
            cv2.waitKey(1)


    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    args = init_args()
    parse_json(args.json_path, args.image_dir)