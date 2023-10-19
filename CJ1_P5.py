#import libraries neccessary to make a table
import numpy as np 
from astropy.table import Table
from astropy.io import ascii

#define main function
def main():
	#range 0 - 2pi, 1000 steps
	x = np.linspace(0,2*np.pi,1000)

	#important to note, pi can never be represented accurately
	#with a floating point number, pi is not given in radians
	#sin(2pi) will get infinitely close to 0 but never show 0 in results
	sin_x = np.sin(x)

	#make table
	data = Table([x,sin_x], names=['x','sin_x'])

	#print the table
	print(data)

if __name__ == '__main__':
	 main()