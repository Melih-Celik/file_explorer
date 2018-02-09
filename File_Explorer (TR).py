import os
from time import sleep
from shutil import rmtree

def info():
    print("\n\t\tİşlem Rehberi\n1.Yeni dosya oluşturmak için -d\n2.Dosya içeriğini ekrana yazdırmak için -r(Beta)\n3.Yeni Klasör oluşturmak için -k\
\n4.Klasör silmek için -ks\t!!!Klasör kalıcı olarak silinir!!!\n5.Dosya silmek için -ds \t!!!Dosya kalıcı olarak silinir!!!\n6.Çıkmak için 'cik' yazınız...\n")
def create_file(cwd):
    dosya_adi=input("Oluşuturacağınız dosyanın adını uzantısıyla beraber yazınız : ")
    if dosya_adi =='cik':
        print("İşlem iptal edildi.Çıkılıyor.Lütfen bekleyin...")
        sleep(1.5)
    else:
        yeni_dosya=open("%s/%s"%(cwd,dosya_adi),"w")
        while True:
            yaz=input("Dosyanıza içerik yazmak ister misiniz :  [E/H]  ")
            if yaz == "E" or yaz== "e":
                print("\n Çıkmak için 'cik' yazın\nMetninizi giriniz : \n")
                while True:
                    icerik=input()
                    if icerik=="cik":
                        print("Başarıyla kaydedildi.Çıkılıyor.Lütfen bekleyin...")
                        sleep(1.5)
                        break
                    else:
                        yeni_dosya.write(icerik+"\n")
                        continue
                yeni_dosya.close()
                break
            elif yaz == "H" or yaz== "h":
                pass
            else:
                print("Lütfen Evet için E Hayır için H yazınız !!!")
                continue
        print("\n"*100)

def read_file(cwd):
    print("\n"*100)
    files_in_dir(cwd)
    file_read=int(input("\n(Dosyada değişikilik yapılamaz)\nOkunacak dosyayı seçiniz : "))
    if str(file_read)=="cik":
        print("İşlem iptal edildi.Çıkılıyor.Lütfen bekleyin...")
        sleep(1.5)
    else:
        file_to_read=open("%s"%(os.listdir(cwd)[file_read-1]),"r")
        for a in file_to_read: print(a)
        while True:
            cikis=input("\n\nCikmak icin 'cik' yazın : ")
            if cikis=="cik":
                break
            else:
                print("Yanlış giriş yaptınız...\n")
                continue
def remove_file(cwd):
    print("\n"*100)
    files_in_dir(cwd)
    file_del=input("Silinecek dosyayı seçiniz : ")
    if file_del=="cik":
        print("İşlem iptal edildi.Çıkılıyor.Lütfen bekleyin...")
        sleep(1.5)
    else:
        try:
            while True:
                secim=input("Dosyayı kalıcı olarak silmek istediğinize emin misiniz : [E/H]  ")
                if secim.upper() =="E":
                    file_del=int(file_del)
                    os.remove("%s/%s"%(cwd,os.listdir(cwd)[file_del-1]))
                    print("İşlem başarılı.Lütfen bekleyin...")
                    sleep(1)
                    break
                elif secim.upper() =="H":
                    break
                else:
                    print("Lütfen Evet için E Hayır için H yazınız !!!")
                    continue
        except PermissionError:
            print("Klasör silme erişiminiz yok! (Programı yönetici olarak açmayı deneyin)\nLütfen Bekleyin...")
            sleep(3)
def create_dir(cwd):
    crt_dir=input("Oluşturmak istediğiniz klasörün adını giriniz : ")
    if crt_dir=="cik":
        print("İşlem iptal edildi.Çıkılıyor.Lütfen bekleyin...")
        sleep(1.5)
    else:
        os.mkdir("%s/%s"%(cwd,crt_dir))
        os.chdir("%s/%s"%(cwd,crt_dir))
        print("İşlem başarılı.Lütfen bekleyin...")
        sleep(1)

def remove_dir(cwd):
    print("\n"*100)
    files_in_dir(cwd)
    dir_del=input("Silinecek klasörü seçiniz : ")
    if dir_del=="cik":
        print("İşlem iptal edildi.Çıkılıyor.Lütfen bekleyin...")
        sleep(1.5)
    else:
        try:
            while True:
                secim=input("Klasörü ve içindekileri kalıcı olarak silmek istediğinize emin misiniz : [E/H]")
                if secim.upper()=="E":
                    dir_del=int(dir_del)
                    rmtree("%s/%s"%(cwd,os.listdir(cwd)[dir_del-1]))
                    print("İşlem başarılı.Lütfen bekleyin...")
                    sleep(1)
                    break
                elif secim.upper() =="H":
                    break
                else:
                    print("Lütfen Evet için E Hayır için H yazınız !!!")
                    continue
        except PermissionError:
            print("Dizin silme erişiminiz yok! (Programı yönetici olarak açmayı deneyin)\nLütfen Bekleyin...")
            sleep(3)
def files_in_dir(cwd):
    try:
        print("-1.Geri gel")
        n=1
        for a in os.listdir(cwd):
            print(n,a)
            n=n+1
    except PermissionError:
        print("Bu dizine giriş izniniz yok! (Programı yönetici olarak açmayı deneyin)\nGeri gelin.")
            
def pick_dir(cwd):
    while True:
        try:
            new_way=input("Bir işlem yapınız : ")
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
            elif new_way == "cik":
                exit()
            else:
                print("Geçersiz bir işlem yaptınız!")
        except (FileNotFoundError,TypeError,ValueError,IndexError):
            print("\nYanlış bir işlem yaptınız !")
        except NotADirectoryError:
            print("Bu bir dizin değil!!!")

while True:
    print("\nSeçenekleri görmek için -i yazınız...\n")
    cwd=os.getcwd()
    print("Bulunduğunuz dizin : \n%s\n"%(cwd))
    files_in_dir(cwd)
    pick_dir(cwd)
    print("\n"*100)
    continue
