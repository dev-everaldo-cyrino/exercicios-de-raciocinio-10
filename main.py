class bomba:
    def __init__(self,tipoCombustivel='',valorLitro=0,quantidadeCombustivel=0):
        self.tpcombustivel = tipoCombustivel
        self.valorl = valorLitro
        self.qtcombustivel = quantidadeCombustivel
    
    def valor(self):
        self.tpcombustivel = 'gasolina'
        self.valorl = 5
        self.qtcombustivel = 1000
    
    def abastecerPorValor(self):
        valor = float(input('digite o valor pago: '))
        litros = valor / self.valorl
        self.qtcombustivel -= litros
        print('combustivel na bomba: {} L de {}'.format(self.qtcombustivel, self.tpcombustivel))
        print('foram abastecidos: {} L do combustivel: {}'.format(litros, self.tpcombustivel))
        print('valor: {}'.format(valor))
        print('...........................')
        
    def abastecerPorLitro(self):
        valor = float(input('digite a qauntidade de litros: '))
        litros = valor * self.valorl
        self.qtcombustivel -= valor
        print('combustivel na bomba: {} L de {}'.format(self.qtcombustivel, self.tpcombustivel))
        print('foram abastecidos: {} L do combustivel: {}'.format(valor, self.tpcombustivel))
        print('valor: {}'.format(litros))
        print('...........................')
        
    def alterarValor(self):
        print('preço atual: {}'.format(self.valorl))
        valor = float(input('digite o novo preço: '))
        self.valorl = valor
        print('valor atualizado com sucesso!!')
        print('...........................')
        
    def alterarCombustivel(self):
        print('combustivel atual: {}'.format(self.tpcombustivel))
        tipo = input('qual o tipo do combustivel: ')
        self.tpcombustivel = tipo
        print('tipo do combustivel atualizado com sucesso!!')
        print('...........................')
        
    def alterarQuantidadeCombustivel(self):
        print('quantidade de combustivel atual: {}'.format(self.qtcombustivel))
        quant = input('qual o tipo do combustivel: ')
        self.qtcombustivel = quant
        print('quantidade de combustivel atualizado com sucesso!!')
        print('...........................')
        
        
bomba.valor(bomba)
while True:
    print('......................................')
    print('''
          ------MENU------
          1- abastecer por dinheiro
          2- abastecer por litros
          3- alterar o preço do combustivel
          4- alterar o combustivel
          5- alterar a quantidade de combustivel
          6- sair''')
    op = int(input('opção:  '))
    print('......................................')
    if op ==1:
        bomba.abastecerPorValor(bomba)
    if op ==2:
        bomba.abastecerPorLitro(bomba)
    if op ==3:
        bomba.alterarValor(bomba)
    if op ==4:
        bomba.alterarCombustivel(bomba)
    if op ==5:
        bomba.alterarQuantidadeCombustivel(bomba)
    if op ==6:
        break