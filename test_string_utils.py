import pytest
from string_utils import StringUtils
    
@pytest.mark.parametrize('string, result', [('звезда', 'Звезда'), ('идет дождь', 'Идет дождь'), ('',''), (' ', ' ')])   
def test_capitilize_positive(string, result):
    string_utils = StringUtils()
    res = string_utils.capitilize(string)
    assert res == result
       
@pytest.mark.xfail
def test_capitilize_negative1():
    string_utils = StringUtils() 
    res = string_utils.capitilize('1000')
    assert res == '1000'

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

@pytest.mark.parametrize('string, symbol, result', [('Дождь','д', True), ('Дождь', 'а', False)])  
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