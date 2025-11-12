from abc import ABC, abstractmethod


class Veiculo(ABC):
    @abstractmethod
    def buscar_cliente(self) -> None: 
        pass

class CarroLuxo(Veiculo):
    def buscar_cliente(self) -> None:
        print('Carro de luxo está buscando por cliente')

        
class CarroPopular(Veiculo):
    def buscar_cliente(self) -> None:
        print('Carro popular está buscando por cliente')
     
              
class MotoPopular(Veiculo):
    def buscar_cliente(self) -> None:
        print('Moto está buscando por cliente')


class MotoLuxo(Veiculo):
    def buscar_cliente(self) -> None:
        print('Moto de luxo está buscando por cliente')
 
        
class VeiculoFactory(ABC):
    def __init__(self, tipo):
        self.carro = self.get_carro(tipo)
    
    @staticmethod
    @abstractmethod
    def get_carro(tipo: str) -> Veiculo: pass
        
    def buscar_cliente(self):
        self.carro.buscar_cliente()
        
        
class ZonaNorteVeiculoFactory(VeiculoFactory):
    @staticmethod
    def get_carro(tipo: str) -> Veiculo:
        if tipo == 'luxo':
            return CarroLuxo()
        
        if tipo == 'popular':
            return CarroPopular()
        
        if tipo == 'moto':
            return MotoPopular()
        
        if tipo == 'moto_luxo':
            return MotoLuxo()
        assert 0, 'Veiculo indisponivel no momento'
        
        
class ZonaSulVeiculoFactory(VeiculoFactory):
    @staticmethod
    def get_carro(tipo: str) -> Veiculo:
        if tipo == 'popular':
            return CarroPopular()
        assert 0, 'Veiculo indisponivel no momento'
        
if __name__ == '__main__':
    from random import choice
    veiculos_disponiveis_z_n = ['luxo', 'popular', 'moto', 'moto_luxo']
    veiculos_disponiveis_z_s = ['popular']
    
    
    print('===ZONA NORTE===') 
    for i in range(10):
        carro = ZonaNorteVeiculoFactory(choice(veiculos_disponiveis_z_n))
        carro.buscar_cliente()
        
    print()
    print('===================')
    print()
    
    print('===ZONA SUL===') 
    for i in range(10):
        carro2 = ZonaNorteVeiculoFactory(choice(veiculos_disponiveis_z_s))
        carro2.buscar_cliente()