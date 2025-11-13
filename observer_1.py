from __future__ import annotations

from abc import ABC, abstractmethod
from ast import Dict
from typing import List


class IObservable(ABC):
    @property
    @abstractmethod
    def state(self): pass

    @abstractmethod
    def add_observer(self, observer: IObserver) -> None: pass
    
    @abstractmethod
    def remove_observer(self, observer: IObserver) -> None: pass
    
    @abstractmethod
    def notify_observer(Self) -> None: pass
    
    
class WeatherStation(IObservable):
    def __init__(self):
        self._observers: List[IObserver] = []
        self._state: Dict = {}
       
    @property
    def state(self):
        return self._state
        
    @state.setter
    def state(self, state_update: Dict) -> None: 
        new_state: Dict = {**self._state, **state_update}
    
        if new_state != self._state:
            self._state = new_state
            self.notify_observer()
            
    def reset_state(self):
        self._state = {}
        self.notify_observer()
                   
    def add_observer(self, observer: IObserver) -> None:
        self._observers.append(observer)
    
    def remove_observer(self, observer: IObserver) -> None: 
        if observer in self._observers :
            self._observers.remove(observer)
    
    def notify_observer(self) -> None:
        for observer in self._observers:
            observer.update()
            
class IObserver(ABC):
    @abstractmethod
    def update(self) -> None: pass


class Smartphone(IObserver): 
    def __init__(self, name, observable: IObservable) -> None:
        self.name = name
        self.observable = observable
         
    def update(self) -> None: 
        observable_name = self.observable.__class__.__name__
        print(f'{self.name}, o objeto {observable_name} acabou de ser atualizado => {self.observable.state}')

if __name__ == '__main__':
    weather_station = WeatherStation()
    
    smartphone = Smartphone('Iphone 16 pro, 1tb', weather_station)
    smartphone2 = Smartphone('Iphone 17 pro max, 1tb', weather_station)
    
    weather_station.add_observer(smartphone)
    weather_station.add_observer(smartphone2)
    
    weather_station.state = {'temparature': '30'}
    weather_station.state = {'temparature': '32' }
    
    weather_station.remove_observer(smartphone2)
    weather_station.reset_state()
