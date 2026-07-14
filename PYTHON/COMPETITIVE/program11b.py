def CountDigit(No):
    Count=0

    while(No > 1):
        Count =Count+1
        No=No/10
    return Count



    
def main():

    Value=int(input("Enter number:"))

    Ret =CountDigit(Value)

    print("Total no of Digits:",Ret)
  

if __name__ =="__main__":
    main()