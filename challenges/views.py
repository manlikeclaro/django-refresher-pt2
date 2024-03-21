from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

# Create your views here.


def month_challenge(request, month):
    challenge_text = None
    if month == 'january':
        challenge_text = f'{month} - First month of the year 💀'
    elif month == 'february':
        challenge_text = f'{month} - This is the month of Love! 😍'
    else:
        return HttpResponseNotFound(f'{month} - This month is not supported dumbass! 🙄')

    return HttpResponse(f'{challenge_text}')
