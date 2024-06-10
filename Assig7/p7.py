
x = int(input("Enter Number : "))
i =0
count =0
while(x>0):
    if(i%2==0):
        count+=1
    if(count==x):
        break
    i+=1
print(i)
