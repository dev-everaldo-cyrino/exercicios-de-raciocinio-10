class bomba:
    def __init__(self,tipoCombustivel='',valorLitro=0,quantidadeCombustivel=0):
        self.tpcombustivel = tipoCombustivel
        self.valorl = valorLitro
        self.qtcombustivel = quantidadeCombustivel
    
    def abastecerPorValor(self):
        valor = float(input('digite o valor pago: '))
        litros = 0
        while valor > self.valorl:
            valor -= self.valorl
            litros += 0.25
            self.qtcombustivel -= 0.25
        print('combustivel na bomba: {} L'.format(self.qtcombustivel))
        print('foram abastecidos: {} L'.format(litros))
        print('...........................')
        
    def abastecerPorLitro(self):
        pass
    def alterarValor(self):
        pass
    def alterarCombustivel(self):
        pass
    def alterarQuantidadeCombustivel(self):
        pass