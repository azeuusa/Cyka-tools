import base64

def encode_base64(text):
    return base64.b64encode(text.encode()).decode()

def decode_base64(encoded_text):
    return base64.b64decode(encoded_text.encode()).decode()

def encode_ascii(text):
    return ' '.join(str(ord(char)) for char in text)

def decode_ascii(encoded_text):
    return ''.join(chr(int(num)) for num in encoded_text.split())

def encode_hex(text):
    return text.encode().hex()

def decode_hex(encoded_text):
    return bytes.fromhex(encoded_text)

def exit_program():
    print("Exiting blyat decoder. Stay strong, blyat!")
    exit()

while True:
    print("""
   === Blyat Decoder ===
1. Base64 Encode
2. Base64 Decode
3. ASCII Encode
4. ASCII Decode
5. Hex Encode
6. Hex Decode
7. Exit
""")
    choice = input("Select an option (1-7): ")
    if choice == '7' or choice.lower() == 'exit':
        exit_program()
    
    text = input("Enter the text: ")

    try:
        if choice == '1':
            print("Encoded Base64:", encode_base64(text))
        elif choice == '2':
            print("Decoded Base64:", decode_base64(text))
        elif choice == '3':
            print("Encoded ASCII:", encode_ascii(text))
        elif choice == '4':
            print("Decoded ASCII:", decode_ascii(text))
        elif choice == '5':
            print("Encoded Hex:", encode_hex(text))
        elif choice == '6':
            print("Decoded Hex:", decode_hex(text))
        else:
            print("Invalid choice.")
    except Exception as e:
        print("An error occurred:", e)
    
    input("Press Enter to continue...")  # Menambahkan ini agar user bisa lanjut setelah melihat hasil


