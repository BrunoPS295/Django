from nota.models.base import BaseModel
from django.contrib.auth.models import User

class Account(BaseModel):
    owner = models.ManyToManyField(User, verbose_name = 'Account Owner')
    class Meta:
        abstract = True