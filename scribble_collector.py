import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QImage, QPixmap, QPen, QBrush, QPainter  # QCursor  # QPainter, QBrush
from scribble_collector_UI import Ui_Form  # import from the py file generated by Qt_Designer
# from Dialog_UI import Ui_Dialog  # import from the py file generated by Qt_Designer
import argparse
import json
import os
import time
import numpy as np
import cv2
from PIL import Image

# class DialogWindow(QtWidgets.QDialog, Ui_Dialog):
#     def __init__(self):
#         super().__init__()
#         self.setupUi(self)

class MainWindow(QtWidgets.QWidget, Ui_Form):
    def __init__(self, dataset_dir, user_id, list_id):
        super().__init__()
        self.setupUi(self)

        self.dataset_dir = dataset_dir
        self.seq_dir = os.path.join(self.dataset_dir, 'JPEGImages')
        assert os.path.exists(self.seq_dir), print('Error with dataset_dir: Jpeg not exist')
        self.annot_dir = os.path.join(self.dataset_dir, 'CleanedAnnotations')
        assert os.path.exists(self.seq_dir), print('Error with dataset_dir: CleanAnnotation not exist')

        self.user_id =user_id
        assert self.user_id is not None, print('Error with user id')

        self.list_id = list_id
        assert self.list_id is not None, print('Error with list id')
        self.label_list.setText('List: %d    User: %d' % (int(self.list_id), int(self.user_id)))

        error_json_dir = os.path.join(self.dataset_dir, 'Scribbles', )

        if os.path.exists(error_json_dir) is False:
            os.makedirs(error_json_dir)
        self.user_json_path = os.path.join(error_json_dir, '%03d_log_%02d.json' % (int(self.user_id), int(self.list_id)))

        print('Loading...')
        self.afterGenerationConfig()

    def afterGenerationConfig(self):
        self.user_dict = dict()
        self.labeled_seq = set()
        self.seq_idx = 0
        self.loadSeqList()
        self.loadUserJson()

        self.canvas.setMouseTracking(True)
        self.horizontalSlider.valueChanged.connect(self.reset)
        self.canvas.mouseMoveEvent = self.cursorMoveEvent
        self.canvas.mousePressEvent = self.cursorPressEvent
        self.canvas.mouseReleaseEvent = self.cursorReleaseEvent
        #
        self.pushButton_rst.clicked.connect(self.reset)
        self.pushButton_save.clicked.connect(self.save)
        self.pushButton_err.clicked.connect(self.err)

        self.selectSeq()

    def selectSeq(self):
        self.painting = False
        self.init_time = None
        self.horizontalSlider.setValue(0)

        self.seq_name = self.seq_list[self.seq_idx]
        self.label_seq.setText('Sequence: ' + str(len(self.labeled_seq) + len(self.error_seq)) + '/' + str(self.seq_num) + f' {self.seq_name}')

        self.frame_dir = self.seq_dir + '/' + self.seq_name
        self.frame_list = np.sort(os.listdir(self.frame_dir))
        self.frame_nums = len(self.frame_list)
        self.horizontalSlider.setMaximum(self.frame_nums - 1)

        self.annot_frame_dir = self.annot_dir + '/' + self.seq_name
        self.annot_frame_list = np.sort(os.listdir(self.annot_frame_dir))
        self.annot_frame_nums = len(self.frame_list)

        assert self.frame_nums == self.annot_frame_nums  # annotations should correspond with frames

        self.loadExistJson()
        self.loadMetaJson()
        self.reset()

    def loadUserJson(self):
        try:
            with open(self.user_json_path, 'r') as f:
                json_info = json.load(f)
                self.error_seq = set(json_info['Error Sequences'])
        except:
            self.error_seq = set()

    def loadSeqList(self):
        txt_path = './sequences/sequences_%02d.txt' % int(self.list_id)
        assert os.path.exists(txt_path), txt_path

        with open(txt_path, 'r') as file:
            self.seq_list = file.readlines()
        self.seq_list = [i.rstrip() for i in self.seq_list]
        self.seq_num = len(self.seq_list)

    def loadExistJson(self):
        read_path = os.path.join(self.dataset_dir, 'Scribbles', self.seq_name)
        json_path = os.path.join(read_path, '%03d.json' % (int(self.user_id)))

        print('Sequence: ' + str(self.seq_idx) + '/' + str(self.seq_num))

        if os.path.exists(json_path) is True:
            with open(json_path, 'r') as file:
                line = file.readline()
                info_dict = json.loads(line)
            self.labeled_seq.add(self.seq_name)
            self.nextSeq()
            # return

        if self.seq_name in self.error_seq:
            self.nextSeq()


    def loadMetaJson(self):
        meta_json_path = self.dataset_dir + '/meta.json'
        with open(meta_json_path, 'r') as f:
            meta_json = json.load(f)
        self.obj_num = len(meta_json['videos'][self.seq_name]['objects'])
        self.label_obj.setText('Obj Number: ' + str(self.obj_num))

    def loadImg(self):
        img_path = self.frame_dir + '/' + self.frame_list[self.horizontalSlider.value()]
        img = cv2.imread(img_path)

        self.img_H, self.img_W, _ = img.shape

        self.loadMask()

        for idx, mask in enumerate(self.mask_list):
            inv_mask = cv2.bitwise_not(mask)
            c_img = self.getBlank(img.shape[1], img.shape[0], self.getColor(idx))
            fg = cv2.addWeighted(img, 0.6, c_img, 0.4, 0)
            fg = cv2.bitwise_and(fg, fg, mask=mask)
            bg = cv2.bitwise_and(img, img, mask=inv_mask)
            img = cv2.add(fg, bg)

        self.img = img
        self.updatePixmap()

    def loadMask(self):
        annot_frame_path = self.annot_frame_dir + '/' +self.annot_frame_list[self.horizontalSlider.value()]

        self.label = Image.open(annot_frame_path)
        self.label = np.array(self.label, dtype=np.uint8)

        self.mask_list = []
        for i in range(1, self.obj_num + 1):
            mask = np.array(self.label == i, dtype=np.uint8) * 255
            self.mask_list.append(mask)


    def updatePixmap(self):
        self.img = cv2.resize(self.img, (1280, 720))
        rgbImage = cv2.cvtColor(self.img, cv2.COLOR_BGR2RGB)
        convertToQtFormat = QImage(rgbImage.data, rgbImage.shape[1], rgbImage.shape[0],
                                   QImage.Format_RGB888)

        # self.pixmap = QPixmap.fromImage(convertToQtFormat.scaledToHeight(, 450))
        self.pixmap = QPixmap.fromImage(convertToQtFormat)

        self.canvas.setPixmap(self.pixmap)

    def drawPoint(self, x, y):
        pen = QPen(QtCore.Qt.green)
        brush = QBrush(QtCore.Qt.green)

        painter = QPainter(self.pixmap)
        painter.setPen(pen)
        painter.setBrush(brush)
        painter.drawEllipse(x, y, 3, 3)
        self.canvas.setPixmap(self.pixmap)

    def getColor(self, idx):
        palette = [(0, 255, 255), (255, 0, 255), (60, 60, 255), (255, 30, 30), (200, 255, 2), (0, 160, 0), (255, 100, 0)]
        # 青
        # purple
        # blue
        # red
        # Yellow
        # dark green
        # orange

        assert idx < len(palette)
        return palette[idx]

    def getBlank(self, width, height, rgb_color=(0, 0, 0)):
        """Create new image(numpy array) filled with certain color in RGB"""
        # Create black blank image
        image = np.zeros((height, width, 3), np.uint8)

        # Since OpenCV uses BGR, convert the color first
        color = tuple(reversed(rgb_color))
        # Fill image with color
        image[:] = color
        return image

    def bitget(self, byteval, idx):
        return ((byteval & (1 << idx)) != 0)

    def labelcolormap(self, N=256):
        color_map = np.zeros((N, 3))
        for n in range(N):
            id_num = n
            r, g, b = 0, 0, 0
            for pos in range(8):
                r = np.bitwise_or(r, (self.bitget(id_num, 0) << (7-pos)))
                g = np.bitwise_or(g, (self.bitget(id_num, 1) << (7-pos)))
                b = np.bitwise_or(b, (self.bitget(id_num, 2) << (7-pos)))
                id_num = (id_num >> 3)
            color_map[n, 0] = r
            color_map[n, 1] = g
            color_map[n, 2] = b
        return color_map



