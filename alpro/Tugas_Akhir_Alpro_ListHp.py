# Fungsi untuk melihat data
def lihatData():
    print("------------------------------------------------------------")
    print("|><><><><><><><><><>< DAFTAR HANDPHONE ><><><><><><><><><><|")
    print("------------------------------------------------------------")
    data = zip(listMerek, listType, listHarga) #zip untuk menggabungkan menjadi 1 list
    print("| {:<5}| {:<15}| {:<15}| {:<16}|".format('No','Merk Handphone','Type Handphone','Harga Handphone'))
    print("------------------------------------------------------------")
    for index, v in enumerate(data): #enumerate untuk mendapatkan index dari list data
        merek, type, harga = v
        print ("| {:<5}| {:<15}| {:<15}| {:<16}|".format( index+1, merek, type, harga))

#Fungsi untuk menambah data
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

#Fungsi untuk menghapus data
def hapusData(hapus):
    listMerek.pop(hapus - 1) #-1 karena index dimulai dari 0
    listType.pop(hapus - 1)
    listHarga.pop(hapus - 1)
    
    stringMerek = ",".join(listMerek)
    stringType = ",".join(listType)
    stringHarga = ",".join(str(x) for x in listHarga) #mengubah harga dari type int menjadi str dan menggabungkan str menggunakan koma
    
    my_file = open("NamaList.txt", "w") #w untuk membuka txt dengan fungsi write pada file
    my_file.write(stringMerek + "\n")
    my_file.write(stringType + "\n")
    my_file.write(stringHarga)
    my_file.close()

#Fungsi untuk mengubah data 
def ubahData(ubah, merek, type, harga):
    listMerek[ubah - 1] = merek 
    listType[ubah - 1] = type   #-1 karena index dimulai dari 0
    listHarga[ubah - 1] = harga
    
    stringMerek = ",".join(listMerek)
    stringType = ",".join(listType)
    stringHarga = ",".join(str(x) for x in listHarga) #mengubah harga dari type int menjadi str dan menggabungkan str menggunakan koma
    
    my_file = open("NamaList.txt", "w") #w untuk membuka txt dengan fungsi write pada file
    my_file.write(stringMerek + "\n")
    my_file.write(stringType + "\n")
    my_file.write(stringHarga)
    my_file.close()

#Program untuk membuka file txt
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

listMenu = ["1.Menambah Data", "2.Menampilkan Data", "3.Mengubah Data" ,"4.Menghapus Data","0.Keluar dari program"]

while True :
    print("-----------------------")
    print("| Daftar Menu Utama : |")
    print("-----------------------")
    for x in listMenu :
        print(x)
    print("----------------------")
    print("| Pilih Menu Utama : |")
    print("----------------------")
    menu =int(input())
    
    if menu == 1 :
        print("Masukkan Merek Handphone :")
        merek =str(input())
        print("Masukkan Type Handphone :")
        type =str(input())
        print("Masukkan Harga Handphone :")
        harga =int(input())
        tambahData(merek, type, harga)
        lihatData()    
    elif menu == 2 :
        lihatData()    
    elif menu == 3 :
        print("Data Handphone Yang Akan Diubah :")
        ubah =int(input())    
        if ubah <=len(listMerek) :
            print("Masukkan Merek Handphone :")
            merek =str(input())
            print("Masukkan Type Handphone :")
            type =str(input())
            print("Masukkan Harga Handphone :")
            harga =int(input())
            ubahData(ubah, merek, type, harga)
            lihatData()    
        else :
            print ("Data Yang Anda Masukkan Tidak Sesuai :(")    
    elif menu == 4 :
        print("Pilih Data Handphone Yang Akan Dihapus :")
        hapus =int(input())    
        if hapus <=len(listMerek) :    
            hapusData(hapus)
            lihatData()    
        else :
            print("Data Yang Anda Masukkan Tidak Sesuai :(")    
    elif menu == 0 :
        break    
    else :
        break
    print("------------------------------------------------------------")