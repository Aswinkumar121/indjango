from django.contrib import admin

from .models import *
from django.contrib.auth.admin import UserAdmin




class ExpenseAdmin (admin.ModelAdmin):
    list_display = ('name','category','date','description','amount',)


admin.site.register(Expense,ExpenseAdmin)


