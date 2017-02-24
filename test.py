import pytest
import functions

def test_BMI():
	assert functions.BMICalc(100, 60) == 19.527777777777775
	assert functions.BMICalc(200, 90) == 17.358024691358025
	assert functions.BMICalc(12, 23) == 15.947069943289225
	with pytest.raises(ValueError)
                 assert functions.BMICalc("a","b")

def test_Ret():
	assert functions.retCalc(20, 40000, 30, 50000) == 24
	assert functions.retCalc(5, 10, 100, 500) == 55
	assert functions.retCalc(99, 1000, 2, 500) == 124
	assert functions.retCalc(-0, 45, -45, 0) == 0
	with pytest.raises(ValueError)
                 assert functions.retCalc("a", "food", 5, "hello")

def test_Dist():
	assert functions.distCalc(5, 5, 10, 5) == 5
	assert functions.distCalc(1, 50, 120, 3) == 126.84636376341263
	assert functions.distCalc(9999, 12, 3, 45920) == 46990.54221862097
	assert functions.distCalc(-11, -100, 5, 90) == 190.67249408344142

def test_Email():
	assert functions.emailVerify("alc552@msstate.edu") == True
	assert functions.emailVerify("$Asd%!@msstate.edu") == False
	assert functions.emailVerify("@.edu") == False
	assert functions.emailVerify("alc552.msstate@edu") == False
	assert functions.emailVerify(11) == False
