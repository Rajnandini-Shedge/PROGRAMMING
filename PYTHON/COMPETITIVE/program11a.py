def Prime(No):
    for i in range(2,No):
        if(No % i == 0):
            return False
    return True
def main():

    Value=int(input("Enter number:"))

    Ret =Prime(Value)

    if(Ret == True):
        print("Its a prime number")
    else:
        print("Its not prime number")

if __name__ =="__main__":
    main()