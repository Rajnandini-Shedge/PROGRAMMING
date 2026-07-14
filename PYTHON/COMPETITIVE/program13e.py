def DisplayGrade(Marks):
    if(Marks>=75):
        print("Distinction")
    elif(Marks>=60):
        print("First Class")
    elif(Marks>=50):
        print("Second Class")
    else:
        print("fail")
    
def main():

    Value=int(input("Enter Marks:"))

    DisplayGrade(Value)


if __name__ =="__main__":
    main()