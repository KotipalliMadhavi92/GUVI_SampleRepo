n=int(input())
l=list(map(int,input().split()))
res=list()
for i in range(0,n):
	if(i==l[i]):
		res.append(l[i])
if(len(res)==0):
	print("-1")
else:
	res.sort()
	for i in res:
		print(i,end=" ")
