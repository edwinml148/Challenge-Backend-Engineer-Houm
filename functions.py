
from requests_mod.requests_functions import api_response


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

    # Guardamos en un lista los URL's
    egg_groups_raichu_urls = [ egg_group['url'] for egg_group in egg_groups_raichu ]

    # aplicamos api_response a cada url y extraemos los pokemones
    # que tengan el mismo egg_groups.
    pokemons_egg_gropus_raichu_name_url = [ api_response(url)["pokemon_species"] for url in egg_groups_raichu_urls ] 

    return pokemons_egg_gropus_raichu_name_url


def get_data_pokemons_type_fighting_name_url():
    type = "fighting"
    
    url_pokemon_type =  __ROOT_URL + f"type/{type}"
    fighting_pokemons = api_response(url_pokemon_type)["pokemon"]

    pokemons_type_fighting_name_url = [i['pokemon'] for i in fighting_pokemons]
    
    return pokemons_type_fighting_name_url


def number_of_names_with_at_and_double_a(get_add_names_urls):

    names_with_at_and_double_a = [ name_url['name']  for name_url in get_add_names_urls  if (name_url['name'].count('a') == 2) and name_url["name"].count('at') >= 1  ]
    
    return len( names_with_at_and_double_a )


def number_of_names_egg_gropus_raichu(get_add_names_urls):

    names_pokemons = []
    for name_url in range(len(get_add_names_urls)):
        names_pokemons.append( name_url['name'] for name_url in get_add_names_urls[name_url] )

    return len( set(names_pokemons) )


def max_and_min_weight_of_type_fighting(get_add_names_urls):

    urls_id_less_151 = [ url  for url in get_add_names_urls if ( int(url.split('/')[-2]) <= 151 ) ]

    pokemon_weigths = [ api_response(url)['weight']  for url in urls_id_less_151 ]

    max_weight = max(pokemon_weigths)
    min_weight = min(pokemon_weigths)

    return [max_weight, min_weight]

