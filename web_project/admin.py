from django.contrib import admin

from .models import VIAPerson, SOSUPerson, Drink, Food, Fruit, CreditCard, MobilePay, Order

admin.site.register(VIAPerson)
admin.site.register(SOSUPerson)
admin.site.register(Drink)
admin.site.register(Food)
admin.site.register(Fruit)
admin.site.register(CreditCard)
admin.site.register(MobilePay)
admin.site.register(Order)