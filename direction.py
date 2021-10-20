
#n,s,e,w=0,1,2,3

x=input("Enter initial direction: ")
direction_map = {
    'n': 0,
    's': 1,
    'e': 2,
    'w': 3,
}
val = direction_map.get(x)
if not val:
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


