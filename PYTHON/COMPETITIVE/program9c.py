def Square(No1):
    return No1*No1
    
def main():

    Value=int(input("Enter number:"))

    Ret=Square(Value)

    print("Square of number is:",Ret)

if __name__ =="__main__":
    main()