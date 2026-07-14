def Vowel(Ltr):
    if(Ltr== 'a') or (Ltr == 'e') or (Ltr == 'i') or (Ltr == 'o') or (Ltr == 'u') or (Ltr == 'A') or (Ltr == 'E')or (Ltr == 'I')or (Ltr == 'O')or (Ltr == 'U'):
        return True
    else:
        return False
    
    
def main():

    Char=input("Enter Character:")

    Ret=Vowel(Char)

    if(Ret == True):
        print("Vowel")
    else:
        print("Not a vowel")

if __name__ =="__main__":
    main()