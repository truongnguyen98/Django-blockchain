
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver

links =  [
    ('producer', 'Producer'),
    ('shipper', 'Shipper'),
    ('wholesaler', 'Wholesaler'),
    ('detailer', 'Detailer'),
    ]

class UserProfile(AbstractUser):
    widget = models.CharField(max_length=20, choices=links,verbose_name="Choose your link",default=links[0])

    def get_link(self):
        return self.widget


