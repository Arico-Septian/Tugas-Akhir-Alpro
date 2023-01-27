def lihatData():
    print("------------------------------------------------------------")
    print("|><><><><><><><><><>< DAFTAR HANDPHONE ><><><><><><><><><><|")
    print("------------------------------------------------------------")
    data = zip(listMerek, listType, listHarga)
    print ("| {:<5}| {:<15}| {:<15}| {:<16}|".format('No','Merk Handphone','Type Handphone','Harga Handphone'))
    print("------------------------------------------------------------")
    for index, v in enumerate(data):
        merek, type, harga = v
        print ("| {:<5}| {:<15}| {:<15}| {:<16}|".format( index+1, merek, type, harga))

def tambahData(merek, type,harga):
    listMerek.append(merek)
    listType.append(type)
    listHarga.append(harga)
    
def hapusData(hapus):
    listMerek.pop(hapus - 1)
    listType.pop(hapus - 1)
    listHarga.pop(hapus - 1)
    
def ubahData(ubah, merek, type, harga):
    listMerek[ubah - 1] = merek
    listType[ubah - 1] = type
    listHarga[ubah - 1] = harga
    
listMerek = ["samsung", "oppo", "iphone"]
listType = ["Galaxy a20", "Reno 8", "Xr"]
listHarga = [2500000,3500000,4500000]

listMenu = ["1.Menambah Data", "2.Menampilkan Data", "3.Mengubah Data" ,"4.Menghapus Data"]
while True :
    print("------------------------")
    print("|    Daftar Menu Hp :  |")
    print("------------------------")
    for x in listMenu :
        print(x)
    print("---------------------")
    print("|    Pilih Menu  :  |")
    print("---------------------")
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
        print("Data Yang Akan Diubah :")
        ubah =int(input())
        print("Masukkan Merek :")
        merek =str(input())
        print("Masukkan Type Hp :")
        type =str(input())
        print("Masukkan Harga Hp :")
        harga =int(input())
        ubahData(ubah, merek, type, harga)
    elif menu == 4 :
        print("Data Yang Akan Dihapus :")
        hapus =int(input())
        hapusData(hapus)
    else :
        break
    print("------------------------------------------------------------")