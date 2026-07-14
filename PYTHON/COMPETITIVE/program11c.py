def CountDigit(No):
    Count=0
    Digit=0

    while(No > 1):
        Digit=No%10
        Count =Count+Digit
        No=No//10
    return Count



    
def main():

    Value=int(input("Enter number:"))

    Ret =CountDigit(Value)

    print("Total no of Digits:",Ret)
  

if __name__ =="__main__":
    main()