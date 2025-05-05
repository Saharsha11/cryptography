import hashlib

def compute_md5(input_string):
    # Create an MD5 hash object
    md5_hash = hashlib.md5()
    
    # Update the hash object with the input string encoded as bytes
    md5_hash.update(input_string.encode('utf-8'))
    
    # Return the hexadecimal representation of the hash
    return md5_hash.hexdigest()

if __name__ == "__main__":
    # Example usage
    input_data = input("Enter the string to hash using MD5: ")
    md5_result = compute_md5(input_data)
    print(f"MD5 Hash: {md5_result}")