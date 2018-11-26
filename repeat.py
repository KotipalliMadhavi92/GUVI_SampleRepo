a=int(input())
l=list(input().split())
ans=list()
for i in range(0,a):
	if l[i] in l[i+1:]:
		ans.append(l[i])
for i in ans:
	print(i,end=" ")