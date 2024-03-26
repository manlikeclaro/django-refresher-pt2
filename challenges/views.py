from django.http import Http404, HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse

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
    'december': None
}


# Create your views here.
def index(request):
    months = list(challenges.keys())

    return render(request, "challenges/index.html", {
        "months": months
    })


def trial(request):
    month_list = list(challenges.keys())
    # month_list = [key.capitalize() for key in challenges.keys()]
    redirect_paths = []

    for item in month_list:
        redirect_path = reverse('month-challenge', args=[item])
        redirect_paths.append(redirect_path)

    # response_data = {
    #     'months' : month_list,
    #     'redirect_paths' : redirect_paths
    # }
        
    # Zip the lists together
    zipped_data = zip(month_list, redirect_paths)
    # zipped_data = zip([item.capitalize() for item in month_list], redirect_paths)

    response_data = {
        'zipped_data': zipped_data
    }

    return render(request, 'challenges/challenge.html', context=response_data)


def month_challenge_by_no(request, month):
    if month <= len(challenges):
        months = list(challenges.keys())
        forward_month = months[month - 1]
        # return HttpResponseRedirect(f'/challenges/{forward_month}')

        redirect_path = reverse('month-challenge', args=[forward_month])
        # return HttpResponseRedirect(f'{redirect_path}')
        return redirect(redirect_path)

    else:
        return HttpResponseNotFound(f'Invalid Month XD!')


def month_challenge(request, month):
    try:
        challenge_text = challenges[month]
        month_text = month
        # return HttpResponse(challenge_text)

        # response_data = f'<h1>{challenge_text}</h1>'
        # return HttpResponse(response_data)

        response_data = {
            'challenge_text': challenge_text,
            'month_text': month_text.capitalize()
        }

        return render(request, 'challenges/single-challenge.html', context=response_data)

    except:
        # return HttpResponseNotFound(f'This month is not supported!')
        raise Http404()
