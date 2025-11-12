from abc import ABC, abstractmethod


class VeiculoLuxo(ABC):
    @abstractmethod
    def buscar_cliente(self) -> None: 
        pass
    
    
class VeiculoPopular(ABC):
    @abstractmethod
    def buscar_cliente(self) -> None: 
        pass

# Norte
class CarroLuxoZN(VeiculoLuxo):
    def buscar_cliente(self) -> None:
        print('Carro de luxo ZN está buscando por cliente')

        
class CarroPopularZN(VeiculoPopular):
    def buscar_cliente(self) -> None:
        print('Carro popular ZN está buscando por cliente')
     
              
class MotoPopularZN(VeiculoPopular):
    def buscar_cliente(self) -> None:
        print('Moto está buscando por cliente')


class MotoLuxoZN(VeiculoLuxo):
    def buscar_cliente(self) -> None:
        print('Moto de luxo ZN está buscando por cliente')
 
        
# Sul
class CarroLuxoZS(VeiculoLuxo):
    def buscar_cliente(self) -> None:
        print('Carro de luxo ZS está buscando por cliente')

        
class CarroPopularZS(VeiculoPopular):
    def buscar_cliente(self) -> None:
        print('Carro popular ZS está buscando por cliente')
     
              
class MotoPopularZS(VeiculoPopular):
    def buscar_cliente(self) -> None:
        print('Moto está buscando por cliente')


class MotoLuxoZS(VeiculoLuxo):
    def buscar_cliente(self) -> None:
        print('Moto de luxo ZS está buscando por cliente')
 
        
class VeiculoFactory(ABC):  
    @staticmethod
    @abstractmethod
    def get_carro_luxo(tipo: str) -> VeiculoLuxo: 
        pass
    
    @staticmethod
    @abstractmethod
    def get_carro_popular(tipo: str) -> VeiculoPopular: 
        pass
    
    @staticmethod
    @abstractmethod
    def get_moto_luxo(tipo: str) -> VeiculoLuxo: 
        pass
    
    @staticmethod
    @abstractmethod
    def get_moto_popular(tipo: str) -> VeiculoPopular: 
        pass
        
     
class ZonaNorteVeiculoFactory(VeiculoFactory):
    @staticmethod
    def get_carro_luxo() -> VeiculoLuxo: 
        return CarroLuxoZN()
    
    @staticmethod
    def get_carro_popular() -> VeiculoPopular: 
        return CarroPopularZN()
    
    @staticmethod
    def get_moto_luxo() -> VeiculoLuxo: 
        return MotoLuxoZN()
    
    @staticmethod
    def get_moto_popular() -> VeiculoPopular: 
        return MotoPopularZN()
        
     
class ZonaSulVeiculoFactory(VeiculoFactory):
    @staticmethod
    def get_carro_luxo() -> VeiculoLuxo: 
        return CarroLuxoZS()
    
    @staticmethod
    def get_carro_popular() -> VeiculoPopular: 
        return CarroPopularZS()
    
    @staticmethod
    def get_moto_luxo() -> VeiculoLuxo: 
        return MotoLuxoZS()
    
    @staticmethod
    def get_moto_popular() -> VeiculoPopular: 
        return MotoPopularZS()
        
class Cliente:
    def busca_clientes(self):
        for factory in [ZonaNorteVeiculoFactory(), ZonaSulVeiculoFactory()]:
            carro_popular = factory.get_carro_popular()
            carro_popular.buscar_cliente()
            
            carro_luxo = factory.get_carro_luxo()
            carro_luxo.buscar_cliente()
            
            moto_popular = factory.get_moto_popular()
            moto_popular.buscar_cliente()
            
            moto_luxo = factory.get_moto_luxo()
            moto_luxo.buscar_cliente()
    
      
if __name__ == '__main__':
    cliente = Cliente()
    cliente.busca_clientes()