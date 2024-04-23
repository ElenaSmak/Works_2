from smartphone import Smartphone

phone1 = Smartphone("Apple", "15", "+49000000000") #Наполняем список пятью разными экземплярами класса Smartphone
phone2 = Smartphone("Apple", "14", "+49000000001")
phone3 = Smartphone("Apple", "13", "+49000000002")
phone4 = Smartphone("Apple", "12", "+49000000003")
phone5 = Smartphone("Apple", "11", "+49000000004")

catalog = [phone1,phone2,phone3,phone4,phone5]
for phone in catalog:
    print(phone.phone_brand,"-",phone.phone_model,".",phone.phone_number," ")
  