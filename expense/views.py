from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate, login
from . forms import *
from django.contrib.auth.decorators import login_required
from .models import *
from datetime import datetime
from django.db.models import Q
from django.contrib.auth.decorators import user_passes_test

from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.
def home(request):
    return render(request, 'index.html')
"""
def expenseList(request):
    Exp= Expense.objects.filter(created_by=request.user)
    return render(request, 'expenseList.html',{"Expense":Exp})
"""
def is_expense_creator_or_superuser(user):
    return user.is_superuser or user.groups.filter(name='ExpenseCreator').exists()

@user_passes_test(is_expense_creator_or_superuser, login_url='/loginExpense')
def expenseList(request):

    if request.method == 'POST' and 'logout' in request.POST:
        logout(request)
        return redirect('loginExpense')  # Replace 'your_login_url' with the actual URL pattern name for your login view
        
    date_filter = request.GET.get('date_filter')
    expense_name_filter = request.GET.get('expense_name_filter')

    expenses = Expense.objects.filter(created_by=request.user)

    if date_filter:
        try:
            date_filter = datetime.strptime(date_filter, '%Y-%m-%d').date()
            expenses = expenses.filter(date=date_filter)
        except ValueError:
            # Handle invalid date format if needed
            pass

    if expense_name_filter:
        expenses = expenses.filter(name__icontains=expense_name_filter)

   

    return render(request, 'expenseList.html', {"Expense": expenses, "is_creator": True})




def handleExpense(request):
    if request.method == "POST":
        form = ExpenseForm(request.POST)
        if form.is_valid():
            # Save the form data to the database
            expense = form.save(commit=False)
            expense.created_by = request.user  # Assuming you have user authentication
            expense.save()
            messages.success(request, 'Expense added successfully!')
            return redirect('expenselist')  # Redirect to the expense list page after successful form submission
        else:
            messages.error(request, 'Expense creation failed. Please check the form.')
    
    else:
        form = ExpenseForm()

    return render(request, 'createExpense.html', {'form': form})

def editExpense(request,id):
    expense = Expense.objects.get(id=id)
    return render(request,'editExpense.html',{'expense': expense})

def updateExpense(request, id):
    if request.method == "POST":
        expense = Expense.objects.get(id=id)
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            messages.success(request, 'Expense updated successfully!')
            return redirect('expenselist')  # Redirect to your expense list or home page
        else:
            messages.error(request, 'Expense update failed. Please check the form.')
        print(form.errors)

    return render(request,"editExpense.html",{"expense": expense}) 

def destroy (request, id):
    """expense = Expense.objects.get(id=id)
    expense.delete()
    messages.warning(request, 'Expense deleted successfully!')
    return redirect('expenselist')"""
    expense = get_object_or_404(Expense, id=id)

    if request.method == 'POST':
        expense.delete()
        messages.warning(request, 'Expense deleted successfully!')
        return redirect('expenselist')

    return render(request, 'confirm_delete.html', {'expense': expense})

def loginExpense (request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome, {username}!')
                return redirect('expenselist')  # Replace with your desired redirect URL
            
        
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})


    
