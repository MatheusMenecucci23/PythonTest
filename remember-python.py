def funtion():
    num = int(input("Digite o valor do número desejado: "))
    i = 1
    fatora = 1
    while +i <= num:
        fatora = fatora*i
        i = i + 1
    print(num, fatora)

funtion()

op = input("Digite a operação que você deseja realizar: ")
n1 = float(input("Digite o número: "))
n2 = float(input("Digite outro número: "))
if op == "*":
    print(n1*n2, "multiplicação")
elif op == "-":
    print(n1*n2, "sub")
elif op == "/":
    print(n1*n2, "div")
elif op == "+":
    print(n1*n2, "adição")
else:
    print("operação não cadastrada")




