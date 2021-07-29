#ceaser cypher
alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
message = input("Type message...")
key = len(message)
print(key)
encrypt, decrypt = "", ""
for i in message:
    new_position = (alphabet.find(i)+key) % len(alphabet)
    if i == " ":
        encrypt += " "
    else:
        encrypt += alphabet[new_position]


for i in encrypt:
    position = (alphabet.find(i)-key) % len(alphabet)
    if i == " ":
        decrypt += " "
    else:
        decrypt += alphabet[position]


print("Encrypted message:", encrypt)
print("Decrypted message:", decrypt)