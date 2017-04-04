# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/ahshoe/Desktop/Pyslvs-PyQt5/core/info/fileInfo.ui'
#
# Created by: PyQt5 UI code generator 5.8
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Info_Dialog(object):
    def setupUi(self, Info_Dialog):
        Info_Dialog.setObjectName("Info_Dialog")
        Info_Dialog.setEnabled(True)
        Info_Dialog.resize(500, 400)
        Info_Dialog.setMinimumSize(QtCore.QSize(351, 265))
        Info_Dialog.setMaximumSize(QtCore.QSize(500, 400))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/main.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Info_Dialog.setWindowIcon(icon)
        Info_Dialog.setAutoFillBackground(True)
        Info_Dialog.setSizeGripEnabled(True)
        Info_Dialog.setModal(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(Info_Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.fileName = QtWidgets.QLabel(Info_Dialog)
        self.fileName.setObjectName("fileName")
        self.verticalLayout.addWidget(self.fileName)
        self.line = QtWidgets.QFrame(Info_Dialog)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.authorName = QtWidgets.QLabel(Info_Dialog)
        self.authorName.setObjectName("authorName")
        self.verticalLayout.addWidget(self.authorName)
        self.descriptionText = QtWidgets.QTextBrowser(Info_Dialog)
        self.descriptionText.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.descriptionText.setTextInteractionFlags(QtCore.Qt.TextBrowserInteraction)
        self.descriptionText.setObjectName("descriptionText")
        self.verticalLayout.addWidget(self.descriptionText)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.closeButton = QtWidgets.QPushButton(Info_Dialog)
        self.closeButton.setDefault(True)
        self.closeButton.setObjectName("closeButton")
        self.horizontalLayout.addWidget(self.closeButton)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Info_Dialog)
        self.closeButton.clicked.connect(Info_Dialog.accept)
        QtCore.QMetaObject.connectSlotsByName(Info_Dialog)

    def retranslateUi(self, Info_Dialog):
        _translate = QtCore.QCoreApplication.translate
        Info_Dialog.setWindowTitle(_translate("Info_Dialog", "About this file"))
        self.fileName.setText(_translate("Info_Dialog", "File Name:"))
        self.authorName.setText(_translate("Info_Dialog", "Author:"))
        self.descriptionText.setHtml(_translate("Info_Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Sans Serif\'; font-size:9pt;\"><br /></p></body></html>"))
        self.closeButton.setText(_translate("Info_Dialog", "Close"))

import icons_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Info_Dialog = QtWidgets.QDialog()
    ui = Ui_Info_Dialog()
    ui.setupUi(Info_Dialog)
    Info_Dialog.show()
    sys.exit(app.exec_())

