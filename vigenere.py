import string
import time

def encrypt_vigenere(plaintext, key):
    encrypted_text = ""
    key = key.lower()
    key_index = 0

    for char in plaintext:
        if char.isalpha():
            ascii_offset = ord('а') if char.islower() else ord('А')
            key_char = key[key_index % len(key)]
            key_offset = ord(key_char.lower()) - ord('а')
            shifted_char = chr((ord(char) - ascii_offset + key_offset) % 33 + ascii_offset)

            if char.isupper():
                shifted_char = shifted_char.upper()

            encrypted_text += shifted_char
            key_index += 1
        else:
            encrypted_text += char

    return encrypted_text

def decrypt_vigenere(ciphertext, key):
    decrypted_text = ""
    key = key.lower()
    key_index = 0

    for char in ciphertext:
        if char.isalpha():
            ascii_offset = ord('а') if char.islower() else ord('А')
            key_char = key[key_index % len(key)]
            key_offset = ord(key_char.lower()) - ord('а')
            shifted_char = chr((ord(char) - ascii_offset - key_offset) % 33 + ascii_offset)

            if char.isupper():
                shifted_char = shifted_char.upper()

            decrypted_text += shifted_char
            key_index += 1
        else:
            decrypted_text += char

    return decrypted_text


def main():
    while True:
        print("Выберите действие:")
        print("1. Зашифровать")
        print("2. Дешифровать")
        print("3. Выход")

        choice = input("Ваш выбор: ")

        if choice == "1":
            plaintext = input("Введите текст для шифрования: ")
            key = input("Введите ключ: ")
            encrypted_text = encrypt_vigenere(plaintext, key)
            print("Зашифрованный текст:", encrypted_text)
        elif choice == "2":
            ciphertext = input("Введите зашифрованный текст: ")
            key = input("Введите ключ: ")
            decrypted_text = decrypt_vigenere(ciphertext, key)
            print("Дешифрованный текст:", decrypted_text)
        elif choice == "3":
            time.sleep(1)
            print("Программа завершена.")
            break
        else:
            print("Ошибка: неверный выбор действия")

if __name__ == "__main__":
    main()
