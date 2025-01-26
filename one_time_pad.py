
def encrypt(text  ,key):
    result = ""
    for i in range(len(text)):
        p = text[i]
        k = key[i]
        if p.isupper() and k.isupper():
            char = chr((ord(p) + ord(k)) % 26 + 65)
            result += char
        else:
            char = chr(((ord(p) - 97) + (ord(k)-97)) % 26 + 97)
            result += char
    return result     
print(encrypt("hello","write"))