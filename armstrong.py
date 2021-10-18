num=int(input("Enter the number: "))
sum=0
temp=num
while(temp>0):
    rem=temp%10
    sum+=rem**3
    temp//=10
if(num==sum):
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")
