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
    parser.add_argument('--seq_list_path', type=str, help='', default=None)
    parser.add_argument('--user_json_path', type=str, help='', default=None)

    return parser.parse_args()

def inspect_json(scribble_dir, user_id, list_id):
    """
    :param scribbles_dir:
    """
    user_json_name = '%03d_log_%02d.json' % (user_id, list_id)
    user_json_path = os.path.join(scribble_dir, user_json_name)
    seq_list_name = 'sequences_%02d.txt' % list_id
    seq_list_path = os.path.join('..', 'sequences', seq_list_name)

    assert ops.exists(seq_list_path), '{:s} not exist'.format(seq_list_path)
    assert ops.exists(user_json_path), '{:s} not exist'.format(user_json_path)

    with open(seq_list_path, 'r') as f1:
        seq_list = f1.readlines()
        seq_list = [i.rstrip() for i in seq_list]
        seq_set = set(seq_list)
        seq_num = len(seq_list)

    with open(user_json_path, 'r') as f2:
        line = f2.readline()
        info_dict = json.loads(line)

        wrong_seq = set(info_dict['Error Sequences'])
        labeled_seq = set(info_dict['Labeled Sequences'])

    absent_seq = seq_set - wrong_seq - labeled_seq


    print(f'Error Sequences: {len(wrong_seq)}')
    print(f'Labeled Sequences: {len(labeled_seq)}')

    if len(wrong_seq) + len(labeled_seq) ==100:
        print('  Files are complete.')
        return True
    else:
        print('  Missing seq: ', absent_seq)
        return False

    # for item in absent_seq:
    #     for idx, seq in enumerate(seq_list):
    #         if item == seq:
    #             print(idx)

if __name__ == '__main__':
    args = init_args()

    user_id = 7
    list_id = 4
    json_name = '%03d_log_%02d.json' % (user_id, list_id)
    args.seq_list_path = os.path.join('..', 'sequences', 'sequences_%02d.txt' % list_id)
    # args.user_json_path = os.path.join('..', '..', 'dataset', 'Youtube-VOS', 'temp', 'Scribbles', json_name)
    args.user_json_path = os.path.join('..', '..', 'dataset', 'Youtube-VOS', 'Scribbles', json_name)

    inspect_json(args.seq_list_path, args.user_json_path)