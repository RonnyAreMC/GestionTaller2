"""Pruebas automáticas del módulo calculadora usando pytest."""

import pytest

from calculadora import suma, resta, multiplicacion, division


def test_suma():
    assert suma(5, 3) == 8


def test_suma_negativos():
    assert suma(-2, -3) == -5


def test_resta():
    assert resta(10, 4) == 6


def test_multiplicacion():
    assert multiplicacion(6, 7) == 42


def test_division():
    assert division(20, 5) == 4


def test_division_entre_cero():
    with pytest.raises(ValueError):
        division(10, 0)
