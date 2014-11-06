def finder(l):
	a = l[0]
	for num in l:
		if(a<num):
			a = num;
	return a;

def counter(l,num):
	count =0;
	for x in l:
		if(num==x):
			count +=1
	return count

myMax = [1,2,1000,5,8,1000,1000]
print finder(myMax);

print counter(myMax,1000)

