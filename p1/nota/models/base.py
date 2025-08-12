from django.db import models
from nota.models.base import BaseModel
from django.contrib.auth.models import User

app_label = 'nota' 

class Account(BaseModel):
    owner = models.models.ManyToManyField(User, verbose_name=_("Account Owner")) 
    description = models,CharField(max_lenght=200, help_text='Description for your account')
    number = models.CharField(max_length=20, help_text='Insert your account number here')
    balance = models.FloatField(default=0, help_text='Insert your initial balance')
    class Meta:
        abstract = False
    def __str__(self):
        return "{}: {} - {}".format(self.number, self.description,self.balance)
    def update_balance(self, value):
        try:
            self.balance = self.balance + float(value)
            return True
        except:
            return False
    def get_balance(self):
        return self.balance

    