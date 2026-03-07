import hashlib

def run_hash():
    while True:
        print("""
   === Hash Generator ===
1. MD5
2. SHA-1
3. SHA-256
4. SHA-512
5. Back
""")
        choice = input("Select an option (1-5): ")
        if choice == '5' or choice.lower() == 'back':
            return
        
        text = input("Enter the text to hash: ").encode()

        try:
            if choice == '1':
                print("MD5:", hashlib.md5(text).hexdigest())
            elif choice == '2':
                print("SHA-1:", hashlib.sha1(text).hexdigest())
            elif choice == '3':
                print("SHA-256:", hashlib.sha256(text).hexdigest())
            elif choice == '4':
                print("SHA-512:", hashlib.sha512(text).hexdigest())
            else:
                print("Invalid choice.")
        except Exception as e:
            print("An error occurred:", e)
        
        input("Press Enter to continue...")
