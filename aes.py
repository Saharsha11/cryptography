from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import base64

class AESDemo:
    def __init__(self):
        # Generate a random 256-bit (32-byte) key
        self.key = get_random_bytes(32)
        
    def encrypt(self, plaintext):
        """
        Encrypt the plaintext using AES-256 in CBC mode with proper padding
        """
        # Convert string to bytes
        plaintext = plaintext.encode('utf-8')
        
        # Generate random IV (Initialization Vector)
        iv = get_random_bytes(AES.block_size)
        
        # Create cipher object and encrypt the data
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        
        # Pad data to be multiple of 16 bytes
        padded_data = pad(plaintext, AES.block_size)
        
        # Encrypt the padded data
        encrypted_data = cipher.encrypt(padded_data)
        
        # Combine IV and encrypted data and encode in base64
        encrypted_package = base64.b64encode(iv + encrypted_data).decode('utf-8')
        
        return encrypted_package

    def decrypt(self, encrypted_package):
        """
        Decrypt the encrypted package using AES-256 in CBC mode
        """
        # Decode the base64 encrypted package
        encrypted_package = base64.b64decode(encrypted_package.encode('utf-8'))
        
        # Extract IV and encrypted data
        iv = encrypted_package[:AES.block_size]
        encrypted_data = encrypted_package[AES.block_size:]
        
        # Create cipher object for decryption
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        
        # Decrypt and unpad the data
        decrypted_data = unpad(cipher.decrypt(encrypted_data), AES.block_size)
        
        return decrypted_data.decode('utf-8')

def demonstrate_aes():
    # Create instance of AES demo
    aes = AESDemo()
    
    # Original message
    message = "My name is Saharsha"
    print(f"Original message: {message}\n")
    
    # Encrypt the message
    encrypted = aes.encrypt(message)
    print(f"Encrypted (Base64): {encrypted}\n")
    
    # Decrypt the message
    decrypted = aes.decrypt(encrypted)
    print(f"Decrypted message: {decrypted}\n")
    
    # Verify the decryption worked correctly
    print(f"Decryption successful: {message == decrypted}")

if __name__ == "__main__":
    demonstrate_aes()