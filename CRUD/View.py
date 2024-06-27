from . import Operasi

def creat_console():
    print("\n\n" + "="*100)
    print("#isi data anime\n")
    penulis = input("masukan nama penulis\t:")
    judul = input("masukan judul anime\t:")
    while(True):    
        try:
            tahun = int(input("masukan tahum\t:"))
            if len(str(tahun)) == 4:
                break
            else: 
                print("angka harus berjumlah 4")
        except:
            print("masukan angka bukan huruf, coba lagi")

    Operasi.creat(tahun,judul,penulis)
    print("\n#berikut adalah ata baru anda")
    read_console()

def read_console():
    data_file = Operasi.read()
    index = "No"
    judul = "Judul"
    penulis = "Penulis"
    tahun = "Tahun"

    #header
    print("\n"+"="*100)
    print(f"{index:4} | {judul:40} | {penulis:40} | {tahun:5}")
    print("-"*100)
    #data_base

    for index, data in enumerate(data_file):
        data_break = data.split(",")
        pk = data_break[0]
        date_add = data_break[1]
        judul = data_break[2]
        penulis = data_break[3]
        tahun= data_break[4]
        print(f"{index+1:4} | {judul:.40} | {penulis:.40} | {tahun:4}",end="")

    #footer
    print("="*100 + "\n")
