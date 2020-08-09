a=0
b=1
i=1
num=int(input("enter a number: "))
print("the fibonacci series is: ")
print(a, end=",")
print(b, end=",")
while(i<=num-2):
    c=a+b
    a=b
    b=c
    i+=1
    print(c, end=",")
