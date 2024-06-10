

x = int(input(" : "))
num = x
Z = x
ret = 0
count = 0
while(Z>0):
    Z = Z//10
    count+=1
while(x>0):
    N = x%10
    ret = ret + N**count
    x//=10
if(num==ret):
    print("amg")


