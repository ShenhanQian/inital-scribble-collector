import os, shutil
import json
import random
import numpy as np

from pprint import pprint

rt_dir = 'E:\Documents\SIST\Projects\Davis_challenge\dataset\Youtube-VOS'
output_dir = 'E:\Documents\SIST\Projects\Davis_challenge\dataset\Youtube_VOS_sample100'

if __name__ == '__main__':

    with open('sequences.txt', 'r') as f:

        samples = f.readlines()
        samples = [item.rstrip() for item in samples]

    # os.mkdir(os.path.join(rt_dir, '..', 'Youtube_VOS_sample100'))

    for i, seq in enumerate(samples):
        src_path_annot = os.path.join(rt_dir, 'CleanedAnnotations', seq)
        dst_path_annot = os.path.join(output_dir, 'CleanedAnnotations', seq)
        shutil.copytree(src_path_annot, dst_path_annot)
        if os.path.isdir(dst_path_annot):
            print(i, "Success A")

        src_path_jpg = os.path.join(rt_dir, 'JPEGImages', seq)
        dst_path_jpg = os.path.join(output_dir, 'JPEGImages', seq)
        shutil.copytree(src_path_jpg, dst_path_jpg)
        if os.path.isdir(dst_path_jpg):
            print(i, "Success J")







