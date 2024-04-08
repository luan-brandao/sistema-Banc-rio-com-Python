menu = "\n opções de conta\n\n 0-Sair\n 1-deposito\n 2-saque\n 3-extrato\n\n ***digite o numero da sua opção*** \n\n =>"
conta = 0.0
limite = 500
extrato = [[], []]
numero_de_saques = 0
LIMITE_DE_SAQUE = 3

while True:
    opcao = input((menu))

    if opcao == "1":
        print("Opção de deposito selecionada ")
        deposito = float(input("Quanto deseja depositar?\n"))
        conta += deposito
        print("Operação realizada com sucesso!")
        extrato[1].append(deposito)
        
    elif opcao == "2":
        if conta == 0:
            print("Saldo insuficiente para realizar saques")
        else:
            while numero_de_saques < LIMITE_DE_SAQUE :
                saque = float(input("Quanto deseja sacar?\n"))
                if (saque <= limite) and saque <= 500 and (conta > saque):
                    numero_de_saques += 1
                    conta -= saque
                    extrato[0].append(saque)
                    print(f"Saque de {saque:.2f}R$ realizado com sucesso.")
                    break
                elif (conta < saque):
                    print(f"Saldo insuficiente, seu saldo total disponivel para saque é  {conta:2}R$")
                else:
                    print("O valor tem q ser menor q 500.00$")   
            else:
                print("Valor maximo de saques excedido! Não pode mais sacar")    
    elif opcao == "3":
        print("\n***Extrato bancario***\n")
        print("Depositos ")
        for i, item in enumerate((extrato[1])):
            print(f"{i+1}- {item:.2f}R$")
        print("\nSaques")
        for i, item in enumerate((extrato[0])):
            print(f"{i+1}- {item:.2f}R$")
        print(f"Saldo bancario: {conta}R$")
    elif opcao == "0":
        print("Saindo")
        break
    else:
        print("resposta invalida, nao foi possivel realizar a opeação. tente novamente! ") 
