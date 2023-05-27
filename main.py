valor = int(input("Digite um valor: "))

if valor % 3 == 0 and valor % 5 == 0:
    print("FizzBuzz")
elif valor % 3 == 0:
    print("Fizz")
elif valor % 5 == 0:
    print("Buzz")
else:
    print(valor)
