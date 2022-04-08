
from requests_mod.requests_functions import api_response
import json
import pprint
import time


__ROOT_URL = "https://pokeapi.co/api/v2/"

def get_data_pokemons_name_url():

    url_one_pokemon = __ROOT_URL + f"pokemon?limit=1"
        
    limit = api_response(url_one_pokemon)['count']

    url_all_pokemon = __ROOT_URL + f"pokemon?limit={limit}"
    pokemons_name_url = api_response(url_all_pokemon)['results']

    return pokemons_name_url


def get_data_pokemons_egg_gropus_raichu_name_url():
    # Extraemos los grupos al cual pertenece Raichu
    url_pokemon_specie = __ROOT_URL + f"pokemon-species/raichu"
    egg_groups_raichu = api_response(url_pokemon_specie)["egg_groups"]

    print(egg_groups_raichu)
    # Guardamos en un lista los URL's
    egg_groups_raichu_urls = [ egg_group['url'] for egg_group in egg_groups_raichu ]

    # aplicamos api_response a cada url y extraemos los pokemones
    # que tengan el mismo egg_groups.
    pokemons_egg_gropus_raichu_name_url = [ api_response(url)["pokemon_species"] for url in egg_groups_raichu_urls ] 

    return pokemons_egg_gropus_raichu_name_url


def get_data_pokemons_fighting_name_url():
    type = "fighting"
    
    url_pokemon_type =  __ROOT_URL + f"type/{type}"
    fighting_pokemons = api_response(url_pokemon_type)["pokemon"]

    pokemons_fighting_name_url = [i['pokemon'] for i in fighting_pokemons]
    
    return pokemons_fighting_name_url



pprint.pprint(get_data_pokemons_name_url())
pprint.pprint(get_data_pokemons_egg_gropus_raichu_name_url())
pprint.pprint(get_data_pokemons_fighting_name_url())


