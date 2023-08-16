import os

filename = "$CRC32_data.txt"

if os.path.isfile(filename):
    print("Файл уже существует. Программа завершается.")
else:
    with open(filename, "w") as file:
        print("Файл успешно создан.")
