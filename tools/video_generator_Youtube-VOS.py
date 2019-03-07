import argparse
import json
import os
import os.path as ops
import time
# import shutil


import cv2
import imageio
import numpy as np

def init_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--dataset_dir', type=str, help='The path of dataset', default=None)
    return parser.parse_args()

def getColor(idx):
    palette = [(0, 255, 255), (255, 0, 255), (60, 60, 255), (255, 30, 30), (200, 255, 2),
               (0, 160, 0), (255, 100, 0), (100, 255, 255), (255, 200, 255), (60, 60, 200),
               (255, 90, 90), (100, 255, 100), (0, 160, 160), (160, 160, 0)]
    # 青
    # purple
    # blue
    # red
    # Yellow
    # dark green
    # orange

    assert idx < len(palette)
    return palette[idx]

def generate_video(dataset_dir):
    # scribble_dir = os.path.join(dataset_dir, 'Scribbles')
    # image_dir = os.path.join(dataset_dir, 'JPEGImages',)

    user_id_list = [7]

    scribble_dir = os.path.join(dataset_dir, 'temp', 'Scribbles')
    image_dir = os.path.join(dataset_dir, 'JPEGImages',)

    assert ops.exists(scribble_dir), '{:s} not exist'.format(scribble_dir)
    assert ops.exists(image_dir), '{:s} not exist'.format(image_dir)

    seq_list = np.sort(os.listdir(scribble_dir))
    seq_num = len(seq_list)

    for user_id in user_id_list:
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        out = cv2.VideoWriter('scribbles_%03d.avi' % user_id, fourcc, 400.0, (960, 540))
        # fourcc = cv2.VideoWriter_fourcc(*'H264')
        # out = cv2.VideoWriter('scribbles_%03d.mp4' % user_id, fourcc, 90.0, (854, 480))

        for seq_id, seq_name in enumerate(seq_list):
            if seq_name[-5:] == '.json':
                continue
            start_time = time.time()
            json_path = os.path.join(scribble_dir, seq_name, '%03d.json' % user_id)
            assert os.path.exists(json_path), f'{json_path} not exsit.'

            frame_list = np.sort(os.listdir(os.path.join(image_dir, seq_name)))

            frame_idx = []
            scribbles = []
            with open(json_path, 'r') as file:
                line = file.readline()
                info_dict = json.loads(line)
                for idx, frame in enumerate(info_dict['scribbles']):
                    if len(frame) > 0:
                        frame_idx = idx
                        scribbles = frame

            print(seq_name)
            image_path = os.path.join(image_dir, seq_name, frame_list[frame_idx])

            img = cv2.imread(image_path)
            img = cv2.resize(img, (960, 540))
            img_h, img_w, _ = img.shape

            # ratio = 0.8
            # img = cv2.resize(img, (int(img_w*ratio), int(img_h*ratio)))


            for stroke_id, stroke in enumerate(scribbles):
                for pt_i, pt in enumerate(stroke['path']):
                        pt_x = int(img_w * pt[0])
                        pt_y = int(img_h * pt[1])
                        cv2.circle(img, (pt_x, pt_y), 2, getColor(stroke['object_id']), thickness=-1)
                        cv2.putText(img, seq_name, (10, 30), 1, 2, (0, 255, 0))
                        # cv2.imshow('0', img)
                        out.write(img)
                        # cv2.waitKey(1)
            print(f'User {user_id}: Generated {seq_id}/{seq_num} in {time.time()-start_time}s')

            # break

    # cv2.destroyAllWindows()

if __name__ == '__main__':
    args = init_args()
    generate_video(args.dataset_dir)