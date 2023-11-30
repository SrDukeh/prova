nome = str(input('Qual o seu nome?'))
idade = int(input('Qual a sua idade (somente numeros inteiros)'))
preco = float(input('Qual o preço do Item?'))

def qual_escolha():
    while True:
        escolha = input("Escolha entre 'True' ou 'False': ").capitalize()
        if escolha in ['True', 'False']:
            return escolha == 'True'
        else:
            print("Escolha inválida. Por favor, digite 'True' ou 'False'.")

cliente_fidelidade = qual_escolha()

idade_str = str(idade)
preco_str = input('Qual o preço do Item?')
preco = float(preco_str.replace(',', '.'))
preco_str = str(preco)
cliente_fidelidade_str = str(cliente_fidelidade)


print ('Bem vindo(a) '+nome+'. Vi que sua idade é de '+idade_str+', certo?! Sendo assim, o preço realmente vai sair a '+preco_str+'! E aproveitando, gostaria de informar que sua fidadelidade esta atuando como: '+cliente_fidelidade_str+'. Espero que tenha gostado de sua consulta. Tenha um otimo dia!')