# User Interface
    def nextSeq(self):
        if self.seq_idx < self.seq_num - 1:
            self.seq_idx += 1
            # print(self.seq_idx)
            self.selectSeq()
        else:
            self.label_seq.setText(
                'Sequence: ' + str(len(self.labeled_seq) + len(self.error_seq)) + '/' + str(self.seq_num))
            self.saveUserJson()
            self.destroy(True)
            print('Congratulations! Mission Complete!')
            sys.exit()

    def lastSeq(self):
        if self.seq_idx > 0:
            self.seq_idx -= 1
        self.selectSeq()

    def nextFrame(self):
        self.horizontalSlider.setValue(self.horizontalSlider.value() + 1)

    def lastFrame(self):
        self.horizontalSlider.setValue(self.horizontalSlider.value() - 1)

    def delete(self):
        '''remove the last stroke'''
        pass

    def reset(self):
        '''remove all the scribbles'''
        self.loadImg()
        self.label_frame.setText('Frame: ' + str(self.horizontalSlider.value()) + '/' + str(self.frame_nums))

        self.init_time = None
        self.labeled_obj = []
        self.scribbles = {'scribbles': [], 'sequence': self.seq_name}
        self.stroke_list = []
        self.label_info.setText('')

    def save(self):
        '''save all the stroke in the current frame'''
        if len(self.labeled_obj) < self.obj_num:
            self.label_info.setText('Labeling not complete!')
            return

        output_path = os.path.join(self.dataset_dir, 'Scribbles', self.seq_name)

        if os.path.exists(output_path) is False:
            os.makedirs(output_path)

        json_path = os.path.join(output_path, '%03d.json' % (int(self.user_id)))

        for idx in range(0,self.frame_nums):
            if idx == self.horizontalSlider.value():
                self.scribbles['scribbles'].append(self.stroke_list)
            else:
                self.scribbles['scribbles'].append([])

        with open(json_path, 'w') as f:
            json.dump(self.scribbles, f)

        self.labeled_seq.add(self.seq_name)
        self.saveUserJson()
        
        self.nextSeq()

    def saveUserJson(self):
        with open(self.user_json_path, 'w') as f:
            self.user_dict['Labeled Sequences'] = list(self.labeled_seq)
            self.user_dict['Error Sequences'] = list(self.error_seq)

            json.dump(self.user_dict, f)

    def err(self):
        self.error_seq.add(self.seq_name)
        self.saveUserJson()


    # Callback functions
    def resizeEvent(self, event):
        pass
        self.updatePixmap()

    def cursorMoveEvent(self, event):
        x = event.x()
        y = event.y()
        if x<0 or x>= self.img_W or y<0 or y>= self.img_H:
            self.painting = False
            return

        if self.painting == True:
            if self.label[y, x] == self.curent_obj:
                self.drawPoint(x, y)
                self.cur_stroke['path'].append([x/float(self.img_W), y/float(self.img_H)])
            else:
                self.label_info.setText('Out of mask!')
                self.painting = False

    def cursorPressEvent(self, event):
        x = event.x()
        y = event.y()

        if x<0 or x>= self.img_W or y<0 or y>= self.img_H:
            return

        if self.label[y, x] != 0:
            self.painting = True
            self.curent_obj = self.label[y, x]

            self.cur_stroke = dict()

            self.cur_stroke['path'] = []
            self.cur_stroke['path'].append([x/float(self.img_W), y/float(self.img_H)])
            # self.cur_stroke['path'].append([x, y])


            self.cur_stroke['object_id'] = int(self.curent_obj)
            self.labeled_obj.append(self.curent_obj)

            if self.init_time is None:
                self.init_time = int(time.time() * 1000)
                self.cur_stroke['start_time'] = 0
            else:
                self.cur_stroke['start_time'] = int(time.time() * 1000) - self.init_time

        else:
            self.label_info.setText('Out of mask!')


    def cursorReleaseEvent(self, event):
        if self.painting == True:
            self.painting = False
            self.cur_stroke['end_time'] = int(time.time()*1000) - self.init_time
            self.stroke_list.append(self.cur_stroke)
        self.label_info.setText('')

    def keyPressEvent(self, QKeyEvent):
        if QKeyEvent.key() == QtCore.Qt.Key_Space:
            self.save()
        elif QKeyEvent.key() == QtCore.Qt.Key_R:
            self.reset()
        elif QKeyEvent.key() == QtCore.Qt.Key_A:
            self.lastFrame()
        elif QKeyEvent.key() == QtCore.Qt.Key_D:
            self.nextFrame()


    # Debug functions

    def imshow(self, im):
        cv2.imshow('0', im)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


def init_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--dataset_dir', type=str, help='The path of dataset', default=None)
    parser.add_argument('--user_id', type=str, default=None)
    parser.add_argument('--list_id', type=str, default=None)
    return parser.parse_args()



if __name__ == "__main__":

    args = init_args()
    assert args.dataset_dir is not None, print('Please specify the right path with --dataset_dir')

    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow(args.dataset_dir, args.user_id, args.list_id)
    mainWin.show()
    sys.exit(app.exec_())
