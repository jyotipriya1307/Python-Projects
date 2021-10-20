def play(l):
    
    c=0
    m=0

    for i in l:
        m=max(l)
        if n==m:
            c+=1
        

    print(c)

    if c%2==0:
        print("A Wins")
    else:
        print("B Wins")
        

l = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
    ele = int(input())
    l.append(ele)


play(l)
