from django.contrib import admin
from .models import Customer, Service, Subscription, Payment

admin.site.register(Customer)
admin.site.register(Service)
admin.site.register(Subscription)
admin.site.register(Payment)