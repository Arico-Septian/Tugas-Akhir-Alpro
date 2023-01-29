listMerek = ["samsung", "oppo", "iphone"]
listType = ["Galaxy a20", "Reno 8", "Xr"]
listHarga = [2500000,3500000,4500000]

def tambahData(merek, type,harga):
    listMerek.append(merek)
    listType.append(type)
    listHarga.append(harga)
    
    stringMerek = ",".join(listMerek)
    stringType = ",".join(listType)
    stringHarga = ",".join(str(x) for x in listHarga) #mengubah harga dari type int menjadi str dan menggabungkan str menggunakan koma
    my_file = open("NamaList.txt", "w")
    my_file.write(stringMerek + "\n") #\n untuk enter
    my_file.write(stringType + "\n")
    my_file.write(stringHarga)
    my_file.close()
    
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
    elif menu == 2 :
        lihatData()
    elif menu == 3 :
        ubahData()
    elif menu == 4 :
        hapusData()
    else :
        break
    print("------------------------------------------------------------")