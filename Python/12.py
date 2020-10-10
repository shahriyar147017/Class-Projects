n = int (input('Enter the limit\n'))
f = 1
for i in range(1, n+1 ,+1):
    f = f*i
print ("Factorial of {0} is {1}".format(n,f))
