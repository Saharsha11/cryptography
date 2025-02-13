from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad
import base64

def encrypt_des(plaintext):
    """
    Encrypt data using DES in ECB mode
    
    Args:
        plaintext (str): Text to encrypt
        
    Returns:
        tuple: (Base64 encoded encrypted data, key used for encryption)
    """
    # Generate a random 8-byte (64-bit) key
    key = get_random_bytes(8)
    
    # Convert plaintext to bytes
    plaintext_bytes = plaintext.encode('utf-8')
    
    # Create DES cipher
    cipher = DES.new(key, DES.MODE_ECB)
    
    # Pad the data to be multiple of 8 bytes (DES block size)
    padded_data = pad(plaintext_bytes, DES.block_size)
    
    # Encrypt the data
    encrypted_data = cipher.encrypt(padded_data)
    
    # Convert to base64
    encrypted_base64 = base64.b64encode(encrypted_data).decode('utf-8')
    
    return encrypted_base64, key

# Example usage
if __name__ == "__main__":
    message = "Hello my name is Ram"
    encrypted_text, encryption_key = encrypt_des(message)
    print(f"Original message: {message}")
    print(f"Encrypted (Base64): {encrypted_text}")
    print(f"Key (in bytes): {encryption_key}")