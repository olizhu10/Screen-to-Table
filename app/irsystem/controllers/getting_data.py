import json
import pandas as pd
import csv

with open('./data/recipe_data/allergy_dict.json') as f:
    allergy_dict = json.load(f)
with open('./data/movie_script_list.txt') as f:
    titles = [line.rstrip('\n ') for line in f.readlines()]
with open('./data/recipe_data/review_keywords.json') as f:
    review_keywords = json.load(f)
with open('./data/movie_food_quotes.json') as f:
    quotes = json.load(f)

# load data
with open('./data/movie_food_words_from_wordnets_top2_edited_2.json') as f:
    movie_list = json.load(f)
with open('./data/recipe_data/clean_recipes.csv') as f:
    csvreader = csv.DictReader(f, delimiter=';')
    recipes = []
    for row in csvreader:
        recipes.append(row)
with open('./data/movie_recipe_mat_top2_edited_2.csv') as f:
    csvreader = csv.reader(f, delimiter=',')
    movie_recipe_mat = []
    for row in csvreader:
        movie_recipe_mat.append(row)
with open('./data/average_reviews.json') as f:
    reviews = json.load(f)