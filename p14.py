

x = int(input(" : "))
count = 0
while(x!=0):
    x = x//10
    if(x%2==1):
        count+=1
print(count)
