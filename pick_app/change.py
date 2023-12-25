import sqlite3
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMessageBox, QPlainTextEdit
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem
from PyQt5.QtGui import QPixmap

class MyWidget_save_chanhe(QMainWindow):
    def __init__(self,root, **kwargs):
        super().__init__(root, **kwargs)
        self.current_image = None
        self.main = root

        uic.loadUi("1.ui", self)
        self.con = sqlite3.connect("squ.db")
        self.cur = self.con.cursor()
        self.tableWidget.itemChanged.connect(self.item_changed)
        self.pushButton_5.clicked.connect(self.zap_update_result)
        self.modified = {}
        self.titles = []

        self.pushButton.clicked.connect(self.MoreRicksForTheRickGod)
        self.pushButton_2.clicked.connect(self.crearDB)
        self.pushButton_6.clicked.connect(self.save_results)
        self.chet = -1

    #очищает БД полностью
    def crearDB(self):
        self.cur.execute('DROP TABLE users;')
        self.cur.execute('''CREATE TABLE IF NOT EXISTS users
                         (id INTEGER, name, status, species, type, gender, origin_name, origin_url, location_name, location_url, image)''')
        self.con.commit()
        self.zap_update_result()

    #Получает данные со строки и отправляет на получание информации по персонажу в pick_api.py
    def MoreRicksForTheRickGod(self):
        text = self.lineEdit.text()
        name_path = text.split(' ')
        next = []
        for i in name_path:
            next.append(int(i))
        self.main.RAM_Api.moreRickAndMorti(next)
        self.main.startData()
    #Происходит запись с БД в таблицу
    def zap_update_result(self):
        # Получили результат запроса, который ввели в текстовое поле
        result = self.cur.execute('SELECT * FROM users').fetchall()
        # Заполнили размеры таблицы
        #Устанавливаю количество строк в таблице
        self.tableWidget.setRowCount(len(result))
        # Если запись не нашлась, то не будем ничего делать
        if not result:
            self.statusBar().showMessage('Ничего не нашлось')
            return
        #Устанавливаем количество столбцов
        self.tableWidget.setColumnCount(len(result[0]))

        for i in range(len(self.cur.description)):
            self.titles.append(self.cur.description[i][0])
        # self.titles = [description[0] for description in cur.description]
        self.tableWidget.setHorizontalHeaderLabels(self.titles)

        # Заполнили таблицу полученными элементами
        for i, elem in enumerate(result):
            for j, val in enumerate(elem):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))
        self.modified = {}

    #Изменение в таблице документируются
    def item_changed(self, item):
        # Если значение в ячейке было изменено,
        # то в словарь записывается пара: название поля, новое значение
        q = len(self.modified)
        q +=1
        row = item.row()
        column = item.column()
        id = self.tableWidget.item(row, 0).text()

        self.modified["id"] = id
        self.modified[self.titles[item.column()]] = item.text()

    #По документу обновляется база данных
    def save_results(self):
        if self.modified:

            que = "UPDATE users SET\n"
            que += ", ".join([f"{key}='{self.modified.get(key)}'"
                              for key in self.modified.keys()])
            que += f" WHERE id = {self.modified['id']}"
            self.cur.execute(que)
            self.con.commit()
            self.modified.clear()