import random
import json

with open("contries_cities.json", "r") as file:
    countries_cities = json.load(file)

def capital_city_input(country):
    capital_city_input = input(f"Game: What is capital city of {country}? ")

    if capital_city_input.strip().title() == str(countries_cities.get(country, "")):
        print("Correct! Well done.")
    else:
        print(f"Incorrect! The correct answer is {countries_cities.get(country)}.")

random_country = random.choice(list(countries_cities.keys()))        

capital_city_input(random_country)