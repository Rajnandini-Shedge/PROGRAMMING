def ReverseNumber(No):
    Rev=0
    Digit=0

    while(No >= 1):
        Digit=No%10
        Rev=(Rev*10)
        Rev=Rev+Digit
        No=No//10
    return Rev

def main():

    Value=int(input("Enter number:"))

    Ret =ReverseNumber(Value)

    print("Total no of Digits:",Ret)
  

if __name__ =="__main__":
    main()