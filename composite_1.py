from __future__ import annotations

from abc import ABC, abstractmethod
from typing import List


class BoxStructure(ABC):
    @abstractmethod
    def print_content(self) -> None: pass

    @abstractmethod
    def get_price(self) -> float: pass

    def add(self, child: BoxStructure) -> None: pass

    def remove(self, child: BoxStructure) -> None: pass


class Box(BoxStructure):
    def __init__(self, name: str) -> None:
        self.name = name
        self._children: List[BoxStructure] = []

    def print_content(self) -> None:
        for child in self._children:
            child.print_content()

    def get_price(self) -> float:
        return sum([
            child.get_price() for child in self._children
        ])

    def add(self, child: BoxStructure) -> None:
        self._children.append(child)

    def remove(self, child: BoxStructure) -> None:
        if child in self._children:
            self._children.remove(child)


class Product(BoxStructure):
    def __init__(self, name: str, price: float) -> None:
        self.name = name
        self.price = price

    def print_content(self) -> None:
        print(self.name, self.price)

    def get_price(self) -> float:
        return self.price


if __name__ == '__main__':
    camisa1 = Product('camisa1', 39.90)
    camisa2 = Product('camisa2', 79.90)
    camisa3 = Product('camisa3', 59.99)

    caixa_camisas = Box('Caixa de camisas')
    caixa_camisas.add(camisa1)
    caixa_camisas.add(camisa2)
    caixa_camisas.add(camisa3)
    caixa_camisas.print_content()
