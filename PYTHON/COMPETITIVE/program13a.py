def AreaRect(Length,width):
    return Length*width
    
def main():

    ValueL=int(input("Enter Length:"))
    ValueW=int(input("Enter Width:"))

    Ret=AreaRect(ValueL,ValueW)

    print("Area of Rectangle is:",Ret)

if __name__ =="__main__":
    main()