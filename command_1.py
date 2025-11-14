from __future__ import annotations

from abc import ABC, abstractmethod
from ast import Dict


class Light:
    """ Receiver - Luz Inteligente """
    
    def __init__(self, name: str, room_name: str) -> None:
        self.name = name
        self.room_name = room_name
        self.color = 'Deafault color'
        
        
    def on(self) -> None:
        print(f'{self.name} in {self.room_name} is now ON')
        
    def off(self) -> None:
        print(f'{self.name} in {self.room_name} is now OFF')
        
    def change_color(self, color: str) -> None:
        self.color = color
        print(f'{self.name} in {self.room_name} is now {self.color}')
        

class ICommand(ABC):
    """ Interface de comando """
    
    @abstractmethod
    def execute(self) -> None:
        pass
    
    @abstractmethod
    def undo(self) -> None: 
        pass
    

class LightOnCommand(ICommand):
    """ Comando concreto """
    
    def __init__(self, light: Light) -> None:
        self.light = light
        
    
    def execute(self) -> None:
        self.light.on()
    
    def undo(self) -> None: 
        self.light.off()
        

class RemoteControler:
    """ Invoker """
    
    def __init__(self) -> None:
        self._buttons: Dict[str, ICommand] = {}
        
    def button_add_command(self, name: str, command: ICommand) -> None:
        self._buttons[name] = command
    
    def button_pressed(self, name: str) -> None:
        if name in self._buttons:
            self._buttons[name].execute()
            
    def button_pressed_again(self, name: str) -> None:
        if name in self._buttons:
            self._buttons[name].undo()
        
    
        
if __name__ == '__main__':
    bedroom_light = Light('Luz', 'quarto')
    bathroom_light = Light('Luz', 'banheiro')
    
    bedroom_light_on = LightOnCommand(bedroom_light)
    bathroom_light_on = LightOnCommand(bathroom_light)
    
    remote = RemoteControler()
    remote.button_add_command('first_button', bedroom_light_on)
    
    remote.button_pressed('first_button')
    remote.button_pressed_again('first_button')