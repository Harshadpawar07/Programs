

def perfect(num):
    
    sum=0
    for i in range(1,num):
        if(num%i==0):
            sum+=i
    if(sum==num):
        print("Perfect Number ",num)
    else:
        print("Not Perfect Number ",num)
    return num

obj = perfect(int(input("Enter Number ")))
print(obj)
