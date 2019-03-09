import argparse
import json
import os
import shutil
import time
import json_absence_check

import cv2
import numpy as np

def init_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--dataset_dir', type=str, help='The path of dataset', default=None)
    parser.add_argument('--user_id', type=int, default=None)
    parser.add_argument('--list_id', type=int, default=None)
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

def generate_video(image_dir, scribble_dir, user_id, list_id):

    assert user_id is not None
    assert list_id is not None

    meta_json_path = os.path.join(image_dir,'..', 'meta.json')  # read meta.json
    with open(meta_json_path, 'r') as f1:
        info_json = json.load(f1)
        meta_dict = info_json['videos']

    user_json_name = '%03d_log_%02d.json' % (user_id, list_id)  # read user_log
    user_json_path = os.path.join(scribble_dir, user_json_name)
    with open(user_json_path, 'r') as f2:
        line = f2.readline()
        info_dict = json.loads(line)
    wrong_seq = info_dict['Error Sequences']
    # wrong_seq = set(info_dict['Error Sequences'])
    labeled_seq = info_dict['Labeled Sequences']
    # labeled_seq = set(info_dict['Labeled Sequences'])
    seq_num = len(labeled_seq)

    fourcc = cv2.VideoWriter_fourcc(*'XVID')  # start to generate video
    out = cv2.VideoWriter('scribbles_%03d-%02d.avi' % (user_id, list_id), fourcc, 400.0, (960, 540))
    # fourcc = cv2.VideoWriter_fourcc(*'H264')
    # out = cv2.VideoWriter('scribbles_%03d.mp4' % user_id, fourcc, 90.0, (854, 480))


    err_seq_list = []
    for seq_id, seq_name in enumerate(labeled_seq):
        if seq_name[-5:] == '.json':
            continue
        start_time = time.time()
        json_path = os.path.join(scribble_dir, seq_name, '%03d.json' % user_id)
        assert os.path.exists(json_path), f'{json_path} not exsit.'

        frame_list = np.sort(os.listdir(os.path.join(image_dir, seq_name)))

        frame_labeled = []
        scribbles = []
        with open(json_path, 'r') as file:
            line = file.readline()
            info_dict = json.loads(line)

        for idx, frame in enumerate(info_dict['scribbles']):
            if len(frame) > 0:
                frame_labeled.append(frame)
                frame_idx = idx

        assert len(frame_labeled) == 1, '%s: Number of labeled frame is %d rather than 1' % (seq_name, len(frame_labeled))
        scribbles = frame_labeled[0]


        image_path = os.path.join(image_dir, seq_name, frame_list[frame_idx])

        img = cv2.imread(image_path)
        img = cv2.resize(img, (960, 540))
        img_h, img_w, _ = img.shape

        # ratio = 0.8
        # img = cv2.resize(img, (int(img_w*ratio), int(img_h*ratio)))

        obj_list = []
        for stroke_id, stroke in enumerate(scribbles):
            for pt_i, pt in enumerate(stroke['path']):

                '''draw scribbles'''
                pt_x = int(img_w * pt[0])
                pt_y = int(img_h * pt[1])
                cv2.circle(img, (pt_x, pt_y), 2, getColor(stroke['object_id']), thickness=-1)
                cv2.putText(img, str(seq_id) + seq_name, (10, 30), 1, 2, (0, 255, 0))

                '''write video'''
                out.write(img)
                '''Count labeled object number'''
                obj_list.append(stroke['object_id'])
                # cv2.imshow('0', img)
                # cv2.waitKey(1)

        print(f'User {user_id}: Generated: {seq_name}, {seq_id}/{seq_num} in {time.time()-start_time}s')

        '''check labeled object number'''
        meta_obj_num = len(meta_dict[seq_name]['objects'])
        lbled_obj_num = len(set(obj_list))
        if lbled_obj_num != meta_obj_num:
            print('   Object number error: %d/%d' %(meta_obj_num, lbled_obj_num))
            err_seq_list.append(seq_id)

    # cv2.destroyAllWindows()
    if len(err_seq_list) != 0:
        print('Inomplete sequences:')
        for idx in err_seq_list:
            print(idx, labeled_seq[idx])
        op = input('Delete incomplete scribble? (Y/N)')
        if op == 'Y':
            for err_seq_id in err_seq_list:
                item_path = os.path.join(scribble_dir, labeled_seq[err_seq_id])
                shutil.rmtree(item_path)
            print('Incomplete scribbles cleared!')
        else:
            print('Remain not processed.')

    else:
        print('   Object number checking pass.')

if __name__ == '__main__':
    args = init_args()
    args.dataset_dir = 'E:\Documents\SIST\Projects\Davis_challenge\dataset\Youtube-VOS/'
    args.user_id = 9
    args.list_id = 5

    scribble_dir = os.path.join(args.dataset_dir, 'temp', 'Scribbles')
    # scribble_dir = os.path.join(args.dataset_dir, 'Scribbles')
    image_dir = os.path.join(args.dataset_dir,'train', 'JPEGImages', )

    assert os.path.exists(scribble_dir), '{:s} not exist'.format(scribble_dir)
    assert os.path.exists(image_dir), '{:s} not exist'.format(image_dir)


    generate_video(image_dir, scribble_dir, args.user_id, args.list_id)