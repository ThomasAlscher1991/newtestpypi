import src.dasscotest as dasscotest
import numpy as np

def test1():
    h=dasscotest.calciHandler()
    owner=h.getOwner()
    assert owner=="defaultuser"

def test2():
    string="thomas"
    h=dasscotest.calciHandler(string)
    owner=h.getOwner()
    assert owner==string