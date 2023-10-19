#importing sys library
import sys

#Defining a class
class Animal:
	#Defining a print function for the class
	def print(self):
		#using fstrings, print the class variables with descriptors
		print("My Animal")
		print(f"Length of arms: {self.armLength}")      #float
		print(f"Length of legs: {self.legLength}")      #float
		print(f"Number of eyes: {self.numOfEyes}")	    #integer
		print(f"Does it have a tail? {self.hasATail}")	#bool
		print(f"Is it furry? {self.is_furry}")	        #bool

	#initializing class variables
	def __init__(self, armlen=1.0, leglen=2.0, num_eyes=2, hasTail=False, isFurry = True):
		self.armLength = armlen 
		self.legLength = leglen
		self.numOfEyes = num_eyes
		self.hasATail = hasTail
		self.is_furry = isFurry

#define main function
def main():
	#call animal class for initialization of a new animel and print using the class function
	fave_animal = Animal()
	fave_animal.print()

#idiom to execute main function
if __name__ == '__main__':
	main()