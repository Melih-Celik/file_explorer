import os
from time import sleep
from shutil import rmtree

def info():
    print("\n\t\tGuide\n1.Creating a new file -d\n2.Printing a file -r(Beta)\n3.Creating a new folder -k\
\n4.Deleting a folder -ks\t!!!FOLDER WILL BE DELETED PERMANENTLY!!!\n5.Deleting a file -ds \t!!!FILE WILL BE DELETED PERMANENTLY!!!\n6.Write 'exit' to close program\n")
def create_file(cwd):
    dosya_adi=input("Write name of file you want to create with its type : ")
    if dosya_adi =='exit':
        print("Process canceled.Leaving now.Please wait...")
        sleep(1.5)
    else:
        yeni_dosya=open("%s/%s"%(cwd,dosya_adi),"w")
        while True:
            yaz=input("Do you want to write in file you created :  [Y/N]  ")
            if yaz == "Y" or yaz== "Y":
                print("\n Write exit to close\nWrite you text : \n")
                while True:
                    icerik=input()
                    if icerik=="exit":
                        print("Saved succesfuly.Leaving now.Please wait...")
                        sleep(1.5)
                        break
                    else:
                        yeni_dosya.write(icerik+"\n")
                        continue
                yeni_dosya.close()
                break
            elif yaz == "N" or yaz== "n":
                pass
            else:
                print("Please write Y for Yes and N for No!!!")
                continue
        print("\n"*100)

def read_file(cwd):
    print("\n"*100)
    files_in_dir(cwd)
    file_read=int(input("\n(NO CHANGES AVAILABLE)\nChoose the file you want to read : "))
    if str(file_read)=="exit":
        print("Process canceled.Leaving now.Please wait...")
        sleep(1.5)
    else:
        file_to_read=open("%s"%(os.listdir(cwd)[file_read-1]),"r")
        for a in file_to_read: print(a)
        while True:
            exitis=input("\n\nWrite 'exit' to leave : ")
            if exitis=="exit":
                break
            else:
                print("Wrong input...\n")
                continue
def remove_file(cwd):
    print("\n"*100)
    files_in_dir(cwd)
    file_del=input("Choose the file you want to remove : ")
    if file_del=="exit":
        print("Process canceled.Leaving now.Please wait...")
        sleep(1.5)
    else:
        try:
            while True:
                secim=input("Do you really want to delete file permanently : [Y/N]  ")
                if secim.upper() =="Y":
                    file_del=int(file_del)
                    os.remove("%s/%s"%(cwd,os.listdir(cwd)[file_del-1]))
                    print("Succesfuly done.Please wait...")
                    sleep(1)
                    break
                elif secim.upper() =="N":
                    break
                else:
                    print("Please write Y for Yes and N for No!!!")
                    continue
        except PermissionError:
            print("Have no permission to delete this file! (Open program again with administrator permission)\nPlease Wait...")
            sleep(3)
def create_dir(cwd):
    crt_dir=input("Write name of the folder you want to create : ")
    if crt_dir=="exit":
        print("Process canceled.Leaving now.Please wait...")
        sleep(1.5)
    else:
        os.mkdir("%s/%s"%(cwd,crt_dir))
        os.chdir("%s/%s"%(cwd,crt_dir))
        print("Succesfuly done.Please wait...")
        sleep(1)

def remove_dir(cwd):
    print("\n"*100)
    files_in_dir(cwd)
    dir_del=input("Choose the folder you want to remove : ")
    if dir_del=="exit":
        print("Process canceled.Leaving now.Please wait...")
        sleep(1.5)
    else:
        try:
            while True:
                secim=input("Do you really want to remove folder and its items permanently : [Y/N]")
                if secim.upper()=="Y":
                    dir_del=int(dir_del)
                    rmtree("%s/%s"%(cwd,os.listdir(cwd)[dir_del-1]))
                    print("Succesfuly done.Please wait...")
                    sleep(1)
                    break
                elif secim.upper() =="N":
                    break
                else:
                    print("Please write Y for Yes and N for No!!!")
                    continue
        except PermissionError:
            print("Have no permission to delete this folder! (Open program again with administrator permission)\nPlease Wait...")
            sleep(3)
def files_in_dir(cwd):
    try:
        print("-1.Parent directory")
        n=1
        for a in os.listdir(cwd):
            print(n,a)
            n=n+1
    except PermissionError:
        print("Have no permission to enter this folder! (Open program again with administrator permission)\nPlease Wait...")
            
def pick_dir(cwd):
    while True:
        try:
            new_way=input("Type a command : ")
            if new_way == "-1":
                os.chdir(os.pardir)
                break
            elif new_way.isdigit():
                new_way=int(new_way)
                os.chdir("%s/%s"%(cwd,os.listdir(cwd)[new_way-1]))
                break
            elif new_way == "-i":
                info()
            elif new_way == "-d":
                create_file(cwd)
                break
            elif new_way == "-r":
                read_file(cwd)
                break
            elif new_way == "-k":
                create_dir(cwd)
                break
            elif new_way == "-ks":
                remove_dir(cwd)
                break
            elif new_way == "-ds":
                remove_file(cwd)
                break
            elif new_way == "exit":
                exit()
            else:
                print("Wrong input!")
        except (FileNotFoundError,TypeError,ValueError,IndexError):
            print("\nWrong command !")
        except NotADirectoryError:
            print("This is not a folder!!!")

while True:
    print("\nType -i to see the guide...\n")
    cwd=os.getcwd()
    print("Current directory : \n%s\n"%(cwd))
    files_in_dir(cwd)
    pick_dir(cwd)
    print("\n"*100)
    continue
