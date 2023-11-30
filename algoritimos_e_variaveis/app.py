nome = str(input('Qual o seu nome?' ))
idade = int(input('Qual a sua idade (somente números inteiros)? '))

def qual_escolha():
    while True:
        escolha = input("Você tem a FIDELIDADE? 'SIM' ou 'NÃO': ").upper()
        if escolha in ['SIM', 'NÃO']:
            return escolha == 'SIM'
        else:
            print("Escolha inválida. Por favor, digite 'SIM' ou 'NÃO'.")

cliente_fidelidade = qual_escolha()
preco_str = input('Qual o preço do Item?')
preco_str = preco_str.replace(',', '.')
preco = float(preco_str)
idade_str = str(idade)
preco_str = str(preco)
status_fidelidade = 'ATIVO' if cliente_fidelidade else 'INATIVO'

print('Bem-vindo(a) ' + nome + '. Vi que sua idade é de ' + idade_str + ', certo?! Sendo assim, o preço realmente vai sair a ' + preco_str + '! E aproveitando, gostaria de informar que sua fidelidade está ' + status_fidelidade + '. Espero que tenha gostado de sua consulta. Tenha um ótimo dia!')