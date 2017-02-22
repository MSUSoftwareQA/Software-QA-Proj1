#/bin/python3

# Software Testing and QA - Proj 1
# Alex Cote - alc552
# Ginny Tabor - glt79
# Patrick Boudreaux - pdb145
# Damian Cooper - dcc198

import math
import re

def BMICalc(usrWeight, usrHeight):
	return (usrWeight / ((usrHeight**2) * 703))

def retCalc(usrAge, usrSal, usrSav):
	return (usrAge + math.floor(usrSav / (usrSal * (usrSav / 100))))

def distCalc(x1, x2, y1, y2):
	return (math.sqrt(((x2 - x1)**2) + ((y2 - y1)**2)))

def emailVerify(usrEmail):
	return bool(re.match("\w\w*@\w\w*.[a-zA-Z]{3}$", usrEmail))

loopProg = True

while loopProg:
	print("0) Exit\n1) BMI Calc\n2) Retirement Calc\n3) Distance Calc\n4) Email Verify")
	usrInput = int(input("\nWhich would you like to run? (0-4) "))
	
	# Begin branching based on which option the user has chosen.
	if usrInput == 0:
		# Exit program
		loopProg = False
	elif usrInput == 1:
		print("\n\n### BMI Calculator ###\n\n")
		weightInput = input("Weight (lbs): ")
		heightInput = input("Height (inches): ")

		usrBMI = BMICalc(weightInput, heightInput)

		print("\nBMI: " + usrBMI)
		if usrBMI <= 18.5:
			print("You are underweight.\n\n")
		elif usrBMI < 25:
			print("You are at a normal weight.\n\n")
		elif usrBMI < 30:
			print("You are overweight.\n\n")
		else:
			print("You are obese.\n\n")
	elif usrInput == 2:
		print("\n\n### Retirement Calculator ###\n\n")
		usrAge = input("Current age: ")
		usrSalary = input("Annual salary: ")
		savePerc = input("Savings percentage: ")
		saveGoal = input("Savings goal amount: ")

		goalAge = retCalc(usrAge, usrSalary, savePerc)

		print("Age you will meet your goal: " + goalAge)
		if goalAge >= 100:
			print("You will not meet your goal.")
		else:
			print("You can meet your goal!")
	elif usrInput == 3:
		print("\n\n### Distance Calculator ###\n\n")
		loc1X = int(input("Location 1 X: "))
		loc1Y = int(input("Location 1 Y: "))
		loc2X = int(input("Location 2 X: "))
		loc2Y = int(input("Location 2 Y: "))

		distRes = distCalc(loc1X, loc2X, loc1Y, loc2Y)

		print("The distance between your two points is", distRes)
	elif usrInput == 4:
		print("\n\n### Email Verifier ####\n\n")
		emailInput = input("What email would you like to verify? ")
		
		if emailVerify(emailInput):
			print(emailInput + " is a valid email address.")
		else:
			print(emailInput + " is not a valid email address.")

print("\nExiting...")
