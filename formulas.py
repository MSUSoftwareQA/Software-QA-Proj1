#/bin/python3
import math

def BMICalc(usrWeight, usrHeight):
	return (usrWeight / ((usrHeight**2) * 703))

def retCalc(usrAge, usrSal, usrSav):
	return (usrAge + math.floor(usrSav / (usrSal * (usrSav / 100))))

def distCalc(x1, x2, y1, y2):
	return (math.sqrt(((x2 - x1)**2) + ((y2 - y1)**2)))

def emailVerify(usrEmail):
	pass

loopProg = True

while loopProg:
	print("0) Exit\n1) BMI Calculator\n2) Retirement\n3) Distance")
	usrInput = int(input("\nWhich would you like to calculate? (0-3) "))
	
	if usrInput == 0:
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


print("\nExiting...")
