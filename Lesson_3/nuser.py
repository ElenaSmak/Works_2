#класс User
class User:
    def __init__(self, first_name, last_name): #принимает на вход два параметра имя и фамилию
        print("я создался")
        self.userfirst_name = first_name
        self.userlast_name = last_name
        
       
    def sayfirst_name(self):# метод  
        print("меня зовут",self.userfirst_name)#Передаем имя пользователя 
      
    def saylast_name(self):# метод 
         print("моя фамилия",self.userlast_name )#Передаем фамилию пользователя 

    def sayall_name(self):# метод 
        print(self.userlast_name, self.userfirst_name)#Передаем имя и фамилию пользователя 