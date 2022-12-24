data_nested = [['1', ' Abdullah', ' Direktur', ' 10000000', ' 10'], [
    '2', ' Budi', ' Manajer Pemasaran', ' 10000000', ' 5'], ['3', ' Tono', ' Manajer Keuangan', ' 8000000', ' 10']]

data_list = [16500000, 12500000, 11000000]

data_count = 0
for i in data_nested:
    i.append(data_list[data_count])
    print(i)
    data_count +=1
    

    # data_kelist = data_list[i]
    # print(data_nested[i].append(data_kelist))


# import csv
# ''' Open File '''

# with open('../pembelajaran/tugas_file/Cobain.csv') as csv_file:
#     read_csv = csv.reader(csv_file, delimiter=';')
#     for i in read_csv:
#         print(int(i[2]))

''' Gaji Karyawan ----- '''
# gajiTotalKaryawan = int(GajiKaryawan[1]) + (GajiKaryawan[2])
# print(f'{gaji}')
# for i in dataListKaryawan:
#     selectDataKaryawan = i[1]
#     if name in selectDataKaryawan:
#         jabatanKaryawan = i[2]
#         gajiPokok = i[3]
#         gajiLembur = i[4]

#         ''' Cek Gaji Tunjangan '''
#         for j in dataListTunjangan:
#             selectDataJabatan = j[1]
#             # print(selectDataJabatan) ## Bisa di coba isinya apa aja
#             if selectDataJabatan in jabatanKaryawan: # jika data di jabatan(tunjangan) ada di jabatan karyawan maka
#                 gajiTunjangan = j[2]
#                 upahLembur = j[3]

# ''' Menghitung Gaji Total Karyawan '''
# gajiTotal = int(gajiPokok) + int(gajiTunjangan) + (int(gajiLembur) * int(upahLembur))
# return gajiTotal

''' Hitung Direct ----- '''
   # for i in dataListKaryawan:
#     namaKaryawan = i[1]
#     if namaKaryawan in i:
#         jabatanKaryawan = i[2]
#         gajiPokok = i[3]
#         gajiLembur = i[4]
#         for j in dataListTunjangan:
#             selectDataJabatan = j[1]
#             if selectDataJabatan in jabatanKaryawan:
#                 jabatanKaryawan = i[2]
#                 gajiTunjangan = j[2]
#                 upahLembur = j[3]
#                 # Semua gaji di pindah ke list
#                 global gajiKeList
#                 gajiKeList = [gajiPokok, gajiTunjangan, gajiLembur, upahLembur]
#                 TotalSemuaGaji.append(gajiKeList)

# Akhir -> di hapus deskripsinnya
