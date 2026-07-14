def ChkPerfect(No):
    Sum=0
    No1=No
    for i in range(1,No):
        if(No % i ==0):
            Sum=Sum+i
            
        if(Sum==No1):
            return True

    return False
        
    
def main():

    Value=int(input("Enter number:"))
    
    Ret=ChkPerfect(Value)

    if(Ret==True):
        print("Perfect Number")
    else:
        print("Not a Perfect Number")

if __name__ =="__main__":
    main()