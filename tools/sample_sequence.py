import os
import json
import random
import numpy as np


db_root_dir = '/media/jia/668e5c5d-a703-4118-93ec-2bf71f556aa2/Youtube-VOS'


if __name__ == '__main__':
    random.seed(2019)
    np.random.seed(2019)

    num_seqs = 100

    with open(os.path.join(db_root_dir, 'train', 'meta.json')) as f:
        meta_info = json.load(f)

    meta_info = meta_info['videos']

    train_seqs = list(meta_info.keys())

    print(len(train_seqs))

    for i in range(12):
        random_seqs = random.sample(train_seqs, num_seqs)

        train_seqs = set(train_seqs) - set(random_seqs)
        train_seqs = list(train_seqs)

        print(len(train_seqs))

        with open(f'seqence_{i+1:02d}.txt', 'w') as f:
            f.write("\n".join(random_seqs))
