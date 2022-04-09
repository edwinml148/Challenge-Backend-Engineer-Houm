"""
Author  : Edwin Mendoza Leon
script : functions.py
description : script with the api data extraction functions, and specific filtering by question.
"""
from requests_module import api_response

__ROOT_URL = "https://pokeapi.co/api/v2/"

def get_data_pokemon_name_url():
    """
    -> parameters : none.
    -> return : dict type , names and urls of all pokemon.
    """
    url_one_poke = __ROOT_URL + "pokemon?limit=1"
    limit = api_response(url_one_poke)['count']
    url_all_poke = __ROOT_URL + f"pokemon?limit={limit}"
    poke_name_url = api_response(url_all_poke)['results']

    return poke_name_url


def get_data_pokemons_egg_gropus_raichu_name_url():
    """
    -> parameters : none.
    -> return : dict type,names and urls of all pokemons that belong to the same egg_group as raichu
    """
    url_poke_specie = __ROOT_URL + "pokemon-species/raichu"
    egg_groups_raichu = api_response(url_poke_specie)["egg_groups"]
    egg_groups_raichu_urls = [ egg_group['url'] for egg_group in egg_groups_raichu ]
    poke_egg_gropus_raichu_name_url = [ api_response(url)["pokemon_species"]
                                      for url in egg_groups_raichu_urls ]

    return poke_egg_gropus_raichu_name_url


def get_data_pokemons_type_fighting_name_url():
    """
    -> parameters : none.
    -> return : type dict , names and urls of all fighting type pokemon.
    """
    url_poke_type = __ROOT_URL + "type/fighting"
    fighting_poke = api_response(url_poke_type)["pokemon"]
    poke_type_fighting_name_url = [poke_name_url['pokemon'] for poke_name_url in fighting_poke]

    return poke_type_fighting_name_url


def number_of_names_with_at_and_double_a(get_data):
    """
    -> parameters : dict type , names and urls of all pokemon.
    -> return : int type, number of pokemon names with 'at' and double 'a'.
    """
    names_at_double_a = [ name_url['name']  for name_url in get_data
                        if name_url['name'].count('a') == 2 and name_url["name"].count('at') >= 1 ]
    return len(names_at_double_a)


def number_of_names_egg_gropus_raichu(get_data):
    """
    -> parameters : dict type,names and urls of all pokemons that belong
                    to the same egg_group as raichu
    -> return : int type, numbers of unique pokemon names with the same egg_gropus from raichu.
    """
    names_pokemons = []
    for name_url in range(len(get_data)):
        names_pokemons = names_pokemons + [ name_url['name'] for name_url in get_data[name_url] ]

    return len(set(names_pokemons))


def max_and_min_weight_of_type_fighting(get_data):
    """
    -> parameters : type dict , names and urls of the fighting type pokemons
    -> return : list type, maximum and minimum weight of the first generation pokemons
                 (pokemons with id less than 151) fighting type.
    """
    urls_id_less_151 = [ name_url['url'] for name_url in get_data
                       if int(name_url['url'].split('/')[-2]) <= 151 ]

    pokemon_weigths = [ api_response(url)['weight']  for url in urls_id_less_151 ]
    max_weight = max(pokemon_weigths)
    min_weight = min(pokemon_weigths)

    return [max_weight, min_weight]
