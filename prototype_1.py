from __future__ import annotations

from ast import List


class StringReprMixin:
    def __str__(self):
        params = ', '.join([f'{k}={v}' for k, v in self.__dict__.items()])
        
        return f'{self.__class__.__name__}({params})'
        
    def __repr__(self):
        return self.__str__()
    
    
class Person(StringReprMixin):
    def __init__(self,firstname: str, lastname: str) -> None:
        self.firstname = firstname
        self.lastname = lastname
        self.addresses: List[Address] = []
        
    def add_address(self, address) -> None:
        self.addresses.append(address)
        
        
class Address:
    def __init__(self, street: str, number: str) -> None:
        self.street = street
        self.number = number


if __name__ == '__main__':
    name1 = Person('NAME', 'LAST NAME')
    address1 = Address('ADDRESS', 'NUMBER')
    name1.add_address(address1)
    print(name1)