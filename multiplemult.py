num = input("Enter a number up to which to multiply: \n")

for i in range(1,num+1):
	print "\n"
	for j in range(1,11):
		print i,"x",j,"=",i*j
