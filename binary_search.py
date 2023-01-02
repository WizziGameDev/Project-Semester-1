''' Binary Search '''
import os
os.system('cls')

''' Interative Search '''

# def interSearch(data_sorted = list, cari_data = int):
#     data_sorted.sort()
#     awal = 0
#     akhir = len(data_sorted) - 1
    
#     ''' Perulangan untuk mengecek setiap angka '''
#     while awal <= akhir:
#         # print(' Nilai awal sesudah penambahan mid = ', awal)
#         mid = awal + (akhir - awal) // 2
#         # print(' Nilai Mid = ',mid)
#         if data_sorted[mid] == cari_data: # Ketika nilai data tengah == data yang di cari maka mengembalikan nilai index nya
#             return mid
#         elif data_sorted[mid] < cari_data: # Ketika nilai data tengah < data yang di cari dan data belum sama maka akan menambah nilai dari awal
#             awal = mid + 1
#         else: # Jika kondisi sebelumnya belum terpenuhi makan bisa di katakan data_sorted[mid] < cari_data 
#             akhir = mid - 1 # maka akhir = mid - 1
#     return -1 # Jika data yang di cari tidak ada maka menghasilkan -1

# list_data = [20,49,39,4,3,2,40,33,55]
# # list_data.sort()
# # print(list_data)

# ''' Pemanggil '''
# print('',' ITERATIVE SEARCH '.center(40, '='))
# inputAngka = int(input(' Masukkan angka = '))
# result = interSearch(list_data, inputAngka)

# ''' Condition '''
# if result != -1:
#     print(f' Angka {inputAngka} terdapat di index ke-{result} setelah di urutkan')
# else:
#     print(f' Angka {inputAngka} tidak ada di dalam index list')

''' Recursive Search '''

# def recSearch(data, input_data, awal, akhir):
#     data = list(data)
#     data.sort()

#     data_list = list(data)
#     data_list.sort()
#     if akhir >= awal:
#         mid = awal + (akhir - awal) // 2
#         if data_list[mid] ==  input_data:
#             return f' Index ke-{mid}, terdapat list data angka {data_list[mid]}'
        
#         elif data_list[mid] > input_data:
#             return recSearch(data_list, input_data, awal, mid-1)
        
#         else:
#             return recSearch(data_list, input_data, mid+1, akhir)

#     else:
#         return -1

# list_data = [20,49,39,4,3,2,40,33,55]

# ''' Pemanggil '''
# print('',' RECURSIVE SEARCH '.center(40, '='))
# inputAngka = int(input(' Masukkan angka = '))
# keluaran_data = recSearch(list_data, inputAngka, 0, len(list_data)-1)

# if keluaran_data != -1:
#     print(keluaran_data)
# else:
#     print(' Data yang dicari tidak ditemukan')