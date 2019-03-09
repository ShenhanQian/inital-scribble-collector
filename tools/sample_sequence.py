import os
import json
import random
import numpy as np


db_root_dir = '/media/jia/668e5c5d-a703-4118-93ec-2bf71f556aa2/Youtube-VOS'


if __name__ == '__main__':
    random.seed(2019)
    np.random.seed(2019)

    num_seqs = 100

    seqs_list = dict()

    with open(os.path.join(db_root_dir, 'train', 'meta.json')) as f:
        train_meta = json.load(f)

    train_seqs = list(train_meta['videos'].keys())

    end_index = len(train_seqs) // num_seqs + 1

    print(len(train_seqs))

    for i in range(len(train_seqs) // num_seqs + 1):
        path = '../sequences/sequences_{:02d}.txt'.format(i + 1)

        if os.path.exists(path):
            with open(path) as f:
                random_seqs = f.readlines()
            random_seqs = [line.strip() for line in random_seqs]

            train_seqs = set(train_seqs) - set(random_seqs)
            train_seqs = list(train_seqs)
        else:
            if len(train_seqs) < num_seqs:
                random_seqs = train_seqs
            else:
                random_seqs = random.sample(train_seqs, num_seqs)
                train_seqs = set(train_seqs) - set(random_seqs)
                train_seqs = list(train_seqs)

        seqs_list[i + 1] = random_seqs

    with open('sequences.json', 'w') as f:
        json.dump(seqs_list, f)