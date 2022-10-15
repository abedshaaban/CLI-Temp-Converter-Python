#!/usr/bin/python

# Author: n-anselm
# Date created: 221014
# Date modified: 221015
# Description: Terminal-based Fahrenheit/Celsius converter

# Formulas
# F2C: °C = (°F − 32) × 5/9
# C2F: °F = °C × 9/5 + 32

from sys import argv, exit

# Convert to Celsius
def to_celsius(f):
	c = (float(f) - 32.0) * 5 / 9
	print(f"{'%.1f' %c} °C")	

# Convert to Fahrenheit
def to_fahrenheit(c):
	f = float(c) * 9 / 5 + 32
	print(f"{'%.1f' %f} °F") 
	

# Check if passed arg is a number
def is_number(num):
	try:
		float(num)
		return True
	except ValueError:
		return False
		
		
def print_help():
	print("\nSpecify what you want to convert to:")
	print("-c  Convert to Celsius")
	print("-f  Convert to Fahrenheit")
	print("Formate: python temp.py -[format] [temp]")
	print("\nExample: python temp.py -c 212")
	print("Output: 100 °C")
	exit(2)


def parseArgs(args):
	# Make sure that there are two args passed in by user
	# (the 1st arg is just the file name) so total is 3

	if len(args) > 2:
		# Get the args
		conversion = argv[1]  # C or F
		temp = argv[2]  # Temp value to convert

		if is_number(temp):  # If the 2nd input is a number
		
			if conversion == "-c":
				to_celsius(temp)  # Convert to Celsius
		
			elif conversion == "-f":
				to_fahrenheit(temp)  # Convert to Fahrenheit
		
		else:
			print("your value is not an integer.")
			
	else:
		print_help()
	
	
if __name__ == "__main__":
	parseArgs(argv)

