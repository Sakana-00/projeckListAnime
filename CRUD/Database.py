from . import Operasi

DB_NAME = "data.txt"
TEMPLATE = {
    "pk":"XXXXXX",
    "date_add":"yyyy-mm-dd",
    "judul":255*" ",
    "penulis":255*" ",
    "tahun":"yyyy"

}


def init_consol():
    try: 
        with open(DB_NAME,"r") as file:
            print("database tersedia, init done")
    except: 
        print("database tidak tersedia, membuat database baru")
        Operasi.creat_first_data()