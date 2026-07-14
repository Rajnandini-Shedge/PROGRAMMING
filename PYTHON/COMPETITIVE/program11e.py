def ReverseNumber(No):
    Rev=0
    Digit=0
    No1=No

    while(No >= 1):
        Digit=No%10
        Rev=(Rev*10)
        Rev=Rev+Digit
        No=No//10


        if(Rev==No1):
            return True
        else :
            return False

def main():

    Value=int(input("Enter number:"))

    Ret =ReverseNumber(Value)

    if(Ret==True):
        print("Number is palindrome")
    else:
        print("Number is palindrome")
  

if __name__ =="__main__":
    main()