def AreaCircle(Radius,PI=3.14):
    return Radius*Radius*PI
    
def main():

    ValueR=int(input("Enter Radius:"))
    

    Ret=AreaCircle(ValueR)

    print("Area of Circle is:",Ret)

if __name__ =="__main__":
    main()