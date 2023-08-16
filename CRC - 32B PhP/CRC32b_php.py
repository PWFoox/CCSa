import os
import time
import binascii
import csv
import subprocess

# Функция для вычисления CRC-32
def calculate_crc32(data):
    crc = binascii.crc32(data.encode()) & 0xffffffff
    return crc

start = True
while start:
    data = input("Введите информацию для хеширования: ")
    hash_dec = calculate_crc32(data)
    hash_hex = hex(hash_dec)[2:]  # Получаем шестнадцатеричное представление, удаляем префикс "0x"
    
    print("Исходная информация:", data)
    time.sleep(0.5)
    print("Хеш-значение CRC-32 в десятичной системе:", hash_dec)
    time.sleep(0.5)
    print("Хеш-значение CRC-32 в шестнадцатеричной системе:", hash_hex)
    
    # Запись значений в текстовый файл
    with open('$CRC32_data.txt', 'a', newline='') as file:
        writer = csv.writer(file, delimiter='\t')
        writer.writerow([data, hash_dec, hash_hex])
    
    start_2 = ''
    while start_2 != 'n' and start_2 != 'y':
        start_2 = input(str('Вы хотите продолжить? y/n '))
        if start_2 == 'n':
            start = False
            break
        elif start_2 == 'y':
            break
    
    print('===================================')

# После выполнения программы:
script_dir = os.path.dirname(os.path.abspath(__file__))
bat_file_path = os.path.join(script_dir, "$SER.bat")
subprocess.call([bat_file_path], shell=True)
