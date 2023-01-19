listMerek = ["samsung", "oppo", "iphone"]
listType = ["Galaxy a20", "Reno 8", "Xr"]
listHarga = [2500000,3500000,4500000]

def tambahData(merek, type,harga):
    listMerek.append(merek)
    listType.append(type)
    listHarga.append(harga)
    
listMenu = ["1.Menambah Data", "2.Menampilkan Data", "3.Mengubah Data" ,"4.Menghapus Data"]
while True :
    print("Daftar Menu :")
    for x in listMenu :
        print(x)
    print("Pilih Menu :")
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