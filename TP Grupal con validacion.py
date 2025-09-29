# Ingreso contadores y acumuladores
cant_total_huesped = 0
habitacion_max = 0
ciudad_max = ""
porc_ocup_suc1 = 0
porc_ocup_suc2 = 0
porc_ocup_suc3 = 0
porc_ocup_suc4 = 0
porc_ocup_suc5 = 0
porc_ocup_suc6 = 0
porc_ocup_suc7 = 0
porc_ocup_suc8 = 0
porc_ocup_suc9 = 0
porc_ocup_suc10 = 0
ciudad_suc1 = ""
ciudad_suc2 = ""
ciudad_suc3 = ""
ciudad_suc4 = ""
ciudad_suc5 = ""
ciudad_suc6 = ""
ciudad_suc7 = ""
ciudad_suc8 = ""
ciudad_suc9 = ""
ciudad_suc10 = ""

# Armo el bucle para pedir las 10 sucursales
for suc in range(1, 11):
    print(f"Ingrese los datos de la filial {suc}")
    
    # Pido datos requeridos
    ciudad = input("Ingrese el nombre de la ciudad: ")
    cap_huesped_suc = int(input("Ingrese la capacidad total en huéspedes: "))
    cant_habitaciones = int(input("Ingrese la cantidad de habitaciones: "))
    huesped_mes = int(input("Ingrese la cantidad de huéspedes en el mes: "))
    
    # Acumulo la capacidad total del hotel
    cant_total_huesped += cap_huesped_suc
    
    # Calculo el porcentaje de ocupación con 2 decimales
    # Busque en internet como hacer para redondear a 2 decimales el porcentaje
    if cap_huesped_suc > 0:
        porc_ocup = (huesped_mes / cap_huesped_suc) * 100
    else:
        porc_ocup = 0  # Evitar división por cero
    
    # Guardo el porcentaje y la ciudad en las variables correspondientes
    if suc == 1:
        porc_ocup_suc1 = porc_ocup
        ciudad_suc1 = ciudad
    elif suc == 2:
        porc_ocup_suc2 = porc_ocup
        ciudad_suc2 = ciudad
    elif suc == 3:
        porc_ocup_suc3 = porc_ocup
        ciudad_suc3 = ciudad
    elif suc == 4:
        porc_ocup_suc4 = porc_ocup
        ciudad_suc4 = ciudad
    elif suc == 5:
        porc_ocup_suc5 = porc_ocup
        ciudad_suc5 = ciudad
    elif suc == 6:
        porc_ocup_suc6 = porc_ocup
        ciudad_suc6 = ciudad
    elif suc == 7:
        porc_ocup_suc7 = porc_ocup
        ciudad_suc7 = ciudad
    elif suc == 8:
        porc_ocup_suc8 = porc_ocup
        ciudad_suc8 = ciudad
    elif suc == 9:
        porc_ocup_suc9 = porc_ocup
        ciudad_suc9 = ciudad
    elif suc == 10:
        porc_ocup_suc10 = porc_ocup
        ciudad_suc10 = ciudad
    
    # Verifico la ciudad con más habitaciones
    if cant_habitaciones > habitacion_max:
        habitacion_max = cant_habitaciones
        ciudad_max = ciudad

# Muestro los resultados finales
print("La cantidad total de huéspedes de la cadena de hoteles es: ",cant_total_huesped)
print("El nombre de la ciudad con mayor cantidad de habitaciones es: ",ciudad_max)
print("Porcentaje de ocupación por filial:")
print(f"{ciudad_suc1}: {porc_ocup_suc1}%")
print(f"{ciudad_suc2}: {porc_ocup_suc2}%")
print(f"{ciudad_suc3}: {porc_ocup_suc3}%")
print(f"{ciudad_suc4}: {porc_ocup_suc4}%")
print(f"{ciudad_suc5}: {porc_ocup_suc5}%")
print(f"{ciudad_suc6}: {porc_ocup_suc6}%")
print(f"{ciudad_suc7}: {porc_ocup_suc7}%")
print(f"{ciudad_suc8}: {porc_ocup_suc8}%")
print(f"{ciudad_suc9}: {porc_ocup_suc9}%")
print(f"{ciudad_suc10}: {porc_ocup_suc10}%")