import sys
import sqlite3
import requests
from change import MyWidget_save_chanhe
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMessageBox, QPlainTextEdit, QPushButton
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem
from PyQt5.QtGui import QPixmap, QIcon, QImageReader
from PyQt5.QtCore import QSize
from pick_api import RickAndMortiAPI
from exceptc import *

class MyWidget_save(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MyWidget_save, self).__init__(*args, **kwargs)
        uic.loadUi("111.ui", self)
        #Подключение БД
        self.con = sqlite3.connect("squ.db")
        self.cur = self.con.cursor()
        self.chet = 0
        self.RAM_Api = RickAndMortiAPI()
        self.chg_res = MyWidget_save_chanhe(self)
        self.pushButton_3.clicked.connect(self.change_result)
        self.pushButton.clicked.connect(self.pervPict)
        self.pushButton_2.clicked.connect(self.nextPict)

        #Небольшой дизайн приложения

        self.setStyleSheet("#MainWindow {background-image: url(rik_and_morti.jpg);}")
        self.name.setStyleSheet("color: rgb(255, 255, 255);")
        self.id.setStyleSheet("color: rgb(255, 255, 255);")
        self.status.setStyleSheet("color: rgb(255, 255, 255);")
        self.race.setStyleSheet("color: rgb(255, 255, 255);")
        self.type.setStyleSheet("color: rgb(255, 255, 255);")
        self.gender.setStyleSheet("color: rgb(255, 255, 255);")
        self.origin_name.setStyleSheet("color: rgb(255, 255, 255);")
        self.local_name.setStyleSheet("color: rgb(255, 255, 255);")
        self.frame.setStyleSheet("background: #a8d7e1;"
                                 "width: 100%; "
                                 "height: 350px;")
        self.frame_2.setStyleSheet("background: #a8d7e1;"
                                 "width: 100%; "
                                 "height: 350px;")

        #Стартовые функции
        self.startData()
        self.nextPict()

    #Обновляем данные о значениях в базе данных(id)
    def startData(self):
        self.id_d = []
        self.getLen()
        er = self.cur.execute('SELECT * FROM users').fetchall()
        for i in er:
            self.id_d.append(i[0])

    #Подключаем форму для взаимодействия с БД
    def change_result(self):
        self.chg_res.show()

    #Получаем количество строк в БД
    def getLen(self):
        result = self.cur.execute('SELECT * FROM users').fetchall()

        self.len = len(result)

    #Получение данных для последующего добавления на страничку персонажей
    def getData(self):
        try:
            if self.chet == -1:
                self.chet = self.len - 1
            if len(self.id_d) == 0:
                self.startData()
                if len(self.id_d) == 0:
                    raise RecordIdTypeException
            row = [self.id_d[self.chet]]
            result = self.cur.execute('SELECT * FROM users WHERE id = ?', row).fetchall()
            if len(result) != 0:
                return result[0]
            else:
                self.RAM_Api.moreRickAndMorti(1)
                self.getData()
        except GetData as e:
            QMessageBox.warning(self, 'Error', e.message, QMessageBox.Ok)
        except RecordIdTypeException as e:
            self.RAM_Api.moreRickAndMorti(1)
            return self.getData()

    #Вызывает следующего персонажа в базе данных
    def nextPict(self):
        try:
            if self.chet < self.len - 1:
                self.chet += 1
            else:
                self.chet = 0

            data = self.getData()
            print(data)


            self.id.setText(str(data[0]))

            self.name.setText(data[1])

            self.status.setText(data[2])

            self.race.setText(data[3])

            self.type.setText(data[4])

            self.gender.setText(data[5])

            self.origin_name.setText(data[6])

            self.local_name.setText(data[8])
            url = data[-1]
            self.current_image = QPixmap(url)
            self.picture.setPixmap(self.current_image)
        except InvalidSettingsException as e:
            print(e.message)
        except TypeError as e:
            self.RAM_Api.moreRickAndMorti(1)
            self.nextPict()

    #Вызывает предыдущего персонажа
    def pervPict(self):
        try:
            if self.chet > -0.1:

             self.chet -= 1

            else:
                self.chet = self.len
            data = self.getData()

            self.id.setText(str(data[0]))

            self.name.setText(data[1])

            self.status.setText(data[2])

            self.race.setText(data[3])

            self.type.setText(data[4])

            self.gender.setText(data[5])

            self.origin_name.setText(data[6])


            self.local_name.setText(data[8])
            url = data[-1]
            self.current_image = QPixmap(url)
            self.picture.setPixmap(self.current_image)
        except Exception as e:
            print(f'Exception in pervPict: {e}')


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)

if __name__ == '__main__':
    sys.excepthook = except_hook
    app = QApplication(sys.argv)

    ex = MyWidget_save()

    ex.show()
    sys.exit(app.exec())
