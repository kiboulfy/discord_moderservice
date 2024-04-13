from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Adding(models.Model):
    name = models.CharField(max_length=100)   
    discord_id = models.CharField(max_length=200)
    #person = models.ForeignKey(User, on_delete=models.SET_NULL,
    #null=True, blank=True)

    KNOW_CHOICES =  [
        ('MON', 'Мониторинг'),
        ('METRO', 'Метро'),
        ('RAD', 'Сарафанное радио'),
        ('STICKS', 'Стикеры'),
    ]
    fromWhereKnows = models.CharField(choices=KNOW_CHOICES, max_length=200)

    def __str__(self):
        return self.discord_id
    
    def get_all_info(self):
        return [self.name, self.discord_id, self.fromWhereKnows]
    
    def getKnows(self):
        for choice in self.KNOW_CHOICES:
            if choice[0] == self.fromWhereKnows:
                return choice[1]