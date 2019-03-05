'''Copyright (c) <2018> <Jonathon Luiten>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.'''

import numpy as np
from PIL import Image
import glob
import time
import cv2
import os

pascal_colormap = [
    0     ,         0,         0,
    0.5020,         0,         0,
         0,    0.5020,         0,
    0.5020,    0.5020,         0,
         0,         0,    0.5020,
    0.5020,         0,    0.5020,
         0,    0.5020,    0.5020,
    0.5020,    0.5020,    0.5020,
    0.2510,         0,         0,
    0.7529,         0,         0,]

def save_with_pascal_colormap(filename, arr):
  colmap = (np.array(pascal_colormap) * 255).round().astype("uint8")
  palimage = Image.new('P', (16, 16))
  palimage.putpalette(colmap)
  im = Image.fromarray(np.squeeze(arr.astype("uint8")))
  im2 = im.quantize(palette=palimage)
  im2.save(filename)

limit = 100 # pixels e.g. approx 10x10
db_root_dir = '/media/jia/668e5c5d-a703-4118-93ec-2bf71f556aa2/Youtube-VOS'
input = os.path.join(db_root_dir, 'train/Annotations/')
output = os.path.join(db_root_dir, 'train/CleanedAnnotations/')
folders = sorted(glob.glob(input + '*/'))
for vid_id,folder in enumerate(folders):
  if not os.path.exists(folder.replace(input,output)):
    os.makedirs(folder.replace(input,output))

  files = sorted(glob.glob(folder + '*.png'))
  for frame_id,file in enumerate(files):

    ann = np.array(Image.open(file))
    ids = np.unique(ann)
    ids = ids[ids != 0]
    cleaned_ann = ann.copy()
    for id in ids:
      mask = (ann==id)*id

      num_con, connected_mask = cv2.connectedComponents(mask)
      part_ids = np.unique(connected_mask)
      part_ids = part_ids[part_ids != 0]
      for part_id in part_ids:
        if np.count_nonzero(connected_mask == part_id) < limit:
          cleaned_ann[connected_mask == part_id] = 0
          print(vid_id,frame_id,id,part_id, np.count_nonzero(connected_mask == part_id), file.split('/')[-2:])
    save_with_pascal_colormap(file.replace(input,output),cleaned_ann)
  print("Video",vid_id,folder.split("/")[-2], "done")