__all__ = ['_displayOne', 'register', 'getRegistry', '_registry']

def _displayOne():
    print('display method from subpackage_two')


class One:
    def __init__(self):
        pass
    def oneDisplay(self):
        print('Hello , i am subpackage_one')
        
        
_registry = []

def register(name):
    _registry.append(name)
    
def getRegistry():
    return _registry
    

