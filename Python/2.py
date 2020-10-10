r = float (input ("Enter the radius of the cylinder in metre\n"))
h = float (input ("Enter the height of the cylinder in metre\n"))
pi = 3.1416

ca= pi * r**2
sa = (2*pi*r*h) + (2*pi* r**2)
vol = pi*h*r**2
print ("Cross section area of the cylinder is",ca, "sq metre\n")
print ("Surface area of the cylinder is", sa, "sq metre\n")
print ("Volume of the cylinder is", vol, "metre^3\n")
       
