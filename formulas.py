#/bin/python3

# Software Testing and QA - Proj 1
# Alex Cote - alc552
# Ginny Tabor - glt79
# Patrick Boudreaux - pdb145
# Damian Cooper - dcc198

import functions

loopProg = True

while loopProg:
	print("\n\n=== Main Menu ===\n\n")
	print("0) Exit\n1) BMI Calc\n2) Retirement Calc\n3) Distance Calc\n4) Email Verify")
	usrInput = int(input("\nWhich would you like to run? (0-4) "))
	
	# Begin branching based on which option the user has chosen.
	if usrInput == 0:
		# Exit program
		loopProg = False
	elif usrInput == 1:
		print("\n\n### BMI Calculator ###\n\n")
		weightInput = int(input("Weight (lbs): "))
		heightInput = int(input("Height (inches): "))

		usrBMI = functions.BMICalc(weightInput, heightInput)

		print("\nBMI:", usrBMI)
		if usrBMI <= 18.5:
			print("You are underweight.")
		elif usrBMI < 25:
			print("You are at a normal weight.")
		elif usrBMI < 30:
			print("You are overweight.")
		else:
			print("You are obese.")
	elif usrInput == 2:
		print("\n\n### Retirement Calculator ###\n\n")
		usrAge = int(input("Current age: "))
		usrSalary = int(input("Annual salary: "))
		savePerc = int(input("Savings percentage: "))
		saveGoal = int(input("Savings goal amount: "))

		goalAge = int(functions.retCalc(usrAge, usrSalary, savePerc, saveGoal))

		print("Age you will meet your goal:", goalAge)
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

		distRes = functions.distCalc(loc1X, loc2X, loc1Y, loc2Y)

		print("Distance between the two points:", distRes)
	elif usrInput == 4:
		print("\n\n### Email Verifier ####\n\n")
		emailInput = input("What email would you like to verify? ")
		
		if functions.emailVerify(emailInput):
			print(emailInput + " is a valid email address.")
		else:
			print(emailInput + " is not a valid email address.")

print("\nExiting...")