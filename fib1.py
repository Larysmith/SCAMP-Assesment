# Define a function for fibonacci
def fibbo (number):

# since the first number always starts with zero	
	a = 0
	b = 1
	result = []
	for i in range (number):
		result.append(a)
		
		temp = a
		a = b
		b = temp + b
	return (result)
	  
print(fibbo(50))