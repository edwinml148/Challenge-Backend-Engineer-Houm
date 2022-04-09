"""
Author  : Edwin Mendoza Leon
script : main.py
description : script test fuctions.
"""
from functions import *
from pytest import raises
from requests_module import RequestError,api_response


def test_class_requestError():
    """
    test class RequestError
    """
    assert RequestError.__name__ == "RequestError"


def test_class_requestError_attribute_status_code():
    """
    test class RequestError attribute status_code
    """
    error = RequestError(404, "https://pokeapi.co/api/v2/poke?limit=1/")
    assert error.status_code == 404


def test_class_requestError_attribute_message_simple():
    """
    test class RequestError attribute message simple
    """
    error = RequestError(404, "https://pokeapi.co/api/v2/poke?limit=1/")
    assert error.message == "Error in the request for url: https://pokeapi.co/api/v2/poke?limit=1/"


def test_class_requestError_attribute_message():
    """
    test class RequestError attribute_message
    """
    try:
        api_response("https://pokeapi.co/api/v2/pokemons?limit=1/")
    except RequestError as e:
        assert e.message=="Error in the request for url:https://pokeapi.co/api/v2/pokemons?limit=1/"
        assert e.status_code != 200


def test_get_data_pokemon_name_url():
    """
    test get data pokemon name url
    """
    assert type(get_data_pokemon_name_url()) == list


def test_get_data_pokemons_egg_gropus_raichu_name_url():
    """
    test get data pokemons egg_gropus raichu name_url
    """
    assert type(get_data_pokemons_egg_gropus_raichu_name_url()) == list


def test_get_data_pokemons_type_fighting_name_url():
    """
    test get data pokemons type fighting name url
    """
    assert type(get_data_pokemons_type_fighting_name_url()) == list


def test_number_of_names_with_at_and_double_a():
    """
    test number of names with 'at' and double 'a'
    """
    get_data = get_data_pokemon_name_url()
    assert type(number_of_names_with_at_and_double_a(get_data)) == int


def test_number_of_names_egg_gropus_raichu():
    """
    test number of names egg_gropus raichu
    """
    get_data = get_data_pokemons_egg_gropus_raichu_name_url()
    assert type(number_of_names_egg_gropus_raichu(get_data)) == int


def test_max_and_min_weight_of_type_fighting():
    """
    test max and min weight of type fighting
    """
    get_data = get_data_pokemons_type_fighting_name_url()
    assert type(max_and_min_weight_of_type_fighting(get_data)) == list
