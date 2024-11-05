from import ABC,Abstractmethod
class vehicle(ABC):
    @Abstractmethod
    def tyre(self)
        print('tyre')
class car(vehicle):
    def tyre(self)
        print('4')
class bike(vehicle):
    def handle(self)
        print('2')
ktm=bike()
ktm.tyre        