listMerek = ["samsung", "oppo", "iphone"]
listType = ["Galaxy a20", "Reno 8", "Xr"]
listHarga = [2500000,3500000,4500000]

def lihatData():
    print("-----------------------------------------------")
    print("|                  Daftar HP                  |")
    print("-----------------------------------------------")
    data = zip(listMerek, listType, listHarga)
    print ("{:<5} {:<15} {:<15} {:<10}".format('No','Merk','Type','Harga'))
    for index, v in enumerate(data):
        merek, type, harga = v
        print ("{:<5} {:<15} {:<15} {:<10}".format( index+1, merek, type, harga))

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
        ubahData()
    elif menu == 4 :
        hapusData()
    else :
        break