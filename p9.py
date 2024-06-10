


num = int(input("Enter Value : "))

for i in range(2,num):
    if(num%i==0):
        print("Not Prime number ",num)
        break
else:
    print("Prime Number : ",num)

