listMerek = ["samsung", "oppo", "iphone"]
listType = ["Galaxy a20", "Reno 8", "Xr"]
listHarga = [2500000,3500000,4500000]
  
def hapusData(hapus):
    listMerek.pop(hapus - 1)
    listType.pop(hapus - 1)
    listHarga.pop(hapus - 1)
    
listMenu = ["1.Menambah Data", "2.Menampilkan Data", "3.Mengubah Data" ,"4.Menghapus Data"]
while True :
    print("Daftar Menu :")
    for x in listMenu :
        print(x)
    print("Pilih Menu :")
    menu =int(input())
    if menu == 1 :
        tambahData()
    elif menu == 2 :
        lihatData()
    elif menu == 3 :
        ubahData()
    elif menu == 4 :
        print("Data Yang Akan Dihapus")
        hapus =int(input())
        hapusData(hapus)
    else :
        break