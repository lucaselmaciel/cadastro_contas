class Conta:
    numero_conta = []
    banc_cont = {}
    def __init__(self, correntista):
        self.correntista = correntista
        #self.numero_conta
        self.gerador_numero_conta()
        self.banco_de_contas()

        
    def gerador_numero_conta(self):
        
        return self.numero_conta.append(1)
    
    
    def banco_de_contas(self):
        
        self.banc_cont.setdefault(sum(self.numero_conta[0:]),{'Nome': None, 'Saldo': 0})
        self.banc_cont[sum(self.numero_conta[0:])] = {'Nome': self.correntista, 'Saldo': 0}
        #return print(f'Seu número de conta é: {sum(self.numero_conta[0:])}')
    
    
    def numeroDaConta(self):    
        return print(f'Seu número de conta é: {sum(self.numero_conta[0:])}', end='\n')
    
    def deposito(self):
        numdaconta = int(input('Numero da conta: '))
        valor = int(input('O valor do depósito: '))
        self.banc_cont[numdaconta]['Saldo'] += valor
        print('Depósito realizado')
        
    def saque(self):
        print('Cédulas disponíveis - R$20 e R$50')
        numdaconta = int(input('Numero da conta: ')) 
        saq = int(input('Insira o valor a ser sacado: '))
        self.banc_cont[numdaconta]['Saldo'] -= saq

    def consultar_dados(self):
        num_conta = input('Numero da conta: ')
        if num_conta=='todas':
            return print(self.banc_cont)
        num_conta = int(num_conta)
        return print(self.banc_cont[num_conta])



if __name__=='__main__':
    while True:
        print()
        print('Escolha uma função: ')
        print('1 - Criar conta')
        print('2 - Realizar depósito')
        print('3 - Sacar dinheiro')
        print('4 - Informações de Conta Corrente')
        esc = int(input()) 
       

        if esc == 1:
            nome = input('Insira seu nome: ')
            conta = Conta(nome)
            conta.numeroDaConta()         
        elif esc==2:
            conta.deposito()
        elif esc == 3:
            conta.saque()
        elif esc==4:
            conta.consultar_dados()
        esc = 0
        