SECURE = (('s', '$'),('and', '&'), ('a', '@'), ('o', '0'), ('i', '1'))
def securePass(password):
    for a,b in SECURE:
        password = password.replace(a,b)
    return password

if __name__ == '__main__':
   passwd = input("Enter Your Password> ")
   password = securePass(passwd)
   print(f"Your Secure Password is \n{password}")

encrypt = ''
decrypt = ''
alaphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
key = 5
for i in passwd:
    text = alaphabet.find(i)
    new_text = (text+5) % len(alaphabet)
    encrypt += alaphabet[new_text]
f = open("password.txt", "a+")
f.write(f"{encrypt},\n")

'''If You Are A Programer You Can Use this To Decode .txt file'''
def decryption():
    global decrypt
    for i in encrypt:
        new_text = alaphabet.find(i)
        text = (new_text - 5) % len(alaphabet)
        decrypt += alaphabet[text]
    return decrypt
