import requests
from django.shortcuts import render


# Create your views here.
def generate_main_page(request):
    def next_country(country_1, country_2):
        country_2 = country_1
        print("kdfjksdjfbj")

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
        "next_country": next_country
    }
    return render(request, 'index.html', context)

def call_custom_function(request):
    pass
