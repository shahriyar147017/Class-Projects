a = int (input ("Enter the year\n"))

if (a%4 == 0):
    if (a%100 == 0):
        if (a%400 ==0):
            print (a ,"is Leap Year\n")
        else:
           print (a ,"is not a Leap Year\n")
    else:
        print (a ,"is Leap Year\n")
else:
    print (a ,"is not Leap Year\n")
