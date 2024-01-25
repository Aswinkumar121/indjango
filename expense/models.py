from django.db import models
from django.contrib.auth.models import AbstractUser,User,Group

import datetime
import os
from django.conf import settings




class Expense (models.Model):
    name = models.CharField(max_length=150,null=False,blank=False)
    date = models.DateField()
    category = models.CharField(max_length=50, choices=[('Health', 'Health'), ('Electronics', 'Electronics'), ('Travel', 'Travel'), ('Education', 'Education'), ('Books', 'Books'), ('Others', 'Others')])
    description = models.TextField()
    amount = models.PositiveIntegerField()
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    """def save(self, *args, **kwargs):
        if not self.created_by:
            self.created_by = kwargs.pop('user', None)
        super(Expense, self).save(*args, **kwargs)"""

    def __str__(self):
        return self.name    

Group.objects.get_or_create(name='ExpenseCreator')  # Users who can create expenses
Group.objects.get_or_create(name='ExpenseAdmin')


