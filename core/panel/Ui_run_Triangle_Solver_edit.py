# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\ahshoe\Desktop\Pyslvs-PyQt5\core\panel\run_Triangle_Solver_edit.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(780, 630)
        Dialog.setMinimumSize(QtCore.QSize(780, 630))
        Dialog.setMaximumSize(QtCore.QSize(780, 630))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/TS.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setModal(True)
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_14.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout_14.setSpacing(6)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.typePanel = QtWidgets.QWidget(Dialog)
        self.typePanel.setObjectName("typePanel")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.typePanel)
        self.verticalLayout_3.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.typeLayout = QtWidgets.QGroupBox(self.typePanel)
        self.typeLayout.setObjectName("typeLayout")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.typeLayout)
        self.verticalLayout_10.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.type = QtWidgets.QComboBox(self.typeLayout)
        self.type.setObjectName("type")
        self.type.addItem("")
        self.type.addItem("")
        self.type.addItem("")
        self.verticalLayout_10.addWidget(self.type)
        self.verticalLayout_3.addWidget(self.typeLayout)
        self.mergeLayout = QtWidgets.QGroupBox(self.typePanel)
        self.mergeLayout.setObjectName("mergeLayout")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.mergeLayout)
        self.verticalLayout_11.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.merge = QtWidgets.QComboBox(self.mergeLayout)
        self.merge.setObjectName("merge")
        self.verticalLayout_11.addWidget(self.merge)
        self.verticalLayout_3.addWidget(self.mergeLayout)
        self.other = QtWidgets.QCheckBox(self.typePanel)
        self.other.setObjectName("other")
        self.verticalLayout_3.addWidget(self.other)
        spacerItem = QtWidgets.QSpacerItem(20, 1, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.horizontalLayout_3.addWidget(self.typePanel)
        self.p1Panel = QtWidgets.QGroupBox(Dialog)
        self.p1Panel.setObjectName("p1Panel")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.p1Panel)
        self.verticalLayout_2.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.p1Exist = QtWidgets.QRadioButton(self.p1Panel)
        self.p1Exist.setObjectName("p1Exist")
        self.verticalLayout_2.addWidget(self.p1Exist)
        self.p1 = QtWidgets.QComboBox(self.p1Panel)
        self.p1.setEnabled(False)
        self.p1.setObjectName("p1")
        self.verticalLayout_2.addWidget(self.p1)
        self.p1Customize = QtWidgets.QRadioButton(self.p1Panel)
        self.p1Customize.setChecked(True)
        self.p1Customize.setObjectName("p1Customize")
        self.verticalLayout_2.addWidget(self.p1Customize)
        self.p1Layout = QtWidgets.QWidget(self.p1Panel)
        self.p1Layout.setObjectName("p1Layout")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.p1Layout)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_6 = QtWidgets.QLabel(self.p1Layout)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout.addWidget(self.label_6)
        self.x1 = QtWidgets.QDoubleSpinBox(self.p1Layout)
        self.x1.setMinimum(-99.99)
        self.x1.setObjectName("x1")
        self.horizontalLayout.addWidget(self.x1)
        self.label_7 = QtWidgets.QLabel(self.p1Layout)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout.addWidget(self.label_7)
        self.y1 = QtWidgets.QDoubleSpinBox(self.p1Layout)
        self.y1.setMinimum(-99.99)
        self.y1.setObjectName("y1")
        self.horizontalLayout.addWidget(self.y1)
        self.verticalLayout_2.addWidget(self.p1Layout)
        self.p1Result = QtWidgets.QRadioButton(self.p1Panel)
        self.p1Result.setObjectName("p1Result")
        self.verticalLayout_2.addWidget(self.p1Result)
        self.r1 = QtWidgets.QComboBox(self.p1Panel)
        self.r1.setEnabled(False)
        self.r1.setObjectName("r1")
        self.verticalLayout_2.addWidget(self.r1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 1, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.horizontalLayout_3.addWidget(self.p1Panel)
        self.p2Panel = QtWidgets.QGroupBox(Dialog)
        self.p2Panel.setObjectName("p2Panel")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.p2Panel)
        self.verticalLayout_6.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout_6.setSpacing(6)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.p2Exist = QtWidgets.QRadioButton(self.p2Panel)
        self.p2Exist.setObjectName("p2Exist")
        self.verticalLayout_6.addWidget(self.p2Exist)
        self.p2 = QtWidgets.QComboBox(self.p2Panel)
        self.p2.setEnabled(False)
        self.p2.setObjectName("p2")
        self.verticalLayout_6.addWidget(self.p2)
        self.p2Customize = QtWidgets.QRadioButton(self.p2Panel)
        self.p2Customize.setChecked(True)
        self.p2Customize.setObjectName("p2Customize")
        self.verticalLayout_6.addWidget(self.p2Customize)
        self.p2Layout = QtWidgets.QWidget(self.p2Panel)
        self.p2Layout.setObjectName("p2Layout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.p2Layout)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_10 = QtWidgets.QLabel(self.p2Layout)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_2.addWidget(self.label_10)
        self.x2 = QtWidgets.QDoubleSpinBox(self.p2Layout)
        self.x2.setMinimum(-99.99)
        self.x2.setObjectName("x2")
        self.horizontalLayout_2.addWidget(self.x2)
        self.label_11 = QtWidgets.QLabel(self.p2Layout)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_2.addWidget(self.label_11)
        self.y2 = QtWidgets.QDoubleSpinBox(self.p2Layout)
        self.y2.setMinimum(-99.99)
        self.y2.setObjectName("y2")
        self.horizontalLayout_2.addWidget(self.y2)
        self.verticalLayout_6.addWidget(self.p2Layout)
        self.p2Result = QtWidgets.QRadioButton(self.p2Panel)
        self.p2Result.setObjectName("p2Result")
        self.verticalLayout_6.addWidget(self.p2Result)
        self.r2 = QtWidgets.QComboBox(self.p2Panel)
        self.r2.setEnabled(False)
        self.r2.setObjectName("r2")
        self.verticalLayout_6.addWidget(self.r2)
        spacerItem2 = QtWidgets.QSpacerItem(20, 1, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem2)
        self.horizontalLayout_3.addWidget(self.p2Panel)
        self.p3Panel = QtWidgets.QGroupBox(Dialog)
        self.p3Panel.setEnabled(False)
        self.p3Panel.setObjectName("p3Panel")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.p3Panel)
        self.verticalLayout_8.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout_8.setSpacing(6)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.p3Exist = QtWidgets.QRadioButton(self.p3Panel)
        self.p3Exist.setObjectName("p3Exist")
        self.verticalLayout_8.addWidget(self.p3Exist)
        self.p3 = QtWidgets.QComboBox(self.p3Panel)
        self.p3.setEnabled(False)
        self.p3.setObjectName("p3")
        self.verticalLayout_8.addWidget(self.p3)
        self.p3Customize = QtWidgets.QRadioButton(self.p3Panel)
        self.p3Customize.setChecked(True)
        self.p3Customize.setObjectName("p3Customize")
        self.verticalLayout_8.addWidget(self.p3Customize)
        self.p3Layout = QtWidgets.QWidget(self.p3Panel)
        self.p3Layout.setObjectName("p3Layout")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.p3Layout)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_13 = QtWidgets.QLabel(self.p3Layout)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_5.addWidget(self.label_13)
        self.x3 = QtWidgets.QDoubleSpinBox(self.p3Layout)
        self.x3.setMinimum(-99.99)
        self.x3.setObjectName("x3")
        self.horizontalLayout_5.addWidget(self.x3)
        self.label_14 = QtWidgets.QLabel(self.p3Layout)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_5.addWidget(self.label_14)
        self.y3 = QtWidgets.QDoubleSpinBox(self.p3Layout)
        self.y3.setMinimum(-99.99)
        self.y3.setObjectName("y3")
        self.horizontalLayout_5.addWidget(self.y3)
        self.verticalLayout_8.addWidget(self.p3Layout)
        self.p3Result = QtWidgets.QRadioButton(self.p3Panel)
        self.p3Result.setObjectName("p3Result")
        self.verticalLayout_8.addWidget(self.p3Result)
        self.r3 = QtWidgets.QComboBox(self.p3Panel)
        self.r3.setEnabled(False)
        self.r3.setObjectName("r3")
        self.verticalLayout_8.addWidget(self.r3)
        spacerItem3 = QtWidgets.QSpacerItem(20, 1, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem3)
        self.horizontalLayout_3.addWidget(self.p3Panel)
        spacerItem4 = QtWidgets.QSpacerItem(1, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.verticalLayout_14.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.PreviewPanel = QtWidgets.QGroupBox(Dialog)
        self.PreviewPanel.setMinimumSize(QtCore.QSize(590, 0))
        self.PreviewPanel.setMaximumSize(QtCore.QSize(590, 16777215))
        self.PreviewPanel.setObjectName("PreviewPanel")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.PreviewPanel)
        self.verticalLayout_9.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout_9.setSpacing(6)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.tabWidget = QtWidgets.QTabWidget(self.PreviewPanel)
        self.tabWidget.setObjectName("tabWidget")
        self.Solving = QtWidgets.QWidget()
        self.Solving.setObjectName("Solving")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.Solving)
        self.verticalLayout_12.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.triangleImage = QtWidgets.QLabel(self.Solving)
        self.triangleImage.setText("")
        self.triangleImage.setObjectName("triangleImage")
        self.verticalLayout_12.addWidget(self.triangleImage)
        spacerItem5 = QtWidgets.QSpacerItem(20, 218, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_12.addItem(spacerItem5)
        self.tabWidget.addTab(self.Solving, "")
        self.Merge = QtWidgets.QWidget()
        self.Merge.setObjectName("Merge")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.Merge)
        self.verticalLayout_13.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.mergeImage = QtWidgets.QLabel(self.Merge)
        self.mergeImage.setText("")
        self.mergeImage.setObjectName("mergeImage")
        self.verticalLayout_13.addWidget(self.mergeImage)
        spacerItem6 = QtWidgets.QSpacerItem(20, 218, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_13.addItem(spacerItem6)
        self.tabWidget.addTab(self.Merge, "")
        self.verticalLayout_9.addWidget(self.tabWidget)
        self.horizontalLayout_4.addWidget(self.PreviewPanel)
        self.valuePanel = QtWidgets.QWidget(Dialog)
        self.valuePanel.setObjectName("valuePanel")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.valuePanel)
        self.verticalLayout_7.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout_7.setSpacing(6)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.len1Panel = QtWidgets.QGroupBox(self.valuePanel)
        self.len1Panel.setObjectName("len1Panel")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.len1Panel)
        self.verticalLayout.setObjectName("verticalLayout")
        self.len1 = QtWidgets.QDoubleSpinBox(self.len1Panel)
        self.len1.setMinimum(0.01)
        self.len1.setProperty("value", 10.0)
        self.len1.setObjectName("len1")
        self.verticalLayout.addWidget(self.len1)
        self.verticalLayout_7.addWidget(self.len1Panel)
        self.len2Panel = QtWidgets.QGroupBox(self.valuePanel)
        self.len2Panel.setEnabled(False)
        self.len2Panel.setObjectName("len2Panel")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.len2Panel)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.len2 = QtWidgets.QDoubleSpinBox(self.len2Panel)
        self.len2.setMinimum(0.01)
        self.len2.setProperty("value", 10.0)
        self.len2.setObjectName("len2")
        self.verticalLayout_5.addWidget(self.len2)
        self.verticalLayout_7.addWidget(self.len2Panel)
        self.anglePanel = QtWidgets.QGroupBox(self.valuePanel)
        self.anglePanel.setObjectName("anglePanel")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.anglePanel)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label = QtWidgets.QLabel(self.anglePanel)
        self.label.setObjectName("label")
        self.verticalLayout_4.addWidget(self.label)
        self.angle = QtWidgets.QDoubleSpinBox(self.anglePanel)
        self.angle.setMinimum(-360.0)
        self.angle.setMaximum(360.0)
        self.angle.setProperty("value", 30.0)
        self.angle.setObjectName("angle")
        self.verticalLayout_4.addWidget(self.angle)
        self.verticalLayout_7.addWidget(self.anglePanel)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem7)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.valuePanel)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonBox.sizePolicy().hasHeightForWidth())
        self.buttonBox.setSizePolicy(sizePolicy)
        self.buttonBox.setOrientation(QtCore.Qt.Vertical)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_7.addWidget(self.buttonBox)
        self.horizontalLayout_4.addWidget(self.valuePanel)
        self.verticalLayout_14.addLayout(self.horizontalLayout_4)

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        self.p1Exist.toggled['bool'].connect(self.p1.setEnabled)
        self.p1Customize.toggled['bool'].connect(self.p1Layout.setEnabled)
        self.p1Result.toggled['bool'].connect(self.r1.setEnabled)
        self.p2Exist.toggled['bool'].connect(self.p2.setEnabled)
        self.p2Customize.toggled['bool'].connect(self.p2Layout.setEnabled)
        self.p2Result.toggled['bool'].connect(self.r2.setEnabled)
        self.p3Exist.toggled['bool'].connect(self.p3.setEnabled)
        self.p3Customize.toggled['bool'].connect(self.p3Layout.setEnabled)
        self.p3Result.toggled['bool'].connect(self.r3.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Direction"))
        self.typeLayout.setTitle(_translate("Dialog", "Solving Type"))
        self.type.setItemText(0, _translate("Dialog", "PLAP"))
        self.type.setItemText(1, _translate("Dialog", "PLLP"))
        self.type.setItemText(2, _translate("Dialog", "PLPP"))
        self.mergeLayout.setTitle(_translate("Dialog", "Merge Type"))
        self.other.setToolTip(_translate("Dialog", "Let the triangle upside down."))
        self.other.setText(_translate("Dialog", "Reverse angle (?)"))
        self.p1Panel.setTitle(_translate("Dialog", "Point A"))
        self.p1Exist.setText(_translate("Dialog", "From Exist Point"))
        self.p1Customize.setText(_translate("Dialog", "Customize"))
        self.label_6.setText(_translate("Dialog", "x:"))
        self.label_7.setText(_translate("Dialog", "y:"))
        self.p1Result.setText(_translate("Dialog", "From Result"))
        self.p2Panel.setTitle(_translate("Dialog", "Point B"))
        self.p2Exist.setText(_translate("Dialog", "From Exist Point"))
        self.p2Customize.setText(_translate("Dialog", "Customize"))
        self.label_10.setText(_translate("Dialog", "x:"))
        self.label_11.setText(_translate("Dialog", "y:"))
        self.p2Result.setText(_translate("Dialog", "From Result"))
        self.p3Panel.setTitle(_translate("Dialog", "Point C"))
        self.p3Exist.setText(_translate("Dialog", "From Exist Point"))
        self.p3Customize.setText(_translate("Dialog", "Customize"))
        self.label_13.setText(_translate("Dialog", "x:"))
        self.label_14.setText(_translate("Dialog", "y:"))
        self.p3Result.setText(_translate("Dialog", "From Result"))
        self.PreviewPanel.setTitle(_translate("Dialog", "Preview"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Solving), _translate("Dialog", "Solving"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Merge), _translate("Dialog", "Merge"))
        self.len1Panel.setTitle(_translate("Dialog", "L0"))
        self.len2Panel.setTitle(_translate("Dialog", "R0"))
        self.anglePanel.setTitle(_translate("Dialog", "β"))
        self.label.setText(_translate("Dialog", "+ Clockwise"))
        self.angle.setSuffix(_translate("Dialog", "°"))

import icons_rc
import preview_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

