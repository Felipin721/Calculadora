#calculadora de idade | Felipe de Bitencourt Rotta

print("Vamos calcular sua idade!")
ano_nascimento = int(input("Digite seu ano de nascimento: "))
ano_atual = int(input("Digite o ano atual: "))

idade = ano_atual - ano_nascimento

print(f"Sua idade é aproximadamente: {idade} anos.")
