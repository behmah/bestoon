from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^submit/expense/$', views.submit_expense, name='sub_expense'),
    re_path(r'^submit/income/$', views.submit_income, name='sub_income'),
]