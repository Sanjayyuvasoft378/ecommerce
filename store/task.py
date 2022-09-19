import textwrap
a = 1234567890
b = str(a)
print(a)
x = textwrap.wrap(b,2)
f=','.join(x)
print(f)
t = []
for i in x:
    sum = str(int(i[0])+int(i[1]))
    t.append(sum)
n = ','.join(t)
y=''.join(t)
print(n)
print(y)
    