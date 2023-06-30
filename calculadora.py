print("Calculadora de cuentas")
cuenta= float(input("total de la cuenta: $ "))
propina=float(input("porcentaje de propina: 10, 12, 15? "))
division=int(input("para cuantas personas se va a dividir la cuenta? "))

p = cuenta*(propina/100)
c= cuenta+ p
d= c/division

print(f"lo que debe pagar cada uno es: $ {d:.2f}")

