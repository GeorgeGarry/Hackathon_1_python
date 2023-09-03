import json
import requests
from django.shortcuts import render
from django.http import JsonResponse
from .models import Game

# Create your views here.
def generate_main_page(request):
    def fetch_random_countries():
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
            game = Game(all_countries)
            game.check_fill()

            return all_countries
            # return random.sample(countries)
        else:
            print(f"Failed to fetch data. Status code: {response.status_code}")
            return []

    fetched_countries = fetch_random_countries()
    # print(fetched_countries)
    context = {
        "context": fetched_countries,
        "country_1": "Israel",
        "country_2": "Panama",
    }
    return render(request, 'index.html', context)


# def call_custom_function(request):
#     # print(request)
#     print("it worked! haleluja!")
#     return "<h1>it worked! haleluja!</h1>"


def call_custom_function(request):
    # Decode the bytes object into a string
    data_str = request.body.decode('utf-8')
    print("data_str: ", data_str)
    # Parse the string as JSON
    data_json = json.loads(data_str)
    print("data_json: ", data_json)
    # Your logic here
    result = "This is a response from the Django view."
    return JsonResponse({'country_1': result})
