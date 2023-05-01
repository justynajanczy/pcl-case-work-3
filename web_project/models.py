from django.db import models
from enum import Enum

class Customer(models.Model):
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

class VIAPerson(Customer):
    VIAId = models.CharField(max_length=200, null=True)
    
class SOSUPerson(Customer):
    SOSUId = models.CharField(max_length=200, null=True)

class DrinkSize(Enum):
    S = "SMALL"
    M = "MEDIUM"
    L = "LARGE"

class FoodType(Enum):
    B = "BREAKFAST"
    L = "LUNCH"
    D = "DINNER"

class FruitType(Enum):
    A = "APPLE"
    B = "BANANA"
    P = "PEAR"

class Product(models.Model):
    name = models.CharField(max_length=200, null=True)
    price = models.CharField(max_length=200, null=True)
    # type = models.CharField(max_length=200, null=True, default='')
    # size = models.CharField(max_length=200, null=True, default='')

    def __str__(self):
        return self.name
    
class Drink(Product):
    DRINKTYPE = (
        # ('Orange Juice', 'Orange Juice'),
        # ('Apple Juice', 'Apple Juice'),
        # ('Grapefruit Juice', 'Grapefruit Juice'),
        # ('Black tea', 'Black tea')
        ('Coffee', 'Coffee'),
        ('Tea', 'Tea'),
        ('Juice', 'Juice')
    )
#    O = "ORANGE JUICE"
#    A = "APPLE JUICE"
#    R = "GRAPEFRUIT JUICE"
#    B = "BLACK TEA"
#    G = "GREEN TEA"
#    W = "WHITE TEA"
#    M = "AMERICANO"
#    E = "ESPRESSO"
#    L = "LATTE"


    type = models.CharField(
        max_length=200,
        choices=DRINKTYPE,
        null=True
    )

    size = models.CharField(
        max_length=200,
        choices=[(tag.name, tag.value) for tag in DrinkSize],
        null=True
    )    

    def __str__(self):
        return self.name + ' ' + self.size

class Food(Product):
    type = models.CharField(
        max_length=200,
        choices=[(tag.name, tag.value) for tag in FoodType],
        null=True
    )
    # test = models.CharField(max_length=200, null=True)

class Fruit(Product):
    # test = models.CharField(max_length=200, null=True)

    type = models.CharField(max_length=200, null=True, default='Fruit')

class Payment(models.Model):
    name = models.CharField(max_length=200, null=True)
    amount = models.CharField(max_length=200, null=True)
    def __str__(self):
        return self.name



class CreditCard(Payment):
   bankAccount = models.CharField(max_length=200, null=True)
#    def __str__(self):
#         return "Credit card " + self.bankAccount

class MobilePay(Payment):
   phoneNumber = models.CharField(max_length=200, null=True)
#    def __str__(self):
#         return "Mobile pay " + self.phoneNumber

class Order(models.Model):
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL) 
    product = models.ManyToManyField(Product)
    payment = models.ForeignKey(Payment, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
