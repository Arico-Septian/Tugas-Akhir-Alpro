def lihatData():
    print("------------------------------------------------------------")
    print("|><><><><><><><><><>< DAFTAR HANDPHONE ><><><><><><><><><><|")
    print("------------------------------------------------------------")
    data = zip(listMerek, listType, listHarga)
    print("| {:<5}| {:<15}| {:<15}| {:<16}|".format('No','Merk','Type','Harga'))
    print("------------------------------------------------------------")
    for index, v in enumerate(data):
        merek, type, harga = v
        print ("| {:<5}| {:<15}| {:<15}| {:<16}|".format( index+1, merek, type, harga))

my_file = open("NamaList.txt", "r")
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
        tambahData()
    elif menu == 2 :
        lihatData()
    elif menu == 3 :
        ubahData()
    elif menu == 4 :
        hapusData()
    else :
        break
    print("------------------------------------------------------------")