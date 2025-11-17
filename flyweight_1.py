from __future__ import annotations

from typing import Dict, List


class Client:
    def __init__(self, name: str) -> None:
        self.name = name
        self._addresses: List = []

        # Extrinsic address
        self._address_number: str
        self._address_detail: str

    def add_address(self, address: Address) -> None:
        self._addresses.append(address)

    def list_addresses(self) -> None:
        for address in self._addresses:
            address.show_address(self._address_number, self._address_detail)


class Address:
    def __init__(self, street: str, neighbourhood: str, zip_code: str) -> None:
        self.street = street
        self.neighbourhood = neighbourhood
        self.zip_code = zip_code

    def show_address(self, address_number: str, address_detail: str) -> None:
        print(self.street, address_number, self.neighbourhood,
              address_detail, self.zip_code)


class AddressFactory:
    _addresses: Dict = {}

    def _ge_key(self, **kwargs) -> str:
        return ''.join(kwargs.values())

    def get_address(self, **kwargs) -> Address:
        key = self._ge_key(**kwargs)

        try:
            address_flyweight = self._addresses[key]
            print('Obj criado')
        except KeyError:
            address_flyweight = Address(**kwargs)
            self._addresses[key] = address_flyweight
            print('Novo obj')

        return address_flyweight


if __name__ == '__main__':
    address_factory = AddressFactory()
    a1 = address_factory.get_address(
        street='Av. Paulista', neighbourhood='Centro', zip_code='11111-11')

    a2 = address_factory.get_address(
        street='Av. Paulista', neighbourhood='Centro', zip_code='11111-11')

    cliente1 = Client('Primeiro cliente')
    cliente1._address_number = '120'
    cliente1._address_detail = 'Apto'
    cliente1.add_address(a1)

    cliente1.list_addresses()
