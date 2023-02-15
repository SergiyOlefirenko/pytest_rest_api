import requests
import pytest
from src.generators.player import PlayerLocalization


@pytest.mark.parametrize("status", [
    "ACTIVE",
    "BANNED",
    "DELETED",
    "INACTIVE"
])
def test_data_generation_status(status, get_player_generator):
    print(get_player_generator.set_status(status).build())


@pytest.mark.parametrize("balance", [
    "100",
    "1",
    "0",
    "-1"
])
def test_data_generation_balance(balance, get_player_generator):
    print(get_player_generator.set_balance(balance).build())


@pytest.mark.parametrize("key_to_delete", [
    'balance',
    'account_status',
    'localize',
    'avatar'
])
def test_data_generation_delete_keys(key_to_delete, get_player_generator):
    test_object = get_player_generator.build()
    del test_object[key_to_delete]
    print(test_object)


def test_inner_generator_update(get_player_generator):
    # probably not the best solution
    test_object = get_player_generator.update_inner_generator('localize', 'fr', PlayerLocalization('fr_FR')).build()
    print(test_object)
    # values of inner object/dict can be generated after test object is built 
    test_object['localize']['en'] = PlayerLocalization('en_US').build()
    print(test_object)