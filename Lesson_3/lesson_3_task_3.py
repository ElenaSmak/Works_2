
from address import Address
from mailing import Mailing

to_address  =  Address("236040", "г. Москва", "ул. Невская", "25", "15")
from_address = Address("236404", "г. Москва", "ул. Мира", "43", "12")
my_mailing = Mailing (to_address,from_address,1200, "12345")  #создали экземпляр класса
print(f'Отправление {my_mailing.track} из {my_mailing.from_address.index}, {my_mailing.from_address.town}, {my_mailing.from_address.street}, {my_mailing.from_address.hous} - {my_mailing.from_address.flat} в {my_mailing.to_address.index}, {my_mailing.to_address.town}, {my_mailing.to_address.street}, {my_mailing.to_address.hous} - {my_mailing.to_address.flat}. Стоимость {my_mailing.cost} рублей.')


