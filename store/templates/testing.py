a = [1,2,3,4,5]
# b=a[::-1]
# print(b)
b = int(input("enter a number"))
ab = []
for i in a:
    if b>=i:
        ab.append(b)
        b = b-1
        print(ab)
        


