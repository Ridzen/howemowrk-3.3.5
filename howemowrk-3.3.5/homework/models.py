from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class CustomerUser(AbstractUser):
    birth_date = models.DateField()
    balance = models.IntegerField()
    user_type = models.CharField(choices=('courier', 'staff', 'customer'))


customers = CustomerUser.objects.filter(user_type='customer')
couriers = CustomerUser.objects.filter(user_type='courier')
