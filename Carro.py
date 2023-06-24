class Carro:

    def __init__(self, marca, modelo, ano_fab, preco, estado_novo, alugado):
        self.marca = marca
        self.modelo = modelo
        self.ano_fab = ano_fab
        self.preco = preco
        self.estado_novo = estado_novo
        self.alugado = alugado
    
    #metodos get
    def getMarca(self):
        return self.marca
    
    def getModelo(self):
        return self.modelo
    
    def getAno_fab(self):
        return self.ano_fab
    
    def getPreco(self):
        return self.preco
    
    def getEstado_novo(self):
        return self.estado_novo
    
    def getAlugado(self):
        return self.alugado

    def json(self):
        return str(f'marca: {self.marca}\n'
              f'modelo: {self.modelo}\n'
              f'ano_fab: {self.ano_fab}\n'
              f'preco: {self.preco}\n'
              f'estado_novo: {self.estado_novo}\n'
              f'alugado: {self.alugado}')
