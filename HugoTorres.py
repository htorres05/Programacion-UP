#pido ingreso de valor de compra
val_comp = int(input("Ingrese el valor de la compra: "))

#guardo en vuelto 
vuelto = 100 - val_comp

#ahora calculo los billetes a usar
bill50 = vuelto // 50
sobra = vuelto % 50
bill20 = sobra // 20
sobra = sobra % 20
bill10 = sobra // 10
sobra = sobra % 10
bill5 = sobra // 5
bill1 = sobra % 5

#imprimo el resultado
print("El vuelto es: ")
print("Billetes de 50: ",bill50 )
print("Billetes de 20: ",bill20 )
print("Billetes de 10: ",bill10 )
print("Billetes de 5: ",bill5 )
print("Billetes de 1: ",bill1 )