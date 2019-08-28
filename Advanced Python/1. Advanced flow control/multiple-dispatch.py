class Planet:
    
    def __init__(self, name, radius, mass, temperature):
        self.name = name
        self.radius = radius
        self.mass = mass
        self.temperature = temperature
        
@property
def name(self):
    return self._name

@name.setter
def name(self, name):
    if not isinstance(name, str):
        raise ValueError('Please enter name in a string format')
    self._name = name
    
        
@property
def radius(self):
    return self._radius

@radius.setter
def radius(self, radius):
    if radius <=0:
        raise ValueError('Please provide proper radius')
    self._radius = radius

        
@property
def mass(self):
    return self._mass

@mass.setter
def mass(self, mass):
    if mass <=0:
        raise ValueError('Please provide valid mass')
    self._mass = mass

        
@property
def temperature(self):
    return self._temperature

@temperature.setter
def temperature(self, temperature):
    self._temperature = temperature
        