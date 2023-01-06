''' Binary Search '''
import os
os.system('cls')

''' Interative Search '''

def interSearch(data = list, find_data = int):
    data.sort()
    low = 0
    high = len(data) - 1

    ''' Perulangan untuk mengecek setiap angka '''
    while low <= high:
        mid = low + (high - low) // 2
        if data[mid] == find_data:                  # Ketika nilai data tengah == data yang di cari maka mengembalikan nilai index nya
            return mid
        elif find_data > data[mid]:                 # Ketika nilai data tengah < data yang di cari dan data belum sama maka akan menambah nilai dari low
            low = mid + 1
        else:                                       # Jika kondisi sebelumnya belum terpenuhi makan bisa di katakan data_sorted[mid] < cari_data 
            high = mid - 1                          # maka high = mid - 1
    return -1                                       # Jika data yang di cari tidak ada maka menghasilkan -1

list_data = [20,49,39,4,3,2,40,33,55]

''' Pemanggil '''
print('',' ITERATIVE SEARCH '.center(40, '='))
inputAngka = int(input(' Masukkan angka = '))
result = interSearch(list_data, inputAngka)

''' Condition '''
if result != -1:
    print(f' Angka {inputAngka} terdapat di index ke-{result} setelah di urutkan')
else:
    print(f' Angka {inputAngka} tidak ada di dalam index list')

''' Recursive Search '''

def recSearch(data, input_data, low, high):
    data = list(data)
    data.sort()

    data_list = list(data)
    data_list.sort()
    if high >= low:
        mid = low + (high - low) // 2
        if data_list[mid] ==  input_data:
            return f' Index ke-{mid}, terdapat list data angka {data_list[mid]}'
        elif data_list[mid] > input_data:
            return recSearch(data_list, input_data, low, mid-1)
        else:
            return recSearch(data_list, input_data, mid+1, high)
    else:
        return -1

list_data = [20,49,39,4,3,2,40,33,55]

''' Pemanggil '''
print('',' RECURSIVE SEARCH '.center(40, '='))
inputAngka = int(input(' Masukkan angka = '))
keluaran_data = recSearch(list_data, inputAngka, 0, len(list_data)-1)

if keluaran_data != -1:
    print(keluaran_data)
else:
    print(' Data yang dicari tidak ditemukan')