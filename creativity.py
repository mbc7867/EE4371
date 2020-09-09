#Q4

def proodd(list_1):
	list2=[]
	s=0
	for i in range(len(list_1)):
		if(list_1[i]%2==1):
			list2.append(1)
			s+=1
		else:
			list2.append(0)
	if(s>=2):
		return 1
	else:
		return 0

list1=[2,4,6,8,9,11]
#print(proodd(list1))

#Q5
'''
s=str(input("Enter the string:"))
length=0
for i in range(len(s)):
	if(s[i]=='a' or s[i]=='A' or s[i]=='e' or s[i]=='E' or s[i]=='i' or s[i]=='I' or s[i]=='o' or s[i]=='O' or s[i]=='u' or s[i]=='U'):
		length+=1
print(length)
'''

#Q6

a,b,c=[int(x) for x in input("Enter three numbers:").split()]

if(a>=b and a>=c):
	if(b+c==a or b*c==a):
		print("yes")
	else:
		print("No")

elif(b>=a and b>=c):
	if(a+c==b or a*c==b):
		print("yes")
	else:
		print("No")
elif(c>=a and c>=b):
	if(a+b==c or a*b==c):
		print("yes")
	else:
		print("No")