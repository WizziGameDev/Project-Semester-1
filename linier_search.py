'''' Linear Search '''
import os
os.system('cls')

def linier_search(listKu = list, inputData = int):
    ''' Function Linear Search '''
    panjangList = len(listKu) #  nilai panjangList = 12
    count_data = 0
    for i in range(panjangList): # nilai i = 0 sampai 11
        if listKu[i] == inputData:
            print(f' Data {listKu[i]} ditemukan, ada di index ke {listKu.index(listKu[i])} dan urutan ke {i+1}')
            count_data += 1 # Jika kondisi ter eksekusi maka count_data += 1
    
    # Jika count_data tetap 0 maka eksekusi kode berikut
    if count_data == 0:
        print(f' Data {inputData} tidak ditemukan')
    
    print(f'\n Jumlah angka {inputData} adalah {count_data}')

data = [4,5,3,2,10,23,44,44,4,4,44,3]
print(' ======== Mencari data dengan linear search ======== \n')
cariData = int(input(' Masukkan data yang ingin dicari = '))
linier_search(data, cariData)