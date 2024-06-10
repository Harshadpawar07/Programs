

x = int(input(" : "))
N = x
rev = 0
while(x>0):
    rev = x%10+(rev*10)
    x = x//10
if(rev==N):
    print("PalinDrom")
else:
    print("Not")

