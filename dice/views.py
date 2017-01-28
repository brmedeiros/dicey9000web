from django.shortcuts import render

from .models import DiceRoll

def home(request):
    return render(request, 'dice/home.html')
