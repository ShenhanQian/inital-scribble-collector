# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'scribble_collector_UI.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1127, 827)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.canvas = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.canvas.sizePolicy().hasHeightForWidth())
        self.canvas.setSizePolicy(sizePolicy)
        self.canvas.setMinimumSize(QtCore.QSize(0, 0))
        self.canvas.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.canvas.setText("")
        self.canvas.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.canvas.setObjectName("canvas")
        self.verticalLayout.addWidget(self.canvas)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_list = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        self.label_list.setFont(font)
        self.label_list.setObjectName("label_list")
        self.horizontalLayout_7.addWidget(self.label_list)
        self.label_seq = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.label_seq.setFont(font)
        self.label_seq.setObjectName("label_seq")
        self.horizontalLayout_7.addWidget(self.label_seq)
        self.label_frame = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_frame.sizePolicy().hasHeightForWidth())
        self.label_frame.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_frame.setFont(font)
        self.label_frame.setObjectName("label_frame")
        self.horizontalLayout_7.addWidget(self.label_frame)
        self.label_obj = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_obj.setFont(font)
        self.label_obj.setObjectName("label_obj")
        self.horizontalLayout_7.addWidget(self.label_obj)
        self.label_info = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_info.setFont(font)
        self.label_info.setText("")
        self.label_info.setObjectName("label_info")
        self.horizontalLayout_7.addWidget(self.label_info)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.horizontalSlider = QtWidgets.QSlider(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalSlider.sizePolicy().hasHeightForWidth())
        self.horizontalSlider.setSizePolicy(sizePolicy)
        self.horizontalSlider.setMouseTracking(False)
        self.horizontalSlider.setFocusPolicy(QtCore.Qt.NoFocus)
        self.horizontalSlider.setMaximum(50)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.verticalLayout.addWidget(self.horizontalSlider)
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_rst = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_rst.sizePolicy().hasHeightForWidth())
        self.pushButton_rst.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_rst.setFont(font)
        self.pushButton_rst.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_rst.setObjectName("pushButton_rst")
        self.horizontalLayout_3.addWidget(self.pushButton_rst)
        self.pushButton_save = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_save.sizePolicy().hasHeightForWidth())
        self.pushButton_save.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_save.setFont(font)
        self.pushButton_save.setObjectName("pushButton_save")
        self.horizontalLayout_3.addWidget(self.pushButton_save)
        self.pushButton_err = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_err.setFont(font)
        self.pushButton_err.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_err.setObjectName("pushButton_err")
        self.horizontalLayout_3.addWidget(self.pushButton_err)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Initial Scribbles Collector"))
        self.label_list.setText(_translate("Form", "List: "))
        self.label_seq.setText(_translate("Form", "Seq: "))
        self.label_frame.setText(_translate("Form", "Frame:"))
        self.label_obj.setText(_translate("Form", "Obj Number:  "))
        self.label.setText(_translate("Form", "A:Last frame  D:Next frame"))
        self.pushButton_rst.setText(_translate("Form", "Reset Scirbble(R)"))
        self.pushButton_save.setText(_translate("Form", "Save(Space)"))
        self.pushButton_err.setText(_translate("Form", "Wrong Sequence"))

