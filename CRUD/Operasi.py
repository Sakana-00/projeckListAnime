from . import  Database
from .Util import random_string
import time

def creat_first_data():

        penulis = input("penulis: ")
        judul = input("judul: ")
        tahun = input("tahun: ")

        data = Database.TEMPLATE.copy()
        data["pk"] = random_string(6)
        data["date_time"] = time.strftime("%Y-%m-%d-%H-%M-%Sz", time.gmtime())
        
        print(data["date_time"])
        tahun = input("tahun: ")