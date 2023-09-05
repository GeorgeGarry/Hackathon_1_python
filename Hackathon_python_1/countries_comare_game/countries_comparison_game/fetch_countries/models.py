# from random import random, shuffle, randint

import random
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
        self.total_score = 0
        tuple_to_list_tmp = []
        for i in range(len(args[0])):
            tuple_to_list_tmp.append(args[0][i])

        random.shuffle(tuple_to_list_tmp)
        self.all_countries = tuple_to_list_tmp
        self.country_1 = [self.all_countries[-1]]
        self.all_countries.pop()
        self.country_2 = self.all_countries  # Copy all countries to country_2

    # Method to move a country from country_2 to country_1
    # def move_country(self):
    #     if self.country_2:
    #         country_to_move = self.country_2.pop()
    #         self.country_1.append(country_to_move)

    def check_fill(self):
        print(len(self.all_countries))
        print(self.country_2)
        print(self.country_1)
        print(len(self.country_2))
        print(len(self.country_1))

    def check_user_win(self, user_input_is_bigger):
        if user_input_is_bigger:
            if self.country_2[-1]["population"] >= self.country_1[-1]["population"]:
                return True
            else:
                return False
        else:
            if self.country_2[-1]["population"] <= self.country_1[-1]["population"]:
                return True
            else:
                return False

    def move_country(self):
        self.country_1.append(self.country_2[-1])
        self.country_2.pop()
        print(self.country_1)
        # print(self.country_2)

    def plus_high_score(self):
        self.total_score += 1

    ######## Лови еще для вьюс функцию для передачи обьектов на фронт через импорт моделей и их функций
# from django.shortcuts import render
# from .models import Game

# def game_view(request):
#     game = Game.objects.first()  
#     context = {
#         'country_1': game.country_1[0],
#         'country_2': game.country_2[-1],
#     }
#     return render(request, 'game.html', context)
