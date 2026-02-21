from .models import *
from django.db.models import Count

def get_countries(request):
    countries = Country.objects.annotate(count_amount=Count('club')).order_by('-count_amount')


    left_countries = []
    right_countries = []

    for i, country in enumerate(countries, start=1):
        if country.club_set.count() == 0:
            break
        if i % 2 == 1:
            left_countries.append(country)
        else:
            right_countries.append(country)





    context = {
        'countries_left': left_countries,
        'countries_right': right_countries,

    }

    return (context)
