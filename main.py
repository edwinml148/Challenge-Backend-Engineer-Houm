"""
Author  : Edwin Mendoza Leon
script : main.py
description : main script where the answers of the questions are printed.
"""
from time import time
import functions as func
from requests_module import RequestError

start_time = time()

try:
    data_first_answer = func.get_data_pokemon_name_url()
    FIRST_ANSWER = func.number_of_names_with_at_and_double_a(data_first_answer)

    data_second_answer = func.get_data_pokemons_egg_gropus_raichu_name_url()
    SECOND_ANSWER = func.number_of_names_egg_gropus_raichu(data_second_answer)

    data_third_answer = func.get_data_pokemons_type_fighting_name_url()
    THIRD_ANSWER = func.max_and_min_weight_of_type_fighting(data_third_answer)

except RequestError as error:
    print(f"\n{error}")
    print("\nTry again...")
else:
    print("\n#### Backend Challenge Houm ####\n")
    print(f"Answer 1 : There are {FIRST_ANSWER} pokemons names with 'at' and double 'a'.")
    print(f"Answer 2 : There are {SECOND_ANSWER} pokemons egg_gropus 'Raichu'.")
    print(f"Answer 3 : The max and min weight of 'fighting' type pokemon are {THIRD_ANSWER}.")

elapsed_time = time() - start_time

print(f"\nElapsed time1: {elapsed_time} seconds")
