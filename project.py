import random
def Randlist(start,end,num):
	res=[]
	for j in range(num):
		res.append(random.randint(start,end))
	return res
n=int(input())
Niter=100000
temp=0
for j in range(Niter):
	randomlist=Randlist(1,365,n)
	seen=[]
	for number in randomlist:
		if number in seen:
			temp+=1
			break
		else:
			seen.append(number)
			continue

print(temp/Niter)