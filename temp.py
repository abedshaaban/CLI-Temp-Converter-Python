#!/usr/bin/python

# Author: n-anselm
# Date created: 221014
# Date modified: 221015
# Description: Terminal-based Fahrenheit/Celsius converter

# Formulas
# F2C - °C = (°F − 32) × 5/9
# C2F - °F = °C × 9/5 + 32

import sys

# Convert to Celsius
def to_celsius(f):
	c = f - 32.0
	c = c * 5 / 9
	print("%.1f" % c + " °C")
	

# Convert to Fahrenheit
def to_fahrenheit(c):
	f = c * 9 / 5 + 32
	print("%.1f" % f + " °F")
	

# Check if passed arg is a number
def is_number(num):
	try:
		float(num)
		return True
	except ValueError:
		return False
		
		
def print_help():
	print("python temp.py -[format] [temp]")
	print("\nSpecify what you want to convert to:")
	print("-c  Convert to Celsius")
	print("-f  Convert to Fahrenheit")
	print("\nExample: python temp.py -c 212")
	print("Output: 100 °C")
	sys.exit(2)


def parseArgs(args):
	# Make sure that there are two args passed in by user
	# (the 1st arg is just the file name) so total is 3
	if len(args) > 2:
		# Get the args
		conversion = sys.argv[1]  # C or F
		temp = sys.argv[2]  # Temp value to convert
		if not is_number(temp):  # If the 2nd input is not a number
			print_help()
		if conversion == "-c":
			to_celsius(float(temp))  # Convert to Celsius
		elif conversion == "-f":
			to_fahrenheit(float(temp))  # Convert to Fahrenheit
		else:
			print_help()
	else:
		print_help()
	
	
if __name__ == "__main__":
	parseArgs(sys.argv)

