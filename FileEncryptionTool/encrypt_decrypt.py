from cryptography.fernet import Fernet
import os

def generate_key():
    """Generates a key for encryption and decryption."""
    return Fernet.generate_key()

def save_key(key, key_file="secret.key"):
    """Saves the encryption key to a file."""
    with open(key_file, "wb") as f:
        f.write(key)

def load_key(key_file="secret.key"):
    """Loads the encryption key from a file."""
    return open(key_file, "rb").read()

def encrypt_file(file_path, key):
    """Encrypts a file."""
    fernet = Fernet(key)
    with open(file_path, "rb") as f:
        data = f.read()
    encrypted_data = fernet.encrypt(data)
    with open(file_path + ".encrypted", "wb") as f:
        f.write(encrypted_data)
    print(f"File encrypted: {file_path}.encrypted")

def decrypt_file(encrypted_file_path, key):
    """Decrypts a file."""
    fernet = Fernet(key)
    with open(encrypted_file_path, "rb") as f:
        encrypted_data = f.read()
    decrypted_data = fernet.decrypt(encrypted_data)
    original_file_path = encrypted_file_path.replace(".encrypted", "")
    with open(original_file_path, "wb") as f:
        f.write(decrypted_data)
    print(f"File decrypted: {original_file_path}")

if __name__ == "__main__":
    key_file = "secret.key"

    # Generate or load the key
    if not os.path.exists(key_file):
        print("Generating new encryption key...")
        key = generate_key()
        save_key(key, key_file)
    else:
        print("Loading existing encryption key...")
        key = load_key(key_file)

    # Encrypt or decrypt a file
    action = input("Do you want to (E)ncrypt or (D)ecrypt a file? ").strip().lower()
    if action == "e":
        file_path = input("Enter the path of the file to encrypt: ").strip()
        encrypt_file(file_path, key)
    elif action == "d":
        encrypted_file_path = input("Enter the path of the encrypted file: ").strip()
        decrypt_file(encrypted_file_path, key)
    else:
        print("Invalid action. Please choose 'E' for encryption or 'D' for decryption.")