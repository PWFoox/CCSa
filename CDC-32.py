import binascii

def calculate_crc32(data):
    crc = binascii.crc32(data.encode()) & 0xffffffff
    return crc

data = input("Введите информацию для хеширования: ")
hash_value = calculate_crc32(data)
print("Хеш-значение CRC-32 для введенной информации:", hash_value)

