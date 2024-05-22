import pytest
from calculator import Calculator
calculator = Calculator()

#@pytest.mark.skip  #  маркер
@pytest.mark.xfail
def test_sum_positive_nums():
    calculator = Calculator()    
    res = calculator.sum(4, 5)
    assert res == 9 

def test_sum_negative_nums():
    calculator = Calculator()
    res = calculator.sum(-6, -10)
    assert res == -16

def test_sum_positive_and_negative_nums():
    calculator = Calculator()
    res = calculator.sum(-6, 6)
    assert res == 0  

def test_sum_float_nums():
    calculator = Calculator()
    res = calculator.sum(5.6, 4.3)
    res = round(res, 1)
    assert res == 9.9  

def test_sum_zero_nums():
    calculator = Calculator()
    res = calculator.sum(10, 0)
    assert res == 10  
# на деление
def test_div_positive():
    calculator = Calculator()
    res = calculator.div(10, 2)
    assert res == 5

def test_div_by_zero():
    calculator = Calculator()
    with pytest.raises(ArithmeticError):
         calculator.sum(10, 0)         

#  найти среднее

def test_avg_empty_list():
    calculator = Calculator()
    nums = []
    res = calculator.avg(nums)
    assert res == 0          

def test_avg_positive():
    calculator = Calculator()
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9,5]
    res = calculator.avg(nums)
    assert res == 5   
