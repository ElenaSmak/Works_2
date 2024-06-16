import pytest
from string_utils import StringUtils
    
@pytest.mark.parametrize('string, result', [('звезда', 'Звезда'), ('идет дождь', 'Идет дождь'), ('1000', '1000')])  # доработка домашки  
def test_capitilize_positive(string, result):
    string_utils = StringUtils()
    res = string_utils.capitilize(string)
    assert res == result

@pytest.mark.xfail  # доработка домашки 
def test_capitilize_negative1():
    string_utils = StringUtils() 
    res = string_utils.capitilize('')
    assert res == ''   

@pytest.mark.xfail  # доработка домашки 
def test_capitilize_negative1():
    string_utils = StringUtils() 
    res = string_utils.capitilize(' ')
    assert res == ' '       
       

@pytest.mark.xfail
def test_capitilize_negative3():
    string_utils = StringUtils() 
    res = string_utils.capitilize(1000)
    assert res == 1000
   
@pytest.mark.xfail
def test_capitilize_negative4():
    string_utils = StringUtils() 
    res = string_utils.capitilize(None)
    assert res == None
    
@pytest.mark.parametrize('string, result', [('  Дождь', 'Дождь'), ('  1000', '1000'), ('  ',''), ('  идет дождь', 'идет дождь')])   
def test_trim_positive(string, result):
    string_utils = StringUtils()
    res = string_utils.trim(string)
    assert res == result    
    
@pytest.mark.xfail
def test_trim_negative1():
    string_utils = StringUtils() 
    res = string_utils.trim('')
    assert res == ''     

@pytest.mark.xfail
def test_trim_negative2():
    string_utils = StringUtils() 
    res = string_utils.trim(1000)
    assert res == 1000       

@pytest.mark.xfail
def test_trim_negative3():
    string_utils = StringUtils() 
    res = string_utils.trim(None)
    assert res == None    

@pytest.mark.parametrize('string, delimeter, result', [('',',',[]), ('дом, дождь', ',', ["дом", " дождь"]), ('дом:дождь',':', ["дом", "дождь"])])  
def test_to_list_positive(string, delimeter, result):
    string_utils = StringUtils()
    res = string_utils.to_list(string, delimeter)
    assert res == result    
    
@pytest.mark.xfail
def test_to_list_negative1():
    string_utils = StringUtils() 
    res = string_utils.to_list(1,2,3,4,5)
    assert res == [1,2,3,4,5]    

@pytest.mark.xfail
def test_to_list_negative2():
    string_utils = StringUtils() 
    res = string_utils.to_list(None)
    assert res == None     

@pytest.mark.parametrize('string, symbol, result', [('Дождь','д', True), ('Дождь', 'а', False), ('1000', '1', True)])  # доработка домашки  
def test_contains_positive(string, symbol, result):
    string_utils = StringUtils()
    res = string_utils.contains(string, symbol)
    assert res == result   

@pytest.mark.xfail
def test_contains_negative1():
    string_utils = StringUtils() 
    res = string_utils.contains(1000, 1)
    assert res == True    

@pytest.mark.xfail
def test_contains_negative2():
    string_utils = StringUtils() 
    res = string_utils.contains(None, None)
    assert res == True     

@pytest.mark.parametrize('string, symbols, result', [('Дожвдь','в', True), ('Дождьдь', 'дь', True)])  
def test_delete_symbol_positive(string, symbols, result):
    string_utils = StringUtils()
    res = string_utils.contains(string, symbols)
    assert res == result  
      
@pytest.mark.parametrize('string, symbol, result', [('Дождь','Д', True), ('Дождь', 'х', False)])  
def test_starts_with_positive(string, symbol, result):
    string_utils = StringUtils()
    res = string_utils.starts_with(string, symbol)
    assert res == result  

# доработка домашки - все тесты ниже
@pytest.mark.parametrize('string, symbol, result', [('ОКо','о', 'ОК'), ('Дождть', 'т','Дождь' )])  
def test_delete_symbol_fix(string, symbol, result):
    string_utils = StringUtils()
    res = string_utils.delete_symbol(string, symbol)
    assert res == result     

@pytest.mark.parametrize('string, symbol, result', [('Дождь','ь', True), ('Дождь', 'х', False)])  
def test_end_with_positive(string, symbol, result):
    string_utils = StringUtils()
    res = string_utils.end_with(string, symbol)
    assert res == result      

@pytest.mark.parametrize('string, result', [('  ', True), ('Дождь', False)])  
def test_is_empty_positive(string, result):
    string_utils = StringUtils()
    res = string_utils.is_empty(string)
    assert res == result      

@pytest.mark.parametrize('list, joiner, result', [([1,2,3,4], ',', '1, 2, 3, 4'), (['дождь', 'снег'], ';', 'дождь; снег' )])  
def list_to_string_positive(list, joiner, result):
    string_utils = StringUtils()
    res = string_utils.list_to_string(list, joiner)
    assert res == result    