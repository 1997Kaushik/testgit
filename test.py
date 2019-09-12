
lst = []
a=1

while len(lst)!=20:
	if a==1:
		a+=1
	elif a==2:
		lst.append(a)
		a+=1
	else:
		for i in range(2,a):
			if a%i == 0:
				a+=1
				break
		else:
			lst.append(a)
			a+=1

print(lst)

