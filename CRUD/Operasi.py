from time import time
from . import  Database
from .Util import random_string
import time

def creat_first_data():

        penulis = input("penulis: ")
        judul = input("judul: ")
        tahun = input("tahun: ")

        data = Database.TEMPLATE.copy()

        data["pk"] = random_string(6)
        data["date_time"] = time.strftime("%Y-%m-%d-%H-%M-%S%z",time.gmtime())
        data["penulis"] = penulis + Database.TEMPLATE["penulis"][len(penulis):]
        data["judul"] = judul + Database.TEMPLATE["judul"][len(judul):]
        data["tahun"] = tahun

        data_str = f'{data["pk"]},{ data["date_time"]},{ data["penulis"]},{data["judul"]},{data["tahun"]}\n'
        print(data_str)
        try:
            with open(Database.DB_NAME, "w", encoding="utf-8") as file:
                file.write(data_str)
        except: 
            print("udah lah gagal bos")
def read():

        try: 
             with open(Database.DB_NAME, "r") as file:
                  content = file.readlines()
                  return content
        except:
             print("membaca data base error")
             return False

       