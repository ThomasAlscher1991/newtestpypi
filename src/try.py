import dasscotest
import numpy as np
h=dasscotest.calciHandler()

a=np.array([1.,2.,3.])
res=h.addOneToVector(a)
print(h.getOwner(),res)

