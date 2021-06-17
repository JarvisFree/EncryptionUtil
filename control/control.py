#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time    ：2020/12/1 22:22
@Author  ：维斯
@File    ：control.py
@Version ：1.0
@Function：
"""

import sys

from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
from PyQt5 import QtCore

from model.jar_encryption_util import JarRandomUtil, JarEncryptionUtil
from view import Encryption_Ui


class Control(QMainWindow):
    def __init__(self, parent=None):
        super(QMainWindow, self).__init__(parent)
        self.ui = Encryption_Ui.Ui_MainWindow()  # test.Ui_Dialog() test：为ui文件转换后的python文件
        self.ui.setupUi(self)

    def get_random_salt(self):
        """
        加密-获取随机盐值 按钮
        """
        self.ui.lineEdit_encode_salt.setText(str(JarRandomUtil().random_int_str(6)))

    def encode(self):
        """
        加密-加密按钮
        """
        self.ui.listView_encode_miwen.setText('')
        salt = self.ui.lineEdit_encode_salt.text()
        if not salt.isdigit() or len(salt) != 6:
            QMessageBox.critical(self, '错误', '盐值需为六位数的数字')
            return None
        pro_text = self.ui.textEdit_encode_minwen.toPlainText()
        if pro_text is None or pro_text == '':
            QMessageBox.critical(self, '错误', '明文不能为空')
            return None
        print(pro_text)
        result, out_error = JarEncryptionUtil.encode_util(pro_text, int(salt))
        if out_error != '':
            QMessageBox.critical(self, '错误', out_error)
        self.ui.listView_encode_miwen.setText(result)

    def decode(self):
        """
        解密-解密按钮
        """
        self.ui.listView_decode_minwen.setText('')
        salt = self.ui.lineEdit_decode_salt.text()
        if not salt.isdigit() or len(salt) != 6:
            QMessageBox.critical(self, '错误', '盐值需为六位数的数字')
            return None
        mi_test = self.ui.textEdit_decode_miwen.toPlainText()
        if mi_test is None or mi_test == '':
            QMessageBox.critical(self, '错误', '密文不能为空')
            return None
        result, out_error = JarEncryptionUtil.decode_util(mi_test, int(salt))
        if out_error != '':
            QMessageBox.critical(self, '错误', out_error)
        self.ui.listView_decode_minwen.setText(result)

    @staticmethod
    def start():
        QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)  # 加上这句（运行后 与设计师里的一样）
        my_app = QApplication(sys.argv)
        my_dialog = Control()
        my_dialog.show()
        sys.exit(my_app.exec_())
