import argparse
import json
import os
import time

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
    args.user_id = 3
    args.list_id = 3
    args.debug = True

    if args.debug == True:
        scribble_dir = os.path.join(args.dataset_dir, 'temp', 'Scribbles')
    else:
        scribble_dir = os.path.join(args.dataset_dir, 'Scribbles')

    image_dir = os.path.join(args.dataset_dir, 'JPEGImages', )

    assert os.path.exists(scribble_dir), '{:s} not exist'.format(scribble_dir)
    assert os.path.exists(image_dir), '{:s} not exist'.format(image_dir)


    '''Sequence List'''
    # seq_list_name = 'sequences_%02d.txt' % args.list_id
    # seq_list_path = os.path.join('..', 'sequences', seq_list_name)
    #
    # assert os.path.exists(seq_list_path), '{:s} not exist'.format(seq_list_path)
    #
    # with open(seq_list_path, 'r') as f1:
    #     seq_list = f1.readlines()
    #     seq_list = [i.rstrip() for i in seq_list]
    #     seq_set = set(seq_list)
    #     seq_num = len(seq_list)

    '''Existing Labeled json'''
    labeled_seq = set(os.listdir(scribble_dir))
    labeled_seq = set(seq for seq in labeled_seq if seq[-5:] != '.json')

    '''User json'''
    user_json_name = '%03d_log_%02d.json' % (args.user_id, args.list_id)
    user_json_path = os.path.join(scribble_dir, user_json_name)
    with open(user_json_path, 'r') as f2:
        line = f2.readline()
        info_dict = json.loads(line)

        wrong_seq_log = set(info_dict['Error Sequences'])
        labeled_seq_log = set(info_dict['Labeled Sequences'])

    '''Evaluation'''
    if len(labeled_seq_log) == len(labeled_seq):
        print('Match!')
    elif len(labeled_seq_log) > len(labeled_seq):
        print('Missed dir:')
        print(labeled_seq_log - labeled_seq)
    elif len(labeled_seq_log) < len(labeled_seq):
        print('Extra dir:')
        print(labeled_seq - labeled_seq_log)
