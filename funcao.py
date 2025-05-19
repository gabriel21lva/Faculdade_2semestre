def exibir_mensagem():
    print('ola,mundo!')

def exibir_mensagem2(nome):
    print(f'Seja bem vindo, {nome}!')

def exibir_mensagem3(nome= "Anonimo"):
    print(f'Seja bem vindo, {nome}!')


exibir_mensagem()
exibir_mensagem2(nome= 'Guilherme')
exibir_mensagem3()
exibir_mensagem3(nome= 'Chappie')

def calcular_total(numeros):
    return sum(numeros)

def retorna_antecessor_e_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1

    return antecessor, sucessor

print(calcular_total([10,20,34]))
print(retorna_antecessor_e_sucessor(10))

def salvar_carro(marca,modelo,ano,placa):

    print(f'Carro inserido com sucesso!{marca}/{modelo}/{ano}/{placa}')

salvar_carro('Fiat', 'Palio', 1999, 'ABC-1234')
salvar_carro(marca='Fiat',modelo='Palio',ano=1999,placa='ABC-1234') 

salvar_carro(**{"marca": "Fiat", "modelo":"Palio", "ano":1999, "placa": "ABC-1234"})

# --> *args valores em tupla
# --> **kwargs valores em dicionario


# Palavra-chave global
salario = 2000

def salario_bonus(bonus):
    global salario
    salario += bonus
    return salario

salario_bonus(500)
print(salario_bonus)