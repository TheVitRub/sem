import requests
import sqlite3
import os
from exceptc import *
class RickAndMortiAPI():
    def __init__(self):
        self.connection = sqlite3.connect("squ.db")
        self.cur = self.connection.cursor()
        self.responce = requests.get("https://rickandmortyapi.com/api/character").json()
        self.cur.execute('''CREATE TABLE IF NOT EXISTS users
                 (id INTEGER, name, status, species, type, gender, origin_name, origin_url, location_name, location_url, image)''')
        self.connection.commit()

    #Запрос на получение информации по новому персонажу по полученному ID
    def moreRickAndMorti(self, count):
        try:
            if type(count) != int:
                for i in count:
                    if i == 0 or i < 0:
                        raise NullExcept
            else:
                if count == 0 or count < 0:
                    raise NullExcept
            responce = requests.get(f"https://rickandmortyapi.com/api/character/{count}").json()
            if type(count) == type(1):
                i = responce
                url = i['image']
                p = requests.get(url)
                out = open(f"qwe/{i['id']}.png", "wb")
                out.write(p.content)
                out.close()
                in_db = []
                in_db.append(i['id'])
                in_db.append(i['name'])
                in_db.append(i['status'])
                in_db.append(i['species'])
                in_db.append(i['type'])
                in_db.append(i['gender'])
                in_db.append(i['origin']['name'])
                in_db.append(i['origin']['url'])
                in_db.append(i['location']['name'])
                in_db.append(i['location']['url'])
                in_db.append(f'qwe/{i["id"]}.png')
                self.cur.execute('INSERT INTO users VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', in_db)
                self.connection.commit()
            else:
                for i in responce:
                    url = i['image']
                    p = requests.get(url)
                    out = open(f"qwe/{i['id']}.png", "wb")
                    out.write(p.content)
                    out.close()
                    in_db = []
                    in_db.append(i['id'])
                    in_db.append(i['name'])
                    in_db.append(i['status'])
                    in_db.append(i['species'])
                    in_db.append(i['type'])
                    in_db.append(i['gender'])
                    in_db.append(i['origin']['name'])
                    in_db.append(i['origin']['url'])
                    in_db.append(i['location']['name'])
                    in_db.append(i['location']['url'])
                    in_db.append(f'qwe/{i["id"]}.png')

                    self.cur.execute('INSERT INTO users VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', in_db)
                    self.connection.commit()
        except NullExcept as e:
            print(f'{e.message}')

    #Проверяет на наличие папки, куда сохраняются фото персонажей
    def checkDirect(self):
        if os.path.isdir("qwe"):
            None
        else:
            os.mkdir("qwe")

    #Происходит запись данных в БД и скачивание фотографий
    def RickInBD(self):
        checkDirect()
        for i in self.responce['results']:
            url = i['image']
            p = requests.get(url)
            out = open(f"qwe/{i['id']}.png", "wb")
            out.write(p.content)
            out.close()
            in_db = []
            in_db.append(i['id'])
            in_db.append(i['name'])
            in_db.append(i['status'])
            in_db.append(i['species'])
            in_db.append(i['type'])
            in_db.append(i['gender'])
            in_db.append(i['origin']['name'])
            in_db.append(i['origin']['url'])
            in_db.append(i['location']['name'])
            in_db.append(i['location']['url'])
            in_db.append(f'qwe/{i["id"]}.png')
            self.cur.execute('INSERT INTO users VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', in_db)
            self.connection.commit()
