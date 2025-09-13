"""
Calculator app tests
SPDX - License - Identifier: LGPL - 3.0 - or -later
Auteurs : Gabriel C. Ullmann, Fabio Petrillo, 2025
"""

from calculator import Calculator

my_calculator = Calculator()
def test_app():
    assert my_calculator.get_hello_message() == "== Calculatrice v1.0 =="

# TODO: ajoutez les tests
def test_addition():
    assert my_calculator.addition(2, 3) == 5
def test_subtraction():
    assert my_calculator.subtraction(4, 2) == 2
def test_multiplication():
    assert my_calculator.multiplication(2, 2) == 4
def test_division():
    assert my_calculator.division(9, 3) == 3
def test_error():
    assert my_calculator.division(9, 3) == 2

