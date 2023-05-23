# KabitaThapa
# cesar_cipher_2358843(np03cs4s230093)

def welcome ():
    print("Welcome to the Caesar Cipher")
    print("This program encrypts and decrypts text using Caesar Cipher.")


def main():
    welcome ()
    while True:
        mode = input("Would you like to encrypt (e) or decrypt (d): ")
        if mode not in ['e', 'd']:
            print("Invalid Mode")
            continue

        message_type = input("Would you like to read from a file (f) or the console (c)? ")
        if message_type == 'c':
            message = input("What message would you like to {}: ".format("encrypt" if mode == 'e' else "decrypt"))
        elif message_type == 'f':
            while True:
                filename = input("Enter a filename: ")
                try:
                    with open(filename, 'r') as file:
                        message = file.read()
                    break
                except FileNotFoundError:
                    print("Invalid Filename")
                    continue
        else:
            print("Invalid input")
            continue

        shift = int(input("What is the shift number: "))

        if mode == 'e':
            result = caesar_cipher_encrypt(message, shift)
        else:
            result = caesar_cipher_decrypt(message, shift)

        print(result)

        if message_type == 'f':
            with open('result.txt', 'w') as file:
                file.write(result)
            print("Output written to result.txt")

        another = input("Would you like to encrypt or decrypt another message? (y/n): ")
        if another.lower() == 'y':
            continue
        else:
            print("Thanks for using the program, goodbye!")
            break

def caesar_cipher_encrypt(message, shift):
    """
    This function performs Caesar Cipher encryption
    :param message: the input message to encrypt
    :param shift: the number of positions to shift the letters
    :return: the encrypted message
    """
    result = ""
    for char in message:
        # Encrypt uppercase characters
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        # Encrypt lowercase characters
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char
    return result.upper()


def caesar_cipher_decrypt(message, shift):
    """
    This function performs Caesar Cipher decryption
    :param message: the input message to decrypt
    :param shift: the number of positions to shift the letters
    :return: the decrypted message
    """
    result = ""
    for char in message:
        # Decrypt uppercase characters
        if char.isupper():
            result += chr((ord(char) - shift - 65) % 26 + 65)
        # Decrypt lowercase characters
        elif char.islower():
            result += chr((ord(char) - shift - 97) % 26 + 97)
        else:
            result += char
    return result.upper()


if __name__ == '__main__':
    main()



    




