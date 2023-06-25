n=int(input())
m=(10**9)+7
for x in range(n):
    a,b,c=input().split()
    a=int(a)
    b=int(b)
    c=int(c)
    bc=((a%m)**b)%m
    abc=(a**bc)%m
    print(abc)