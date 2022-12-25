''' Menghitung Gaji Karyawan Pada CSV '''

import os
import csv
os.system('cls')


dataListKaryawan = [] # ini yang akan di pakai
def dataKaryawan(data):
    ''' File csv Data Karyawan --> List'''
    with open(data) as data_file:
        # Pastikan pemisah data pada csv benar
        openCsv = csv.reader(data_file, delimiter=',')
        # Header
        kata = ' DATA KARYAWAN '
        print('', kata.center(81, '='))
        # Print setiap data
        for listKaryawanCSV in openCsv:
            # Kalau ingin menampilkan data Karyawan:
            print(f' | {listKaryawanCSV[0]:<4} {listKaryawanCSV[1]:<15} {listKaryawanCSV[2]:<20} {listKaryawanCSV[3]:<15} {listKaryawanCSV[4]:^19} |')
            dataListKaryawan.append(listKaryawanCSV)


dataListTunjangan = [] # ini yang akan di pakai
def dataTunjangan(data):
    ''' File csv Data Tunjangan --> List'''
    with open(data) as data_file:
        # Pastikan pemisah data pada csv benar
        openCsv = csv.reader(data_file, delimiter=',')
        # Header
        kata = ' DATA TUNJANGAN '
        print('',kata.center(58,'='))
        # print Setiap data
        for listTunjanganCSV in openCsv:
            # Kalau ingin menampilkan data Tunjangan:
            print(f' | {listTunjanganCSV[0]:4} {listTunjanganCSV[1]:<12} {listTunjanganCSV[2]:<15} {listTunjanganCSV[3]:<20} |')
            dataListTunjangan.append(listTunjanganCSV)


gajiListKaryawan = []
def hitungGaji():
    ''' Cek Data Karyawan '''
    for i in dataListKaryawan:
        namaKaryawan = i[1]
        if namaKaryawan in i:
            jabatanKaryawan = i[2]
            gajiPokok = i[3]
            gajiLembur = i[4]
            for j in dataListTunjangan:
                selectDataJabatan = j[1]
                if selectDataJabatan in jabatanKaryawan:
                    jabatanKaryawan = i[2]
                    gajiTunjangan = j[2]
                    upahLembur = j[3]
                    # Semua gaji di pindah ke list
                    gajiKeList = [namaKaryawan, gajiPokok, gajiTunjangan, gajiLembur, upahLembur]
                    gajiListKaryawan.append(gajiKeList)

    del gajiListKaryawan[0] # Ini saya hapus list ke-0 karena ada data Header
    for i in gajiListKaryawan:
        ''' Total Gaji Karyawan '''
        totalGajiKaryawan = int(i[1]) + int(i[2]) + (int(i[3]) * int(i[4]))
        ''' Print Total gaji masing" karyawan '''
        print(f'{i[0]:<9} dengan total gaji = Rp {totalGajiKaryawan}')


totalAkhir = []
def totalPengeluaranGaji():
    ''' Fungsi Total Akhir '''
    for i in gajiListKaryawan:
        gajiKeseluruhannya = int(i[1]) + int(i[2]) + (int(i[3]) * int(i[4])) 
        totalAkhir.append(gajiKeseluruhannya)
    pengeluaranPerusahaan = sum(totalAkhir)
    # Header
    kata = ' TOTAL GAJI KARYAWAN '
    print('\n',kata.center(54,'='))
    # Print Total Semua Gaji
    print(f'\n Total data gaji semua karyawan adalah = Rp {pengeluaranPerusahaan}\n')
    return pengeluaranPerusahaan


# Gaji Maksimal
def gajiMax():
    ''' Gaji Tertinggi '''
    del dataListKaryawan[0]  # Ini saya hapus list ke 0 karena ada data Header
    MAX = max(totalAkhir)
    data_count = 0
    for i in dataListKaryawan:
        i.append(totalAkhir[data_count])
        if 'Staf' in i[2]:
            if MAX in i:
                print(f' Gaji tertinggi = {i[1]:<7}, nominal = Rp {i[5]:<9}, dengan jabatan{i[2]}')
        data_count +=1

# Gaji Minimal
def gajiMin():
    ''' Gaji Terendah '''
    MIN = min(totalAkhir)
    data_count = 0
    for i in dataListKaryawan:
        i.append(totalAkhir[data_count])
        if 'Staf' in i[2]:
            if MIN in i:
                print(
                    f' Gaji terendah  = {i[1]:<7}, nominal = Rp {i[5]:<9}, dengan jabatan{i[2]}')
        data_count += 1
        


## csv file    
dataKaryawan('data_karyawan.csv') # Perhatikan letak folder/file data csv
print('')
dataTunjangan('data_tunjangan.csv')
print('')

print(' ====== GAJI TOTAL SETIAP KARYAWAN ====== \n')

hitungGaji() # Memanggil hitung Gaji Setiap Karyawan
totalPengeluaranGaji() # Memanggil Total gaji semua Karyawan

''' Pengeluaran Max and Min Staf'''
kata = ' GAJI TERTINGGI DAN TERENDAH OLEH PARA STAF '
print('',kata.center(77,'='))
print('')
gajiMax() # Mencari MAX gaji
gajiMin() # Mencari MIN gaji
