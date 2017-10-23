# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\ahshoe\Desktop\Pyslvs-PyQt5\core\synthesis\DimensionalSynthesis\Algorithm_path_adjust.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(509, 406)
        Dialog.setMinimumSize(QtCore.QSize(509, 406))
        Dialog.setMaximumSize(QtCore.QSize(509, 406))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/DimensionalSynthesis.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setModal(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.splitter = QtWidgets.QSplitter(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.Point_list = QtWidgets.QListWidget(self.splitter)
        self.Point_list.setObjectName("Point_list")
        self.tabWidget = QtWidgets.QTabWidget(self.splitter)
        self.tabWidget.setObjectName("tabWidget")
        self.moving = QtWidgets.QWidget()
        self.moving.setObjectName("moving")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.moving)
        self.verticalLayout_2.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.moving)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.moving)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.moving_y_coordinate = QtWidgets.QDoubleSpinBox(self.moving)
        self.moving_y_coordinate.setMinimum(-1000000.0)
        self.moving_y_coordinate.setMaximum(1000000.0)
        self.moving_y_coordinate.setObjectName("moving_y_coordinate")
        self.gridLayout.addWidget(self.moving_y_coordinate, 1, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 2, 1, 1)
        self.moving_x_coordinate = QtWidgets.QDoubleSpinBox(self.moving)
        self.moving_x_coordinate.setMinimum(-1000000.0)
        self.moving_x_coordinate.setMaximum(1000000.0)
        self.moving_x_coordinate.setObjectName("moving_x_coordinate")
        self.gridLayout.addWidget(self.moving_x_coordinate, 0, 1, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        spacerItem2 = QtWidgets.QSpacerItem(20, 99, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.movingButton = QtWidgets.QPushButton(self.moving)
        self.movingButton.setDefault(True)
        self.movingButton.setObjectName("movingButton")
        self.horizontalLayout_3.addWidget(self.movingButton)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.tabWidget.addTab(self.moving, "")
        self.scaling = QtWidgets.QWidget()
        self.scaling.setObjectName("scaling")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.scaling)
        self.verticalLayout_3.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem5, 0, 2, 1, 1)
        self.scaling_h = QtWidgets.QDoubleSpinBox(self.scaling)
        self.scaling_h.setMinimum(1.0)
        self.scaling_h.setMaximum(10000.0)
        self.scaling_h.setObjectName("scaling_h")
        self.gridLayout_2.addWidget(self.scaling_h, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.scaling)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.scaling)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 1, 0, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem6, 1, 2, 1, 1)
        self.scaling_v = QtWidgets.QDoubleSpinBox(self.scaling)
        self.scaling_v.setMinimum(1.0)
        self.scaling_v.setMaximum(10000.0)
        self.scaling_v.setObjectName("scaling_v")
        self.gridLayout_2.addWidget(self.scaling_v, 1, 1, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout_2)
        self.line = QtWidgets.QFrame(self.scaling)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_3.addWidget(self.line)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_5 = QtWidgets.QLabel(self.scaling)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)
        self.scaling_rx = QtWidgets.QDoubleSpinBox(self.scaling)
        self.scaling_rx.setMinimum(-1000000.0)
        self.scaling_rx.setMaximum(1000000.0)
        self.scaling_rx.setObjectName("scaling_rx")
        self.horizontalLayout_2.addWidget(self.scaling_rx)
        self.scaling_ry = QtWidgets.QDoubleSpinBox(self.scaling)
        self.scaling_ry.setMinimum(-1000000.0)
        self.scaling_ry.setMaximum(1000000.0)
        self.scaling_ry.setObjectName("scaling_ry")
        self.horizontalLayout_2.addWidget(self.scaling_ry)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem7)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        spacerItem8 = QtWidgets.QSpacerItem(20, 52, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem8)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem9)
        self.scalingButton = QtWidgets.QPushButton(self.scaling)
        self.scalingButton.setDefault(True)
        self.scalingButton.setObjectName("scalingButton")
        self.horizontalLayout_4.addWidget(self.scalingButton)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem10)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.tabWidget.addTab(self.scaling, "")
        self.blurring = QtWidgets.QWidget()
        self.blurring.setObjectName("blurring")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.blurring)
        self.verticalLayout_4.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_8 = QtWidgets.QLabel(self.blurring)
        self.label_8.setWordWrap(True)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_4.addWidget(self.label_8)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_7 = QtWidgets.QLabel(self.blurring)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_7.addWidget(self.label_7)
        self.points_num = QtWidgets.QLabel(self.blurring)
        self.points_num.setObjectName("points_num")
        self.horizontalLayout_7.addWidget(self.points_num)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem11)
        self.verticalLayout_4.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_6 = QtWidgets.QLabel(self.blurring)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_6.addWidget(self.label_6)
        self.blurring_num = QtWidgets.QSpinBox(self.blurring)
        self.blurring_num.setObjectName("blurring_num")
        self.horizontalLayout_6.addWidget(self.blurring_num)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem12)
        self.verticalLayout_4.addLayout(self.horizontalLayout_6)
        spacerItem13 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem13)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem14)
        self.blurringButton = QtWidgets.QPushButton(self.blurring)
        self.blurringButton.setDefault(True)
        self.blurringButton.setObjectName("blurringButton")
        self.horizontalLayout_8.addWidget(self.blurringButton)
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem15)
        self.verticalLayout_4.addLayout(self.horizontalLayout_8)
        self.tabWidget.addTab(self.blurring, "")
        self.verticalLayout.addWidget(self.splitter)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem16 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem16)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonBox.sizePolicy().hasHeightForWidth())
        self.buttonBox.setSizePolicy(sizePolicy)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel)
        self.buttonBox.setObjectName("buttonBox")
        self.horizontalLayout.addWidget(self.buttonBox)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Process ..."))
        self.label.setText(_translate("Dialog", "X coordinate: "))
        self.label_2.setText(_translate("Dialog", "Y coordinate: "))
        self.movingButton.setText(_translate("Dialog", "Moving"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.moving), _translate("Dialog", "Moving"))
        self.label_3.setText(_translate("Dialog", "Horizontal: "))
        self.label_4.setText(_translate("Dialog", "Vertical: "))
        self.label_5.setText(_translate("Dialog", "Reference point: "))
        self.scalingButton.setText(_translate("Dialog", "Scaling"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.scaling), _translate("Dialog", "Scaling"))
        self.label_8.setText(_translate("Dialog", "This function can minimize the number of coordinate points."))
        self.label_7.setText(_translate("Dialog", "The number of points: "))
        self.points_num.setText(_translate("Dialog", "0"))
        self.label_6.setText(_translate("Dialog", "Reduced to: "))
        self.blurringButton.setText(_translate("Dialog", "Blurring"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.blurring), _translate("Dialog", "Blurring"))

import icons_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

