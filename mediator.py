from __future__ import annotations

from abc import ABC, abstractmethod
from ast import List


class Colleague(ABC):
    def __init__(self, name: str):
        self.name

    @abstractmethod
    def broad_cast(self, msg: str) -> None: pass

    @abstractmethod
    def direct(self, msg: str) -> None: pass


class Person(Colleague):
    def __init__(self, name: str, mediator: Mediator) -> None:
        self.name = name
        self.mediator = mediator

    def broad_cast(self, msg: str) -> None:
        self.mediator.broad_cast(self, msg)

    def direct(self, msg: str) -> None:
        print(msg)


class Mediator(ABC):
    @abstractmethod
    def broad_cast(self, colleague: Colleague, msg: str) -> None:
        pass

    @abstractmethod
    def direct(self, sender: Colleague, receiver: str, msg: str) -> None:
        pass


class ChatRoom(Mediator):
    def __init__(self) -> None:
        self.colleagues: List[Colleague] = []

    def is_colleague(self, colleague: Colleague) -> bool:
        return colleague in self.colleagues

    def add(self, colleague: Colleague) -> None:
        if not self.is_colleague(colleague):
            self.colleagues.append(colleague)

    def remove(self, colleague: Colleague) -> None:
        if self.is_colleague(colleague):
            self.colleagues.remove(colleague)

    def broad_cast(self, colleague: Colleague, msg: str) -> None:
        if not self.is_colleague(colleague):
            return

        print(f'{colleague.name} disse: {msg}')

    def direct(self, sender: Colleague, receiver: str, msg: str) -> None:
        if not self.is_colleague(sender):
            return

        receiver_obj: List[Colleague] = [
            colleague for colleague in self.colleaguesif if colleague.name == receiver]

        if not receiver_obj:
            return

        receiver_obj[0].direct(
            f'{sender.name} para {receiver_obj[0].name}: {msg}'
        )


if __name__ == '__main__':
    chat = ChatRoom()

    person = Person('João', chat)
    person1 = Person('Maria', chat)
    person2 = Person('Junior', chat)
    person3 = Person('Lucas', chat)

    chat.add(person)
    chat.add(person1)
    chat.add(person2)
    chat.add(person3)

    person.broad_cast('Olá pessoas')
    person1.broad_cast('Opa')
    person2.broad_cast('Eai')
    person3.broad_cast('Eai')
