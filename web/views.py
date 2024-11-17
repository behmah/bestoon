from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from web.models import User, Expense, Income
from django.utils import timezone

@csrf_exempt
def submit_expense(request):
    """" User submits an expense"""
    this_token = request.POST.get('token', None)
    amount = request.POST.get('amount', None)
    text = request.POST.get('text', None)
    if 'date' not in request.POST:
        date = timezone.now()
    this_user = User.objects.filter(token__token=this_token).get()
    Expense.objects.create(user=this_user, amount=amount, text=text, date=date)
    return JsonResponse({'status': 'ok'}, encoder=json.JSONEncoder)

@csrf_exempt
def submit_income(request):
    """" User submits an income"""
    this_token = request.POST.get('token', None)
    amount = request.POST.get('amount', None)
    text = request.POST.get('text', None)
    if 'date' not in request.POST:
        date = timezone.now()
    this_user = User.objects.filter(token__token=this_token).get()
    Income.objects.create(user=this_user, amount=amount, text=text, date=date)
    return JsonResponse({'status': 'ok'}, encoder=json.JSONEncoder)
