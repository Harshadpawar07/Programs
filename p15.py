

x = int(input(" : "))
ret = 0
while(x>0):
    ret = x%10+(ret*10)
    x = x//10
print(ret)

