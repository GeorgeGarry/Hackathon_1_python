import json
import requests
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Game

# Create your views here.
def generate_main_page(request):
    def fetch_all_countries():
        all_countries = []
        url = f'https://restcountries.com/v3.1/all?fields=name,flags,population,id'
        response = requests.get(url)

        if response.status_code == 200:
            countries = response.json()
            for i in range(len(countries)):
                one_country = {
                    "id": i + 1,
                    "names": {"common_name": countries[i]['name']['common'],
                              "official_name": countries[i]['name']['official']
                              },
                    "flag": countries[i]['flags']['png'],
                    "population": countries[i]['population']
                }
                all_countries.append(one_country)
            return all_countries
        else:
            print(f"Failed to fetch data. Status code: {response.status_code}")
            return []
    fetched_countries = fetch_all_countries()
    global game
    game = Game(fetched_countries)
    # game.check_fill()
    country_1 = game.country_1
    country_2 = game.country_2
    # print("print in view: ", country_1)

    context = {
        "context": fetched_countries,
        "country_1": country_1,
        "country_2": country_2,
        "total_score": game.total_score
    }
    return render(request, 'landing.html', context)


# def call_custom_function(request):
#     # print(request)
#     print("it worked! haleluja!")
#     return "<h1>it worked! haleluja!</h1>"


def next_move(request):
    # game.check_user_win()
    if game.check_user_win():
        game.move_country()
    context = {
        "country_1": game.country_1,
        "country_2": game.country_2,
    }

    return render(request, 'landing.html', context)

def call_custom_function(request):
    user_choice=None
    data_str = request.body.decode('utf-8')
    user_input = data_str.split("my_bool=")[1]
    if user_input == "Less":
        user_choice = False
    else:
        user_choice = True
    print("user_choice: ", user_choice)
    if game.check_user_win(user_choice):
        game.move_country()
        game.plus_high_score()
        context = {
            "country_1": game.country_1,
            "country_2": game.country_2,
            "total_score": game.total_score
        }

        return render(request, 'landing.html', context)
    else:
        alert_message = "Sorry, you've lost. Try again!"
        return render(request, 'landing.html', {'alert_message': alert_message})

