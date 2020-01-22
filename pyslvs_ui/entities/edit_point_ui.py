# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pyslvs_ui/entities/edit_point.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from qtpy import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(364, 596)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/bearing.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setSizeGripEnabled(True)
        Dialog.setModal(True)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(Dialog)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.name_label = QtWidgets.QLabel(Dialog)
        self.name_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.name_label.setObjectName("name_label")
        self.verticalLayout.addWidget(self.name_label)
        self.name_box = QtWidgets.QComboBox(Dialog)
        self.name_box.setObjectName("name_box")
        self.verticalLayout.addWidget(self.name_box)
        self.color_label = QtWidgets.QLabel(Dialog)
        self.color_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.color_label.setObjectName("color_label")
        self.verticalLayout.addWidget(self.color_label)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.color_box = QtWidgets.QComboBox(Dialog)
        self.color_box.setObjectName("color_box")
        self.horizontalLayout_2.addWidget(self.color_box)
        self.color_pick_button = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.color_pick_button.sizePolicy().hasHeightForWidth())
        self.color_pick_button.setSizePolicy(sizePolicy)
        self.color_pick_button.setObjectName("color_pick_button")
        self.horizontalLayout_2.addWidget(self.color_pick_button)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.type_box = QtWidgets.QComboBox(self.groupBox)
        self.type_box.setObjectName("type_box")
        self.type_box.addItem("")
        self.type_box.addItem("")
        self.type_box.addItem("")
        self.verticalLayout_3.addWidget(self.type_box)
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.angle_label = QtWidgets.QLabel(self.groupBox)
        self.angle_label.setObjectName("angle_label")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.angle_label)
        self.angle_box = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.angle_box.setMaximum(180.0)
        self.angle_box.setObjectName("angle_box")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.angle_box)
        self.verticalLayout_3.addLayout(self.formLayout_2)
        self.verticalLayout.addWidget(self.groupBox)
        self.pos_group = QtWidgets.QGroupBox(Dialog)
        self.pos_group.setObjectName("pos_group")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.pos_group)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.x_label = QtWidgets.QLabel(self.pos_group)
        self.x_label.setObjectName("x_label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.x_label)
        self.x_box = QtWidgets.QDoubleSpinBox(self.pos_group)
        self.x_box.setDecimals(4)
        self.x_box.setMinimum(-999999.0)
        self.x_box.setMaximum(999999.0)
        self.x_box.setObjectName("x_box")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.x_box)
        self.y_label = QtWidgets.QLabel(self.pos_group)
        self.y_label.setObjectName("y_label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.y_label)
        self.y_box = QtWidgets.QDoubleSpinBox(self.pos_group)
        self.y_box.setDecimals(4)
        self.y_box.setMinimum(-999999.0)
        self.y_box.setMaximum(999999.0)
        self.y_box.setObjectName("y_box")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.y_box)
        self.horizontalLayout_4.addLayout(self.formLayout)
        self.locate_option = QtWidgets.QPushButton(self.pos_group)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.locate_option.sizePolicy().hasHeightForWidth())
        self.locate_option.setSizePolicy(sizePolicy)
        self.locate_option.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/properties.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.locate_option.setIcon(icon1)
        self.locate_option.setIconSize(QtCore.QSize(30, 30))
        self.locate_option.setObjectName("locate_option")
        self.horizontalLayout_4.addWidget(self.locate_option)
        self.verticalLayout.addWidget(self.pos_group)
        self.links_label = QtWidgets.QLabel(Dialog)
        self.links_label.setObjectName("links_label")
        self.verticalLayout.addWidget(self.links_label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.no_selected = QtWidgets.QListWidget(Dialog)
        self.no_selected.setDragEnabled(True)
        self.no_selected.setDragDropMode(QtWidgets.QAbstractItemView.DragDrop)
        self.no_selected.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.no_selected.setObjectName("no_selected")
        self.horizontalLayout.addWidget(self.no_selected)
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.selected = QtWidgets.QListWidget(Dialog)
        self.selected.setDragEnabled(True)
        self.selected.setDragDropMode(QtWidgets.QAbstractItemView.DragDrop)
        self.selected.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.selected.setObjectName("selected")
        self.horizontalLayout.addWidget(self.selected)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_5.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.button_box = QtWidgets.QDialogButtonBox(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_box.sizePolicy().hasHeightForWidth())
        self.button_box.setSizePolicy(sizePolicy)
        self.button_box.setOrientation(QtCore.Qt.Vertical)
        self.button_box.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.button_box.setObjectName("button_box")
        self.verticalLayout_2.addWidget(self.button_box)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout_5.addLayout(self.verticalLayout_2)

        self.retranslateUi(Dialog)
        self.button_box.accepted.connect(Dialog.accept)
        self.button_box.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Point"))
        self.name_label.setText(_translate("Dialog", "Point Number"))
        self.color_label.setText(_translate("Dialog", "Color"))
        self.groupBox.setTitle(_translate("Dialog", "Type"))
        self.type_box.setItemText(0, _translate("Dialog", "R (pin)"))
        self.type_box.setItemText(1, _translate("Dialog", "P (slider block)"))
        self.type_box.setItemText(2, _translate("Dialog", "RP (pin in slot)"))
        self.angle_label.setText(_translate("Dialog", "Angle"))
        self.pos_group.setTitle(_translate("Dialog", "Position"))
        self.x_label.setText(_translate("Dialog", "X"))
        self.y_label.setText(_translate("Dialog", "Y"))
        self.links_label.setText(_translate("Dialog", "Links"))
        self.label_4.setText(_translate("Dialog", ">>"))
from pyslvs_ui import icons_rc
