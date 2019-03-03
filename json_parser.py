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
                # for item in frame:
                #     stroke = dict()
                #     stroke['path'] = item['path']
                #     stroke['object_id'] = item['object_id']
                #     stroke['start_time'] = item['start_time']
                #     stroke['end_time'] = item['end_time']
                #     scribbles.append(stroke)


    # image_path = image_dir + seq_name + '\\' + str(frame_idx) + '.jpg'
    image_path = image_dir + seq_name + '\\' + '%05d' %frame_idx + '.jpg'
    print(image_path)

    img = cv2.imread(image_path)
    img_h, img_w, _ = img.shape
    print(img_h, img_w)
    cv2.imshow('0', img)

    for idx, stroke in enumerate(scribbles):
        for pt in stroke['path']:
            pt_x = int(img_w * pt[0])
            pt_y = int(img_h * pt[1])
            cv2.circle(img, (pt_x, pt_y), 1, (0,255,0))
            cv2.imshow('0', img)
            cv2.waitKey(4)

            # time.sleep(1)


            # print(pt_x, pt_y)
        # print(idx, stroke['path'])

    cv2.waitKey(0)
    cv2.destroyAllWindows()

        # for line_index, line in enumerate(file):
        #
        #
        #     image_dir = ops.split(info_dict['raw_file'])[0]
        #     image_dir_split = image_dir.split('/')[1:]
        #     image_dir_split.append(ops.split(info_dict['raw_file'])[1])
        #     image_name = '_'.join(image_dir_split)
        #     image_path = ops.join(src_dir, info_dict['raw_file'])
        #     assert ops.exists(image_path), '{:s} not exist'.format(image_path)
        #
        #     h_samples = info_dict['h_samples']
        #     lanes = info_dict['lanes']
        #
        #     image_name_new = '{:s}.png'.format('{:d}'.format(line_index + image_nums).zfill(4))
        #
        #     src_image = cv2.imread(image_path, cv2.IMREAD_COLOR)
        #     dst_binary_image = np.zeros([src_image.shape[0], src_image.shape[1]], np.uint8)
        #     dst_instance_image = np.zeros([src_image.shape[0], src_image.shape[1]], np.uint8)
        #
        #     for lane_index, lane in enumerate(lanes):
        #         assert len(h_samples) == len(lane)
        #         lane_x = []
        #         lane_y = []
        #         for index in range(len(lane)):
        #             if lane[index] == -2:
        #                 continue
        #             else:
        #                 ptx = lane[index]
        #                 pty = h_samples[index]
        #                 lane_x.append(ptx)
        #                 lane_y.append(pty)
        #         if not lane_x:
        #             continue
        #         lane_pts = np.vstack((lane_x, lane_y)).transpose()
        #         lane_pts = np.array([lane_pts], np.int64)
        #
        #         cv2.polylines(dst_binary_image, lane_pts, isClosed=False,
        #                       color=255, thickness=5)
        #         cv2.polylines(dst_instance_image, lane_pts, isClosed=False,
        #                       color=lane_index * 50 + 20, thickness=5)
        #
        #     dst_binary_image_path = ops.join(binary_dst_dir, image_name_new)
        #     dst_instance_image_path = ops.join(instance_dst_dir, image_name_new)
        #     dst_rgb_image_path = ops.join(ori_dst_dir, image_name_new)
        #
        #     cv2.imwrite(dst_binary_image_path, dst_binary_image)
        #     cv2.imwrite(dst_instance_image_path, dst_instance_image)
        #     cv2.imwrite(dst_rgb_image_path, src_image)
        #
        #     print('Process {:s} success'.format(image_name))


if __name__ == '__main__':
    args = init_args()
    parse_json(args.json_path, args.image_dir)