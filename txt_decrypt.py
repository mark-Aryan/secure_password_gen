decrypt = ''
alaphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
f = open("password.txt","r")
file = f.read()
f.close()
for i in file:
    new_text = alaphabet.find(i)
    text = (new_text - 5) % len(alaphabet)
    decrypt += alaphabet[text]
print(decrypt)