from __future__ import annotations

from copy import deepcopy
from dataclasses import dataclass
from typing import List

# Ingredientes


@dataclass
class Ingredient:
    price: float


@dataclass
class Bread(Ingredient):
    price: float = 1.50


@dataclass
class Sausage(Ingredient):
    price: float = 4.99


@dataclass
class Bacon(Ingredient):
    price: float = 7.99


@dataclass
class Egg(Ingredient):
    price: float = 1.50


@dataclass
class Cheese(Ingredient):
    price: float = 6.35


@dataclass
class MashedPotatos(Ingredient):
    price: float = 3.90


@dataclass
class PotatosSticks(Ingredient):
    price: float = 0.50


# hotdogs
class HotDog:
    _name: str
    _ingredients: List[Ingredient]

    @property
    def price(self) -> float:
        return round(sum([ingredient.price for ingredient in self._ingredients]), 2)

    @property
    def name(self) -> str:
        return self._name

    @property
    def ingredients(self) -> List[Ingredient]:
        return self._ingredients

    def __repr__(self) -> str:
        return f'{self.name}({self.price} -> {self.ingredients})'


class SimpleHotDog(HotDog):
    def __init__(self) -> None:
        self._name = 'SimpleHotDog'
        self._ingredients: List[Ingredient] = [
            Bread(),
            Sausage(),
            PotatosSticks()
        ]


class SpecialHotDog(HotDog):
    def __init__(self) -> None:
        self._name = 'SpecialHotDog'
        self._ingredients: List[Ingredient] = [
            Bread(),
            Sausage(),
            Bacon(),
            Egg(),
            Cheese(),
            MashedPotatos(),
            PotatosSticks(),
        ]


# Decorators
class HotDogDecorator(HotDog):
    def __init__(self, hotdog: HotDog) -> None:
        self.hotdog = hotdog

    @property
    def price(self) -> float:
        return self.hotdog.price

    @property
    def name(self) -> str:
        return self.hotdog.name

    @property
    def ingredients(self) -> List[Ingredient]:
        return self.hotdog.ingredients


class BaconDecorator(HotDogDecorator):
    def __init__(self, hotdog: HotDog) -> None:
        super().__init__(hotdog)

        self._ingredient = Bacon()
        self._ingredients = deepcopy(self.hotdog.ingredients)
        self._ingredients.append(self._ingredient)

    @property
    def price(self) -> float:
        return round(sum([ingredient.price for ingredient in self._ingredients]), 2)

    @property
    def name(self) -> str:
        return f'{self.hotdog.name} + {self._ingredient.__class__.__name__}'

    @property
    def ingredients(self) -> List[Ingredient]:
        return self._ingredients


if __name__ == '__main__':
    simple_hotdog = SimpleHotDog()
    decorated_simple_hotdog = HotDogDecorator(simple_hotdog)
    bacon_decorator = BaconDecorator(simple_hotdog)
    print(decorated_simple_hotdog)
    print(bacon_decorator)

    special_hotdog = SpecialHotDog()
    print(special_hotdog)
