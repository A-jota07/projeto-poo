from abc import ABC, abstractmethod


class Abstract(ABC):
    def template_method(self):
        self.hook()
        self.operation1()
        self.base_class_method()
        self.operation2()

    def hook(self): pass

    def base_class_method(self):
        print('Ola eu sou da classe abstrata')

    @abstractmethod
    def operation1(self): pass

    @abstractmethod
    def operation2(self): pass


class ConcreteClass1(Abstract):
    def hook(self):
        print('Utilizando o hook')

    def operation1(self):
        print('Operação 1 concluida')

    def operation2(self):
        print('Operação 2 concluida')


class ConcreteClass2(Abstract):
    def operation1(self):
        print('Operação 1 concluida (Maneira diferente)')

    def operation2(self):
        print('Operação 2 concluida (Maneira diferente)')


if __name__ == '__main__':
    c1 = ConcreteClass1()
    c1.template_method()
    print()

    c2 = ConcreteClass2()
    c2.template_method()
