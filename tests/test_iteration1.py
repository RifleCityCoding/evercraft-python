import pytest
from src.character import Character

def test_run_iteration1():
    # create character obj
    char = Character('Bob Dos')
    # set the name in the function
    assert char.name is "Bob Dos"

def test_run_iteration1():
    char = Character(name ='Bob Dos', align ='Good')
    assert char.align is 'Good'

def test_character_has_armor():
    # create character
    char = Character('Bob Dos', 'Good')
    # create dice object roll
    roll = Dice.roll()
    # compare dice roll against char armor
    assert char.armor_class == 10