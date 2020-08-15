import os
from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth import get_user_model

User = get_user_model()


class OfficeModel(models.Model):
    class Meta:
        db_table = 'office'

    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=20)
    phone = models.CharField(max_length=10, blank=True,
                             validators=[RegexValidator('^([0])(\d{9})$', 'not valid phone number')])
    price = models.IntegerField()
    users = models.ManyToManyField(User, related_name='offices')
    photo = models.ImageField(upload_to=os.path.join('office', 'img'), default='', blank=True)

    def __str__(self):
        return self.name
