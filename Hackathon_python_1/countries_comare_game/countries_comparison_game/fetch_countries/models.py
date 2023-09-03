from random import random, shuffle
# import random
# import requests
from django.db import models


# Create your models here.

class Game(models.Model):
    # Define fields for the Game model
    # You can add any other fields you need

    # Initialize the countries in country_2 (exclude one country)
    def __init__(self, *args, **kwargs):
        super(Game, self).__init__(*args, **kwargs)
        self.country_1 = []  # Initialize an empty list for country_1
        self.country_2 = []  # Initialize an empty list for country_2

        # Logic to populate country_2 initially with all countries except one
        self.all_countries = (list(args)) # Replace with your list of countries
        shuffle(self.all_countries)
        self.country_2 = self.all_countries.pop()  # Copy all countries to country_2
        self.country_1.append(self.country_2.pop())  # Remove and add one country to country_1

    # Method to move a country from country_2 to country_1
    # def move_country(self):
    #     if self.country_2:
    #         country_to_move = self.country_2.pop()
    #         self.country_1.append(country_to_move)

    def check_fill(self):
        print(self.all_countries)
        # print("country_2:", self.country_2)
        # print("country_1:", self.country_1)
