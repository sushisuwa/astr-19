#define a function f(x) = x**3 + 8
def math_f(x):
	return x**3+8

def main():
	#send x = 9 to function
	y = math_f(9)
	#print result 
	print(y)
	#if result > 27...
	if(y > 27):
		print("YAY!")

#execute main function
if __name__ == '__main__':
	main()