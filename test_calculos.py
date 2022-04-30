from Calculos import suma
from Calculos import resta
from Calculos import multiplicacion
from Calculos import division

def test_suma():
    assert suma(2,2) == 4

def test_resta():
    assert resta(3,2) == 8

def test_multiplicacion():
     assert multiplicacion (7*3) == 21

def test_division():
    assert division (10/5) == 2
