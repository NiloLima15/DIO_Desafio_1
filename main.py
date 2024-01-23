menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
"""
print("\n=============================================")

saldo = 0
limite = 500
extrato = ""
numero_saque = 0
LIMITE_SAQUE = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do deposito:"))

        if valor > 0:
            saldo += valor
            extrato += f"Desposito R${valor:.2f}\n"
            print(f"\nDeposito no valor de     R${valor:.2f}\n"
                  f"                        Com sucesso! .")
            print("\n=============================================")
        else:
            print("Operação invalida!, Tente novamente outro valor.")
            print("\n=============================================")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque:"))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        exdedeu_saque = numero_saque >= LIMITE_SAQUE

        if excedeu_saldo:
            print("Operação invalida! Não tem saldo suficiente.")
            print("\n=============================================")

        elif excedeu_limite:
            print("Operação invalida! Exedeu o valor maximo de limites.")
            print("\n=============================================")

        elif exdedeu_saque:
            print("Operação invalida! Exedeu o N° maximo de saques.")
            print("\n=============================================")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque R${valor:.2f}\n"
            numero_saque += 1

        else:
            print("Operação Invalida!, Valor informado incorreto.")

    elif opcao == "e":
        print("\n================== EXTRATO ==================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("\n=============================================")

    elif opcao == "q":
        print("\n================= SAINDO... ==================")
        break

    else:
        print("Operação Invalida!, Favor selecionar novamente outra opção.")
        print("\n=============================================")

