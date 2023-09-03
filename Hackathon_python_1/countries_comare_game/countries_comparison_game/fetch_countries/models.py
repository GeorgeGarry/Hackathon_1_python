from random import random

# import requests
from django.db import models


# Create your models here.
# def fetch_random_countries():
#     all_countries = []
#     url = f'https://restcountries.com/v3.1/all?fields=name,flags,population,id'
#     response = requests.get(url)
#
#     if response.status_code == 200:
#         countries = response.json()
#         for i in range(len(countries)):
#             one_country = {
#                 "id": i + 1,
#                 "names": {"common_name": countries[i]['name']['common'],
#                           "official_name": countries[i]['name']['official']
#                           },
#                 "flag": countries[i]['flags']['png'],
#                 "population": countries[i]['population']
#             }
#             all_countries.append(one_country)
#
#         return all_countries
#         # return random.sample(countries)
#     else:
#         print(f"Failed to fetch data. Status code: {response.status_code}")
#         return []
#
#
# all_countries_new = fetch_random_countries()
# # print(fetch_random_countries())
# for i in range(10):
#     print(all_countries_new[i])
