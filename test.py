# Software Testing and QA - Proj 1
# Alex Cote - alc552
# Ginny Tabor - glt79
# Patrick Boudreaux - pdb145
# Damian Cooper - dcc198

import pytest
import functions

def test_BMI():
	assert functions.BMICalc(100, 60) == 19.527777777777775 #Alex
	assert functions.BMICalc(200, 90) == 17.358024691358025 #Alex
	assert functions.BMICalc(12, 23) == 15.947069943289225 #Alex
	assert functions.BMICalc('a', 23) != 20 #Pat
	assert functions.BMICalc("a","b") == 0 #Ginny

def test_Ret():
	assert functions.retCalc(20, 40000, 30, 50000) == 24 #Alex
	assert functions.retCalc(5, 10, 100, 500) == 55 #Alex
	assert functions.retCalc(99, 1000, 2, 500) == 124 #Alex
	assert functions.retCalc('a', 23,"g", 50) != 20 #Pat
	assert functions.retCalc(-0, 45, -45, 0) == 0 #Pat
	assert functions.retCalc("a", "food", 5, "hello") == 0 #Ginny

def test_Dist():
	assert functions.distCalc(5, 5, 10, 5) == 5 #Alex
	assert functions.distCalc(1, 50, 120, 3) == 126.84636376341263 #Alex
	assert functions.distCalc(9999, 12, 3, 45920) == 46990.54221862097 #Alex
	assert functions.distCalc('a', 23, 200,30) != 20 #Pat
	assert functions.distCalc(-11, -100, 5, 90) == 123.0690862889621 #Ginny

def test_Email():
	assert functions.emailVerify("alc552@msstate.edu") == True #Alex
	assert functions.emailVerify("$Asd%!@msstate.edu") == False #Alex
	assert functions.emailVerify("@.edu") == False #Alex
	assert functions.emailVerify("alc552.msstate@edu") == False #Ginny
	assert functions.emailVerify("alc552.msstateedu") == False #Damian
	assert functions.emailVerify("alc55@edu.msstate") == False #Damian
	assert functions.emailVerify("dddd@dddd") == False #Pat
	assert functions.emailVerify("dddddddddddd@ddddddddd") == False
	assert functions.emailVerify(11) == False #Ginny