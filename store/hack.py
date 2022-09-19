n = 5
b=['5','6','7','4','5','6']
c=[]
a=set(b)
for i in a:
    c.append(i)
    c.sort()
    d=''.join(c)
    print(d)