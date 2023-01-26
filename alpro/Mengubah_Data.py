listMerek = ["samsung", "oppo", "iphone"]
listType = ["Galaxy a20", "Reno 8", "Xr"]
listHarga = [2500000,3500000,4500000]

def ubahData(ubah, merek, type, harga):
    listMerek[ubah - 1] = merek
    listType[ubah - 1] = type
    listHarga[ubah - 1] = harga

listMenu = ["1.Menambah Data", "2.Menampilkan Data", "3.Mengubah Data" ,"4.Menghapus Data"]
while True :
    print("-----------------------")
    print("|    Daftar Menu Hp : |")
    print("-----------------------")
    for x in listMenu :
        print(x)
    print("-----------------------")
    print("|     Pilih Menu   :  |")
    print("-----------------------")
    menu =int(input())
    if menu == 1 :
        tambahData()
    elif menu == 2 :
        lihatData()
    elif menu == 3 :
        print("Data Yang Akan Diubah")
        ubah =int(input())
        print("Masukkan Merek :")
        merek =str(input())
        print("Masukkan Type Hp :")
        type =str(input())
        print("Masukkan Harga Hp :")
        harga =int(input())
        ubahData(ubah, merek, type, harga)
    elif menu == 4 :
        hapusData()
    else :
        break