# forms.py
from django import forms
from .models import Expense

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['name', 'category', 'date', 'amount']
    
    category = forms.CharField(required=False)
    date = forms.DateField(required=False)
    amount = forms.DecimalField(required=False)