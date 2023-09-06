import requests
from django.shortcuts import render


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
    country_1 = game.country_1
    country_2 = game.country_2

    context = {
        "context": fetched_countries,
        "country_1": country_1,
        "country_2": country_2,
        "total_score": game.total_score
    }
    return render(request, 'landing.html', context)


def next_move(request):
    user_choice = None
    data_str = request.body.decode('utf-8')
    user_input = data_str.split("my_bool=")[1]
    if user_input == "Less":
        user_choice = False
    else:
        user_choice = True
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
        alert_message = "Sorry, you have lost. Try again!"
        return render(request, 'landing.html', {'alert_message': alert_message})
