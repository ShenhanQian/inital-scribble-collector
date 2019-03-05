import os
import json
import random
import numpy as np

from pprint import pprint

db_root_dir = 'E:\Documents\SIST\Projects\Davis_challenge\dataset\Youtube-VOS'


if __name__ == '__main__':
    random.seed(2019)
    np.random.seed(2019)

    num_seqs = 100

    with open(os.path.join(db_root_dir, 'train', 'meta.json')) as f:
        meta_info = json.load(f)

    meta_info = meta_info['videos']

    train_seqs = list(meta_info.keys())

    random_seqs = random.sample(train_seqs, num_seqs)

    pprint(random_seqs)

    with open('sequences.txt', 'w') as f:
        f.write("\n".join(random_seqs))
x`