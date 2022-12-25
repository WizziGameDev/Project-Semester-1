''' Login System '''

import csv
import os

os.system('cls')

def readFile(namaFile):
    ''' Code Read File '''
    with open(namaFile) as fileCSV:  # membuka namaFile dengan menggunakan fungsi open()
        bacaCSV = csv.reader(fileCSV, delimiter=",")
        dataCSV = []
        for kolom in bacaCSV:
            dataCSV.append(kolom)
        fileCSV.close()
        return dataCSV


def login():
    ''' Login System '''
    namafile = "login.csv"
    status_login = False
    dataCSV = readFile(namafile)
    percobaan_login = 0
    while percobaan_login < 3:
        # Menginputkan username dan password jika login gagal akan mencoba login kembali
        user = input(" Username : ")
        pw = input(" Password : ")
        for kolom in dataCSV:
            if kolom[0] == user and kolom[1] == pw:
                status_login = True
                return status_login
        percobaan_login += 1
        print(" LOGIN GAGAL, percobaan login ke - ", percobaan_login)
    return status_login


def data_ikan():
    ''' Data Semua Ikan '''
    namafile = "data_ikan.csv"
    dataCSV = readFile(namafile)
    baris = 0
    for kolom in dataCSV:
        if baris > 0:
            print(f' {kolom[0]:<20}  -  {kolom[1]}')
        else:
            print(f' {kolom[0]:<20}  -  {kolom[1]}')
            baris += 1


def data_ikanku():
    ''' Jumlah Ikan Yang Di Ekspor '''
    namafile = "data_ikan.csv"
    dataCSV = readFile(namafile)
    line = 0
    jumlah = []
    for row in dataCSV:
        if (line > 0):
            jumlah.append(float(row[1]))
        else:
            line += 1
    print(f" Total ikan semua negara adalah {sum(jumlah)}  ton\n")


def kurang2000():
    ''' Code Total Ekspor Kurang dari 2000'''
    namafile = "data_ikan.csv"
    dataCSV = readFile(namafile)
    line = 0
    for row in dataCSV:
        if (line > 0):
            if float(row[1]) < 2000:
                print(f' Negara {row[0]:<15} dengan jumlah ekspor {row[1]:<7} ton')
        else:
            line += 1

def terbanyak():
    nameFile = "data_ikan.csv"
    dataCSV = readFile(nameFile)
    ''' Code Yang Paling Banyak'''
    # line = 0
    # jumlah = []
    # for row in dataCSV:
    #     if (line > 0):
    #         jumlah.append(float(row[1]))
    #     else:
    #         line += 1
    
    # nextLine = 0
    # MAX = max(jumlah)
    # for maxEkspor in dataCSV:
    #     if nextLine > 0:
    #         if float(maxEkspor[1]) == MAX:
    #             print(f' Negara dengan Ekspor paling banyak adalah {maxEkspor[0]} dengan jumlah{maxEkspor[1]} ton')
    #     else:
    #         nextLine += 1
    ''' Code Mengurutkan dari Yang Terbesar '''
    ## Mengurutkan data 
    del dataCSV[0]
    dataBaru = []
    for i in dataCSV:
        dataBaru.append([i[0], float(i[1])])
    
    # Mengurutkan dengan lambda dimana kita ambil item(list index) kemudian reverse
    # Dimana reverse ini digunakan untuk membalikkan sorted dari kecil -> besar
    listSorted = sorted(dataBaru, key=lambda item:item[1], reverse=True) 
    for i in listSorted:
        print(f' Negara {i[0]:<15} dengan total ekspor = {i[1]:<7} ton')


print(" ============== PROGRAM DIMULAI ===============")
print(" ======= Silahkan Login Terlebih Dahulu =======")
status_login = login()
if status_login:
    print("\n =============== LOGIN BERHASIL ===============")
    # jika login berhasil maka akan keluar list data kemudian memilih nomor untuk melihat data ekspor ikan
    print(
        " 1. Data ekspor ikan \n 2. Jumlah ekspor ikan \n 3. Negara pengekspor ikan dibawah 2000 ton \n 4. Negara pengekspor ikan paling tinggi")
    pilihan = int(input(" Pilih nomor untuk melihat data: "))
    # Pilihan 1 list daftar ekspor
    if pilihan == 1:
        print("\n ===== Data ekspor ikan pada tahun 2019 ======")
        print()
        data_ikan()
    # Pilihan 2 total ekspor
    elif pilihan == 2:
        print("\n ========= Total ekspor ikan pada tahun 2019 =========")
        print()
        data_ikanku()
    # Pilihan 3 ekspor kurang dari 2000
    elif pilihan == 3:
        print("\n ===== Negara pengekspor ikan kurang dari 2000 ton ===== ")
        print()
        kurang2000()
    # Pilihan 4 dari yang terbanyak
    elif pilihan == 4:
        print("\n ===== Negara ekspor ikan dari yang terbanyak ialah ===== ")
        print()
        terbanyak()

# jika login gagal maka program selesai
else:
    print(" =============== LOGIN GAGAL :) ===============")
    print(" ================ PROGRAM END =================")