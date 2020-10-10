a = float(input("Enter the vcalue of a\n"))
b = float(input("Enter the vcalue of b\n"))
c = float(input("Enter the vcalue of c\n"))
p = (b**2 - 4*a*c)
if ( p >= 0 ):
    print ("Real root available\n")
    root1 = (-b + p**0.5)/2*a
    root2 = (-b - p**0.5)/2*a
    print ("The roots are", root1," & ",root2)

else :
    print ("The roots are imaginary")
