from Crypto.Hash import MD4

# Function to compute MD4 hash
def compute_md4_hash(input_string):
    hash_object = MD4.new(input_string.encode('utf-8'))  # Create MD4 hash object
    return hash_object.hexdigest()  # Return the hexadecimal digest

# Example usage
input_data = "Hello, World!"
print("MD4 Hash:", compute_md4_hash(input_data))
