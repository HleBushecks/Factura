import os
import sys

from PyQt6 import QtGui
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import *

from evt_finish import finish


class Table(QMainWindow):
    def __init__(self, parent):
        super().__init__(parent)
        self.resize(1330, 500)

        with open('book.csv', 'r') as file:
            table = file.read()

        table = table.split('\n')
        y = 10
        for i in table:
            x = 10
            line = i.split(',')
            for ii in line:
                self.lbl = QLabel(self)
                self.lbl.setText(ii)
                self.lbl.setStyleSheet('border: 1px solid blue; color: white')
                self.lbl.move(x, y)
                x += 100
            y += 30


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        # self.setFixedSize(1275, 600)
        self.resize(1330, 500)
        self.setWindowTitle('Factura by HleBusheck')
        self.setWindowIcon(QtGui.QIcon('icons/factura.png'))

        self.txt_cpp = QTextEdit(self)
        self.txt_cpp.move(10, 10)
        self.txt_cpp.resize(120, 30)
        self.txt_cpp.setStyleSheet('border: 1px solid red; color: white;')
        self.txt_cpp.setPlaceholderText('Write ČPP')
        self.txt_cpp.resize(120, 30)

        self.btn_cpp = QPushButton(self)
        self.btn_cpp.move(140, 10)
        self.btn_cpp.setText('Add ČPP')
        self.btn_cpp.setStyleSheet("""
                        QPushButton {border: 1px solid green; color: white;}
                        QPushButton:hover {background-color: blue}
                        QPushButton:pressed {background-color: red}
                        """)
        self.btn_cpp.clicked.connect(self.evt_add_cpp)

        self.cls_csv = QPushButton(self)
        self.cls_csv.move(600, 10)
        self.cls_csv.resize(150, 30)
        self.cls_csv.setText('Clear CSV')
        self.cls_csv.setStyleSheet("""
                        QPushButton {border: 1px solid green; color: white;}
                        QPushButton:hover {background-color: blue}
                        QPushButton:pressed {background-color: red}
                        """)
        self.cls_csv.clicked.connect(self.evt_clear_csv)

        self.view_csv = QPushButton(self)
        self.view_csv.move(800, 10)
        self.view_csv.resize(150, 30)
        self.view_csv.setText('View CSV')
        self.view_csv.setStyleSheet("""
                        QPushButton {border: 1px solid green; color: white;}
                        QPushButton:hover {background-color: blue}
                        QPushButton:pressed {background-color: red}
                        """)
        self.view_csv.clicked.connect(self.evt_view_csv)

        self.btn_server = QPushButton(self)
        self.btn_server.move(1170, 10)
        self.btn_server.resize(150, 30)
        self.btn_server.setText('Start WEB Server')
        self.btn_server.setStyleSheet("""
                        QPushButton {border: 1px solid green; color: white;}
                        QPushButton:hover {background-color: blue}
                        QPushButton:pressed {background-color: red}
                        """)
        self.btn_server.clicked.connect(self.evt_start_stop_server)

        self.txt_name = QTextEdit(self)
        self.txt_name.move(10, 60)
        self.txt_name.setStyleSheet('border: 1px solid red; color: white;')
        self.txt_name.resize(120, 30)
        self.txt_name.setPlaceholderText('Name')

        self.btn_check = QPushButton(self)
        self.btn_check.move(150, 60)
        self.btn_check.setText('Check')
        self.btn_check.setStyleSheet("""
                        QPushButton {border: 1px solid green; color: white;}
                        QPushButton:hover {background-color: blue}
                        QPushButton:pressed {background-color: red}
                        """)
        self.btn_check.clicked.connect(self.evt_check)

        self.btn_next = QPushButton(self)
        self.btn_next.move(400, 60)
        self.btn_next.setText('Next')
        self.btn_next.setStyleSheet("""
                                QPushButton {border: 1px solid green; color: white;}
                                QPushButton:hover {background-color: blue}
                                QPushButton:pressed {background-color: red}
                                """)
        self.btn_next.clicked.connect(self.evt_next)

        self.btn_finish = QPushButton(self)
        self.btn_finish.move(520, 60)
        self.btn_finish.setText('Finish')
        self.btn_finish.setStyleSheet("""
                                        QPushButton {border: 1px solid green; color: white;}
                                        QPushButton:hover {background-color: blue}
                                        QPushButton:pressed {background-color: red}
                                        """)
        self.btn_finish.clicked.connect(self.evt_finish)

        self.btn_clear = QPushButton(self)
        self.btn_clear.move(280, 60)
        self.btn_clear.setText('Clear')
        self.btn_clear.setStyleSheet("""
                                                QPushButton {border: 1px solid green; color: white;}
                                                QPushButton:hover {background-color: blue}
                                                QPushButton:pressed {background-color: red}
                                                """)
        self.btn_clear.clicked.connect(self.evt_clear)

        self.array_of_dates = [QLabel(self) for _ in range(31)]
        self.array_of_cpp = [QComboBox(self) for _ in range(31)]
        self.array_of_hours = [QLineEdit(self) for _ in range(31)]

        x = 0
        y = 100
        for i in range(0, 31):
            if i % 7 == 0 and i != 0:
                y += 50
                x = 0
            self.array_of_dates[i].resize(30, 30)
            self.array_of_dates[i].setText(str(i + 1))
            self.array_of_dates[i].move(x, y)
            self.array_of_dates[i].setAlignment(Qt.AlignmentFlag.AlignCenter)
            self.array_of_dates[i].setStyleSheet('border: 1px solid red; color: white;')

            self.array_of_cpp[i].resize(120, 30)
            self.array_of_cpp[i].move(x + 30, y)
            self.array_of_cpp[i].setStyleSheet('border: 1px solid green; color: white;')

            self.array_of_hours[i].resize(30, 30)
            self.array_of_hours[i].move(x + 155, y)
            self.array_of_hours[i].setStyleSheet('border: 1px solid blue; color: white;')

            x += 190

        self.txt_area = QTextEdit(self)
        self.txt_area.move(10, 350)
        self.txt_area.resize(300, 100)
        self.txt_area.setStyleSheet('border: 1px solid green; color: white')

        self.factura = {}
        self.names_list = []

    def evt_start_stop_server(self):
        if "Start" in self.btn_server.text():
            os.system("service apache2 start")
            self.btn_server.setText('Stop WEB Server')
        else:
            os.system("service apache2 stop")
            self.btn_server.setText('Start WEB Server')

    def evt_add_cpp(self):
        for i in self.array_of_cpp:
            i.addItem(self.txt_cpp.toPlainText())

    def evt_clear_csv(self):
        with open('book.csv', 'w') as _:
            pass

    def evt_view_csv(self):
        Table(self).show()

    def evt_check(self):
        name = self.txt_name.toPlainText()
        for i in range(0, 31):
            self.array_of_cpp[i].setCurrentText(self.factura[name][i][0])
            if self.factura[name][i][1] == 0:
                self.array_of_hours[i].setText('')
            else:
                self.array_of_hours[i].setText(str(self.factura[name][i][1]))

    def evt_next(self):
        all_array = []
        if self.txt_name.toPlainText() not in self.names_list:
            self.names_list.append(self.txt_name.toPlainText())
            self.txt_area.append(self.txt_name.toPlainText())
        for i in (range(0, 31)):
            array = []
            array.append(self.array_of_cpp[i].currentText())
            hour = self.array_of_hours[i].text()
            if hour == '':
                array.append(0)
            else:
                try:
                    array.append(int(hour))
                except:
                    array.append(float(hour))
            all_array.append(array)
        self.factura[self.txt_name.toPlainText()] = all_array

    def evt_finish(self):
        finish(self.factura, self.names_list)

    def evt_clear(self):
        for i in self.array_of_hours:
            i.setText('')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
