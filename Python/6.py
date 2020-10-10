a = float(input("Enter your Marks\n"))
if ( a >=0 and a<=100):
    if ( a>=80):
        print ("The grade is A+\n")
    elif ( a>=75):
        print ("The grade is A\n")

    elif ( a>=70):
        print ("The grade is A-\n")

    elif ( a>=65):
        print ("The grade is B+\n")
    
    elif ( a>=60):
        print ("The grade is B\n")

    elif ( a>=55):
        print ("The grade is B-\n")
    
    elif ( a>=50):
        print ("The grade is C\n")

    elif ( a>=45):
        print ("The grade is D\n")

    elif ( a>=40):
        print ("The grade is E\n")
    
    else:
        print ("The grade is F\n")

else:
    print ("Invalid Marks\n")
