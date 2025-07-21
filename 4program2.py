#Check if Number is a Multiple of Both 3 and 5
#Ask the user for a number and check:
#If it is divisible by both 3 and 5.
#Print appropriate messages.

Number = float(input("Enter the Nuumber: " ))
if Number%3==0 and Number%5==0:
    print("Number is fully dividible by 3 and 5")
else :
    print("number is inappropriate ")    