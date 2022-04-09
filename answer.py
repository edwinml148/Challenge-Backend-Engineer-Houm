"""
Author  : Edwin Mendoza Leon
script : answer.py
description : main script where the answers of the questions are printed.
"""
import sys
import functions as func

def first():
    """
    This function will print the result of the first exercise.
    """
    data_first_answer = func.get_data_pokemon_name_url()
    answer = func.number_of_names_with_at_and_double_a(data_first_answer)
    print(f"There are {answer} pokemons names with 'at' and double 'a'.")


def second():
    """
    This function will print the result of the second exercise.
    """
    data_second_answer = func.get_data_pokemons_egg_gropus_raichu_name_url()
    answer = func.number_of_names_egg_gropus_raichu(data_second_answer)
    print(f"There are {answer} pokemons that can breed with Raichu.")


def third():
    """
    This function will print the result of the third exercise.
    """
    data_third_answer = func.get_data_pokemons_type_fighting_name_url()
    answer = func.max_and_min_weight_of_type_fighting(data_third_answer)
    print(f"The max and min weight of fighting type pokemon are {answer}.")


def total_questions():
    """
    hola mundo.
    """
    data_first_answer = func.get_data_pokemon_name_url()
    answer_first = func.number_of_names_with_at_and_double_a(data_first_answer)
    print(f"There are {answer_first} pokemons names with 'at' and double 'a'.")

    data_second_answer = func.get_data_pokemons_egg_gropus_raichu_name_url()
    answer_second = func.number_of_names_egg_gropus_raichu(data_second_answer)
    print(f"There are {answer_second} pokemons that can breed with Raichu.")

    data_third_answer = func.get_data_pokemons_type_fighting_name_url()
    answer_third = func.max_and_min_weight_of_type_fighting(data_third_answer)
    print(f"The max and min weight of fighting type pokemon are {answer_third}.")


switcher = {
    "1": first,
    "2": second,
    "3": third,
    "4": total_questions,
}

argvs = sys.argv

try:
    functions = switcher[argvs[1]]
    functions()
except KeyError:
    print("Please, enter a valid number of the exercise.")
    print("\n1. number of names with at and double a")
    print("2. number of names egg_gropus raichu")
    print("3. max and min weight of type fighting")
except IndexError:
    print("Please, enter the number of the exercise.")
    print("ex: python3 exercise.py 1")
    print("\n1. number of names with at and double a")
    print("2. number of names egg_gropus raichu")
    print("3. max and min weight of type fighting")
