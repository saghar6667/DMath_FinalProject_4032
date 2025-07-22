from base import RSA

def print_menu():
    print("\n=== RSA Encryption Menu ===")
    print("1. Encrypt a message")
    print("2. Decrypt a message")
    print("3. Exit")

def main():
    rsa = RSA()
    last_cipher = None
    
    while True:
        print_menu()
        choice = input("Choose an option: ").strip()
        match choice:
            case "1":
                message = input("\nEnter a message to encrypt: ")
                try:
                    cipher = rsa.encrypt(message)
                    print(f"\nEncrypted message: {cipher}")
                    last_cipher = cipher
                except ValueError as e:
                    print("Error: ", e)
            case "2":
                cipher_input = input("\nEnter the ciphertext to decrypt: ")
                try:
                    decrypted = rsa.decrypt(cipher_input)
                    print(f"\nDecrypted message: {decrypted}")
                except Exception as e:
                    print("Decryption failed:", e)
            case "3":
                print("Exiting...")
                break
            case _:
                print("Invalid option. Try again.")

if __name__ == "__main__":
    main()

