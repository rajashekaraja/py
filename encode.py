a=input()
b=input()
c=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
f=[]
for i in range(len(a)):
    if c.index(b[i])>c.index(a[i]):
        e=c.index(b[i])-c.index(a[i])
    else:
        e=c.index(b[i])-c.index(a[i])+26
    f.append(e)
g=set(f)
if len(g)==1:
    print("Yes")
else:
    print("No")