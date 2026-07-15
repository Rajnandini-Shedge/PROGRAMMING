print("-----------------------------------------")
print("---------Ticket pricing Software---------")
print("-----------------------------------------\n")

print("Please enter your Age:")
Age=int(input())

if(Age <= 5):
    print("Your Entry is free")
elif(Age>5 and Age<=18):
    print("Ticket price : 900")
elif(Age>18 and Age<=40):
    print("Ticket price : 1200")
else:
    print("Ticket price : 500")
