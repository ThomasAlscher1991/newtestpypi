import numpy as np
import json
import importlib.resources
class calciHandler():
    def __init__(self,owner=None):
        if owner is None:
            file_path = 'owners.json'
            with importlib.resources.open_text(__package__,file_path) as f:
                data=json.load(f)

            self.__owner=data["default"]
        else:
            self.__owner=owner

    def getOwner(self):
        return self.__owner

    def addOneToVector(self,a):
        new=np.ones(a.shape)
        return a+new

