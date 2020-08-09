list1=[]
list2=[]
n1=int(input("enter the list of number for list1: "))
n2=int(input("enter the list of number for list2: "))


print("enter the numbers in list1: ")
for i1 in range(n1):
    d1=int(input())
    list1.append(d1)
print("output: ")
for j1 in list1:
    if(j1>=0):
        print(j1, end=",")
print("\n")

        
print("enter the numbers in list2: ")
for i2 in range(n2):
    d2=int(input())
    list2.append(d2)
print("output: ")
for j2 in list2:
    if(j2<0):
        list2.remove(j2)
print(list2)
