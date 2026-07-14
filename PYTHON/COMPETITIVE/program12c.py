def Addition(No1,No2):
    return No1+No2

def Substraction(No1,No2):
    return No1-No2

def Multiplication(No1,No2):
    return No1*No2

def Divison(No1,No2):
    return No1//No2

def main():

    Value1=int(input("Enter first number:"))

    Value2=int(input("Enter first number:"))

    Ret=Addition(Value1,Value2)
    print("Addition is :",Ret)

    Ret=Substraction(Value1,Value2)
    print("substraction is :",Ret)

    Ret=Multiplication(Value1,Value2)
    print("Multiplication is :",Ret)
    
    Ret=Divison(Value1,Value2)
    print("Addition is :",Ret)

if __name__ =="__main__":
    main()