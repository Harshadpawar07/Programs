
x = int(input(" : "))
num = x
ret = 0
while(x!=0):
    N = x%10
    ret = (ret*10)+N
    x = x//10
if(ret==num):
    print("Palim")
else:
    print("Not")

    
