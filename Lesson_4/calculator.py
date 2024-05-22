class Calculator:  # калькулятор
    def sum(self, a, b):  #сложение
        result = a + b
        return result
    
    def sub(self, a, b):  # вычитание
        result = a - b
        return result
    
    def mul(self, a, b):  # умножение
        return a*b
    
    def div(self, a, b ):  # деление с проверкой деления на ноль
        if (b == 0): 
            raise ArithmeticError("На ноль делить нельзя")
            return a/b
        
    def pow(self, a, b = 2):   # возведение в степень, где по умолчанию возводим в степень 2
        return a**b
    
    def avg(self, nums):  #нахождение среднего
        if (len(nums == 0)):
            return 0
        s = 0
        for num in nums:
            s = self.sum(s, num) 
        l = len(nums)
        return self.div(s, l)

