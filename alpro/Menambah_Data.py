def tambahData(merek, type,harga):
    listMerek.append(merek)
    listType.append(type)
    listHarga.append(harga)
    
    stringMerek = ",".join(listMerek)
    stringType = ",".join(listType)
    stringHarga = ",".join(str(x) for x in listHarga) #mengubah harga dari type int menjadi str dan menggabungkan str menggunakan koma
    my_file = open("NamaList.txt", "w") #w untuk membuka txt dengan fungsi write pada file
    my_file.write(stringMerek + "\n") #\n untuk enter
    my_file.write(stringType + "\n")
    my_file.write(stringHarga)
    my_file.close()
    
my_file = open("NamaList.txt", "r") #r untuk membaca file txt
count = 0

listMerek = []
listType = []
listHarga = []

while True:
    count += 1  
    data = my_file.readline()
    if not data:
        break
    if count == 1 :
        listMerek = data.rstrip().split(",")
    elif count == 2 :
        listType = data.rstrip().split(",")
    elif count == 3 :
        listHarga = data.rstrip().split(",")
    
listMenu = ["1.Menambah Data", "2.Menampilkan Data", "3.Mengubah Data" ,"4.Menghapus Data"]
while True :
    print("------------------------")
    print("|    Daftar Menu Hp :  |")
    print("------------------------")
    for x in listMenu :
        print(x)
    print("----------------------")
    print("|    Pilih Menu   :  |")
    print("----------------------")
    menu =int(input())
    if menu == 1 :
        print("Masukkan Merek :")
        merek =str(input())
        print("Masukkan Type HP :")
        type =str(input())
        print("Masukkan Harga Hp :")
        harga =int(input())
        tambahData(merek, type, harga)
        lihatData()
    elif menu == 2 :
        lihatData()
    elif menu == 3 :
        ubahData()
    elif menu == 4 :
        hapusData()
    else :
        break
    print("------------------------------------------------------------")