import binascii

def calculate_crc32(data):
    crc = binascii.crc32(data.encode()) & 0xffffffff
    return crc

data = input("Введите информацию для хеширования: ")
hash_dec = calculate_crc32(data)
hash_hex = hex(hash_dec)[2:]  # Получаем шестнадцатеричное представление, удаляем префикс "0x"

print("Исходная информация:", data)
print("Хеш-значение CRC-32 в десятичной системе:", hash_dec)
print("Хеш-значение CRC-32 в шестнадцатеричной системе:", hash_hex)
