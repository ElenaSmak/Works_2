#создан класс  Address . Класс содержит в себе поля: «индекс», «город», «улица», «дом», «квартира».
class Address:
    #index =  'индекс'
    #town  = 'город'
    #street = 'улица'
    #hous  = 'дом'
    #flat = 'квартира'
    def __init__(self, index, town, street, hous, flat):
         self.index = index
         self.town = town
         self.street = street
         self. hous = hous
         self.flat = flat
