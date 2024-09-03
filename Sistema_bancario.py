## Depósito/Saque/Extrato
## Saque limitado a 3x de R$500 diários 
## Extrato deve listar todas as operações efetuadas + saldo no formato R$ xxxx.xx

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
=> """

saldo = 0
limite = 500
extrato = ""
deposito = 0
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)
    if opcao == "d":
        print("Depósito")
        valor = float(input("Informe o valor a depositar: R$"))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print("Depósito realizado com sucesso!")
        else:
            print("Valor inválido!")

    elif opcao == "s":
        print("Saque")
        valor = float(input("Informe o valor a sacar: R$"))

        if ((valor > 0) and (valor <= limite)) and (numero_saques < LIMITE_SAQUES):
            saldo -= valor
            numero_saques += 1
            extrato += f"Saque: R$ {valor:.2f}\n"
            print("Saque realizado com sucesso!")
        elif (numero_saques == LIMITE_SAQUES):
            print("Limite de saques atingido!")
        else:
            print("Valor inválido, seu limite é R$500!")
    
    elif opcao == "e":
        print("Extrato")
        print(extrato)
        print("Seu saldo é de: R$", saldo)

    elif opcao == "q":
        break

    else:
        print("Opção inválida. Tente novamente.")