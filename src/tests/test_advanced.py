import src.dasscotest as dasscotest
import numpy as np

def test3():
    h=dasscotest.calciHandler()

    a=np.array([1.,2.,3.])
    res=h.addOneToVector(a)
    print(res,a+1)
    assert np.array_equal(res,a+1)
