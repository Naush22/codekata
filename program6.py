a=int(raw_input())
if((a%4==0)):
    print("Leap year")
elif((a%400==0)):
    print("Leap year")
elif((a%100==0)):
    print("Leap year")
else:
    print("Not a leap year")
