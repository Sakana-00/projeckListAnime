import os
import CRUD as CRUD
if __name__ == "__main__":
    system_os = os.name

    match system_os:
        case "ponix": os.system("clear")
        case "nt": os.system("cls")
    print("welcome to my List anime")
    print("Data base List anime")
    print("========================")
    CRUD.init_consol()

    while(True):

        match system_os:
            case "ponix": os.system("clear")
            case "nt": os.system("cls")

        print("welcome to my List anime")
        print("Data base List anime")
        print("========================")

        print(f"1.Read Data")
        print(f"2.Create Data")
        print(f"3.Update Data")
        print(f"4.Delete Data\n")

        user_option = input("masukan pilihan (number)")

        print("\n========================\n")

        match user_option:
            case "1": print("reading data")
            case "2": print("create data")
            case "3": print("update data")
            case "4": print("delete data")

        print("\n=========================\n")
        is_isdone = input("Apakah sudah selesai (y/n): ")
        if is_isdone == "y":
            break
print("Program end arigatoooou")
        

    
