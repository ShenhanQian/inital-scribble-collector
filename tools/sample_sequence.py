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

    with open(os.path.join(db_root_dir, 'valid', 'meta.json')) as f:
        valid_meta = json.load(f)


    train_seqs = list(train_meta['videos'].keys())
    valid_seqs = list(valid_meta['videos'].keys())

    end_index = len(train_seqs) // num_seqs + 1

    print(len(train_seqs))
    print(len(valid_seqs))

    for i in range(len(train_seqs) // num_seqs + 1):
        if len(train_seqs) < num_seqs:
            random_seqs = train_seqs
        else:
            random_seqs = random.sample(train_seqs, num_seqs)
            train_seqs = set(train_seqs) - set(random_seqs)
            train_seqs = list(train_seqs)

        seqs_list[i + 1] = random_seqs

    print(end_index)

    for i in range(len(valid_seqs) // num_seqs + 1):
        if len(valid_seqs) < num_seqs:
            random_seqs = valid_seqs
        else:
            random_seqs = random.sample(valid_seqs, num_seqs)
            valid_seqs = set(valid_seqs) - set(random_seqs)
            valid_seqs = list(valid_seqs)

        print(end_index + i + 1)
        seqs_list[end_index + i + 1] = random_seqs

    print(seqs_list.keys())
    print(len(seqs_list))

    with open('sequences.json', 'w') as f:
        json.dump(seqs_list, f)