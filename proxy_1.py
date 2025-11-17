from __future__ import annotations

from abc import ABC, abstractmethod
from ast import Dict, List
from time import sleep


class IUser(ABC):
    firstname: str
    lastname: str

    @abstractmethod
    def get_addresses(self) -> List[Dict]: pass

    @abstractmethod
    def get_all_user_data(self) -> Dict: pass


class User(IUser):
    def __init__(self, firstname: str, lastname: str) -> None:
        sleep(2)  # simulando requisição
        self.firstname = firstname
        self.lastname = lastname

    def get_addresses(self) -> List[Dict]:
        sleep(2)  # simulando requisição
        return [
            {'rua': 'Avenida das palmeiras', 'numero': 102}
        ]

    def get_all_user_data(self) -> Dict:
        sleep(2)  # simulando requisição
        return [
            {'cpf': '405.452.690-08', 'rg': 360814724}
        ]


class UserProxy(IUser):
    def __init__(self, firstname: str, lastname: str) -> None:
        self.firstname = firstname
        self.lastname = lastname

        self._real_user: User
        self._cache_addresses: List[Dict]
        self._all_user_data: Dict

    def get_user(self) -> None:
        if not hasattr(self, '_real_user'):
            self._real_user = User(self.firstname, self.lastname)

    def get_addresses(self) -> List[Dict]:
        self.get_user()

        if not hasattr(self, '_cache_addresses'):
            self._cache_addresses = self._real_user.get_addresses()
        return self._cache_addresses

    def get_all_user_data(self) -> Dict:
        self.get_user()

        if not hasattr(self, '_all_user_data'):
            self._all_user_data = self._real_user.get_all_user_data()
        return self._all_user_data


if __name__ == '__main__':
    usuario = UserProxy('Joao', 'Pedro')

    print(usuario.firstname, usuario.lastname)
    print(usuario.get_all_user_data())
    print(usuario.get_addresses())

    for i in range(10):
        print(usuario.get_addresses())
