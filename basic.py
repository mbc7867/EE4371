#Basic

#Q1a Sum of squares of numbers less than n

na=int(input("Enter any integer n:"))
s=0
for i in range(1,na):
	s+=i**2;
#print("Sum of squares of integers less than n is",s)


#Q1b Sum of squares of odd integers less than n

nb=int(input("Enter any integer n:"))
s=0
for i in range(1,nb,2):
	s+=i**2;
#print("Sum squares of odd integers less than n is",s)


#Q2a

list_1=[]
for i in range(60,90,10):
	list_1.append(i)
print(list_1)

#Q2b

list_2=[]
for i in range(4,-6,-2):
	list_2.append(i)
print(list_2)
