from typing import Any, Iterable, Iterator, List


class MyIterator(Iterator):
    def __init__(self, collection: List[Any]) -> None:
        self._collection = collection
        self._index = 0

    def __next__(self):
        try:
            item = self._collection[self._index]
            self._index += 1
            return item
        except IndexError:
            raise StopIteration


class MyList(Iterable):
    def __init__(self) -> None:
        self._items: List[Any] = []

    def add(self, value: Any) -> None:
        self._items.append(value)

    def __iter__(self):
        return MyIterator(self._items)

    def __str__(self) -> str:
        return f'{self.__class__.__name__}({self._items})'


if __name__ == '__main__':
    my_list = MyList()
    my_list.add('Luiz')
    my_list.add('Maria')
    my_list.add('Lucas')

    for value in my_list:
        print(value)
