n = int (input('Enter the limit\n'))
f = 1
sum = 0
for i in range(1, n+1 ,+1):
    f = f*i
    sum = i/f
print ("Factorial of {0} is {1} and the sum is {2}".format(n,f,sum))
