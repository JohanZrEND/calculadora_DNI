from calculadora_dni import calculadora_dni

def main():
    numero_dni = int(input("Introduce numero de dni: "))
    letra = calculadora_dni(numero_dni)
    print(f"DNI Calculado: {numero_dni}-{letra}")

main()