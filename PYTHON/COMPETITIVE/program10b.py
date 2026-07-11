def SumofN(No):
    Sum=0
    for i in range(No+1):
        Sum=Sum+i
    return Sum
    
    
def main():

    Value=int(input("Enter number:"))

    Ret=SumofN(Value)

    print("Sum of first N numbers:",Ret)

if __name__ =="__main__":
    main()