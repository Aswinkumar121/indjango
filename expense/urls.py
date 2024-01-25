from django.urls import path
from . import views

urlpatterns=[
    path('', views.home, name = "home"),
    path("ExpenseList",views.expenseList, name="expenselist"),
    path("CreateExpense",views.handleExpense, name="createExpense"),
    path('editExpense/<int:id>', views.editExpense, name='editExpense'),
    path('updateExpense/<int:id>',views.updateExpense,name = 'update'),
    path('deletExpense/<int:id>',views.destroy,name='destroy'),
    path('loginExpense',views.loginExpense, name='login'),
   

  
]