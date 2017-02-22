import module  
import pytest
class TestClass:

    def test_function_1(self):
        # Override the Python built-in input method 
        module.input = lambda:"x" #'some_input' 
        # Call the function you would like to test (which uses input)
        output = module.function()  
        assert output == "x" #'expected_output'

    def test_function_2(self):
        module.input = lambda: 2.5336#'some_other_input'
        output = module.function()  
        assert output == 2.5336#'another_expected_output'        

    def teardown_method(self, method):
        # This method is being called after each test case, and it will revert input back to original function
        module.input = input

        
@pytest.mark.paramatrize("imp1, imp2, out"[
    ( 250, 72, 33.9),
    ( 150, 50, 30)] )
        
def testBMI(imp1,imp2, out):
        output = module.BMICalc(imp1,imp2)
        assert output == out
'''       
@pytest.mark.paramatrize("retImp1, retImp2, retImp3, retOut"[
    ( 250, 72, 33.9),
    ( 150, a, 30)] )
        
def testRET(retImp1, retImp2, retImp3, retOut):
        output = module.retCalc(retImp1, retImp2, retImp3)
        assert output == retOut
        
def testDist(self):
        output = module.distCalc(2.5,4,3,6.36)
        assert output == 2.14
def testEmail(self):
        output = module.emailVerify("hello@yahoo.com")
        assert output == True
'''
