import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), 'seng560-python-math/src/zroberts-seng560-math/'))
import math560

print("Select Operation")
print("1. Addition")
print("2. Subraction")
print("3. Multiplication")
print("4. Division")
print("5. Square Root")
print("6. Exponent")
print("7. Convert to Binary")
print("8. Convert to Hex")
print("9. Convert to Oct")
print("10. Exit Application")

while True:
	choice = int(input("Enter choice: "))
	
	if choice in (1,2, 3, 4, 5, 6, 7, 8, 9, 10):
		if choice == 1:
			num1 = float(input("Enter first number: "))
			num2 = float(input("Enter second number: "))
			print(num1, " + ", num2, "  =  ",  math560.addition(num1, num2))
		
		elif choice == 2:
			num1 = float(input("Enter first number: "))
			num2 = float(input("Enter second number: "))
			print(num1, " - ", num2, "  =  ",  math560.subtract(num1, num2))
		
		elif choice == 3:
			num1 = float(input("Enter first number: "))
			num2 = float(input("Enter second number: "))
			print(num1, " * ", num2, "  =  ",  math560.multiply(num1, num2))
		
		elif choice == 4:
			num1 = float(input("Enter first number: "))
			num2 = float(input("Enter second number: "))
			print(num1, " / ", num2, "  =  ",  math560.divide(num1, num2))
		
		elif choice == 5:
			num1 = float(input("Enter number: "))
			print("SQRT( ", num1, " )  =  ",  math560.squareRoot(num1))

		elif choice == 6:
			num1 = float(input("Enter base number: "))
			num2 = float(input("Enter exponent number: "))
			print(num1, " ^ ", num2, "  =  ",  math560.exponent(num1, num2))
		
		elif choice == 7:
			num1 = int(input("Enter number to conver to binary: "))
			print("BIN( ", num1, " )  =  ",  math560.convertToBinary(num1))
		
		elif choice == 8:
			num1 = int(input("Enter number to conver to hex: "))
			print("HEX( ", num1, " )  =  ",  math560.convertToHex(num1))
		
		elif choice == 9:
			num1 = int(input("Enter number to conver to oct: "))
			print("OCT( ", num1, " )  =  ",  math560.convertToOct(num1))
		
		elif choice == 10:
			print("Exiting application")
			break
		
	else:
		print("Invalid Input")


