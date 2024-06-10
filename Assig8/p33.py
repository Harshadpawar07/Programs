

x = int(input(" : "))
count = 0
for i in range(1,x):
    if(x%i==0):
        count+=i
if(count==x):
    print("Perfect")
else:
    print("Not Perfect")
