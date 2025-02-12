def encrypt(text,key):
    result = ""
    for x in text:
        if(x.isupper()):
            char = chr((ord(x) + key-65) % 26 +65)
            result += char
        else:
            char = chr((ord(x) + key - 97) % 26 + 97)
            result += char
    return result

def decrypt(text,key):
    result = ""
    for x in text:
        if(x.isupper()):
            char = chr((ord(x) - key-65) % 26 +65)
            result += char
        else:
            char = chr((ord(x) - key - 97) % 26 + 97)
            result += char
    return result


text = input("Enter a string = ")
key = 4
print("Plain text = ",text)
print("Key = ",key)
cliper = encrypt(text,key)
print("Ceaser Cipher = ",cliper)
print("Ceaser plain text  = ",decrypt(cliper,key))