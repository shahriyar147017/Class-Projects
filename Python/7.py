a = int (input ("Enter the numbers\n"))
b = int (input('\n'))
c = int (input('\n'))

if (a>=b and c>=b):
    if (a >=c):
        print (a ,"is the largest value\n")
    else:
        print (c ,"is the largest value\n")
    print (b ,'is the smallest value\n')

elif (b>=a and c>=a):
    if (b >=c):
        print (b ,"is the largest value\n")
    else:
        print (c ,"is the largest value\n")
    print (a ,'is the smallest value\n')


elif (b>=c and a>=c):
    if (b >=a):
        print (b ,"is the largest value\n")
    else:
        print (a ,"is the largest value\n")
    print (c ,'is the smallest value\n')
    
