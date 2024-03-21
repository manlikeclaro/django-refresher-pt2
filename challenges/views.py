from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render

challenges = {
    'january': 'January is the first month of the year, typically associated with new beginnings and resolutions.',
    'february': 'February is the second month of the year, known for Valentine\'s Day and being the shortest month.',
    'march': 'March is the third month of the year, often associated with the arrival of spring.',
    'april': 'April is the fourth month of the year, known for its showers bringing May flowers.',
    'may': 'May is the fifth month of the year, usually associated with warmer weather and blooming flowers.',
    'june': 'June is the sixth month of the year, known for the beginning of summer and Father\'s Day.',
    'july': 'July is the seventh month of the year, known for Independence Day in the United States.',
    'august': 'August is the eighth month of the year, often associated with vacations and the end of summer.',
    'september': 'September is the ninth month of the year, known for back-to-school season and the beginning of autumn.',
    'october': 'October is the tenth month of the year, associated with Halloween and the changing colors of leaves.',
    'november': 'November is the eleventh month of the year, known for Thanksgiving in the United States.',
    'december': 'December is the twelfth month of the year, known for Christmas and New Year\'s Eve celebrations.'
}


# Create your views here.


def month_challenge_by_no(request, month):
    if month <= len(challenges):
        months = list(challenges.keys())
        forward_month = months[month - 1]
        return HttpResponseRedirect(f'/challenges/{forward_month}')
    else:
        return HttpResponseNotFound(f'Invalid Month XD!')


def month_challenge(request, month):
    try:
        challenge_text = challenges[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound(f'This month is not supported!')