st=input().split()
s=int(st[0])
t=int(st[1])
ab=input().split()
a=int(ab[0])
b=int(ab[1])
mn=input().split()
m=int(mn[0])
n=int(mn[1])
apple=input().split()
orange=input().split()
print(apple,orange)
ap=[]
org=[]

for i in range(m):
    ap.append(a+(int(apple[i])))
for j in range(n):
    org.append(b+(int(orange[j])))
print(ap)
print(org)
c1=0
c2=0
for i in ap:
    if i>=s and i<=t:
        c1+=1
for j in org:
    if j>=s and j<=t:
        c2+=1

print(c1)
print(c2)