from django.contrib import admin
from .models import Bill, Order, PaymentMethod

admin.site.register(Order)
admin.site.register(PaymentMethod)
admin.site.register(Bill)

# Register your models here.
