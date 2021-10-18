
#n,s,e,w=0,1,2,3

x=input("Enter initial direction: ")
if x=='n':
    val=0
elif x=='s':
    val=1
elif x=='e':
    val=2
elif x=='w':
    val=3
else:
    print("Incorrect Input")
    exit()
    
lst=['L','R','L','S','R','B','L']

for i in lst:
    if i=='L':
        val=3
    elif i=='R':
        val=2
    elif i=='B':
        val=1
    else:
        val=0

print(val)


