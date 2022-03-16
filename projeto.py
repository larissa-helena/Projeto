import sys
from math import floor
from datetime import date
from datetime import datetime


def jogar():
    hoje = datetime.today()
    datas = '{}/{}/{}'.format(hoje.day, hoje.month, hoje.year)

    print("Olá!")
    data = input("Digite uma data: ")
    data2 = datetime.strptime(data, "%d/%m/%Y")
    print("\n")

    print(data)
    print("Está certo?")
    print("1- Sim  2- Não")
    certo = int(input(""))
    print("\n")

    for rodada in range(1):
        if certo == 1:
            print("Ótimo!")
            continue
        else:
            print("Ok, vamos recomeçar.\n")
            jogar()

    print("Hoje é dia", datas, "\n")

    mes = data2.month

    if mes >= hoje.month:
        result = ((hoje.year - data2.year)-1)

    else:
        result = (hoje.year - data2.year)

    week = 0.142857
    anos = result
    meses = (((12 * hoje.year) + hoje.month - 1)-((12 * data2.year) + data2.month))
    dias = (hoje - data2)
    semanas = floor(dias.days*week)

    print("Você está vivo há:")
    print(anos, "Anos,", meses, "Meses,", semanas, "Semanas e", dias.days, "Dias.\n")

    if mes >= hoje.month:
        next = date(hoje.year, data2.month, data2.day)

    else:
        next = date(hoje.year + 1, data2.month, data2.day)

    nt = next

    if mes >= hoje.month:
        ntt = (((12 * nt.year) + nt.month) - ((12 * hoje.year) + hoje.month))
    else:
        ntt = (((12 * nt.year) + nt.month - 1) - ((12 * hoje.year) + hoje.month))

    nttt = ntt

    if data2.day < hoje.day:
        dia = (data2.day - hoje.day) + 30
    else:
        dia = data2.day - hoje.day

    reais = "R${:,.2f}".format(dias.days)
    centavos = "R${:,.2f}".format((dias.days*100)/100)

    print("Seu próximo aniversário será em:")
    print(nttt, "Meses e", dia, "dias\n")
    print("Se você tivesse economizado R$1,00 desde que nasceu, hoje você teria:")
    print(reais, "ou", dias.days*100, "centavos (que são", centavos, "reais)\n")
    print("Escolha uma porcentagem para o juros")

    porcentagem = input("Digite a porcentagem de 1% a 5%: ")
    porcentagem2 = float(porcentagem)
    porcentagem3 = (porcentagem2 / 100) + 1

    meses = (((12 * hoje.year) + hoje.month - 1) - ((12 * data2.year) + data2.month))
    soma = 30
    contador = meses
    valor = 0

    while contador > 0:
        valor = (valor + soma) * porcentagem3

        contador = contador - 1

    total = "R${:,.2f}".format(valor)

    print("\n")
    print("Com o juros de", porcentagem, "%, hoje você teria", total)
    print("\n")

    print("Gostaria de tentar outra data?")
    print("1- Sim  2- Não")
    tentar = int(input())

    if tentar == 1:
        print("Ok, vamos lá!\n")
        jogar()

    else:
        print("Bye!")
        sys.exit(0)


if __name__ == "__main__":
    jogar()
