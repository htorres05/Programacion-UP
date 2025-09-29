# Ingreso contadores y acumuladores
cant_total_huesped = 0
habitacion_max = 0
ciudad_max = ""

# Armo el bucle para pedir las 10 sucursales
for suc in range(1,3):
    print("Ingrese los datos del Hotel",suc)
    
    # Pido datos requeridos
    ciudad = input("Ingrese el nombre de la ciudad: ")
    cap_huesped_suc = int(input("Ingrese la capacidad total en huéspedes: "))
    cant_habitaciones = int(input("Ingrese la cantidad de habitaciones: "))
    huesped_mes = int(input("Ingrese la cantidad de huéspedes en el mes: "))
    
    # Voy acumulando la capacidad total del hotel
    cant_total_huesped += cap_huesped_suc
    
    # Calculo el porcentaje de ocupacion teniendo en cuenta
    # cantidad de habitaciones en el mes
    cant_habit_mes = cant_habitaciones * 30
    porc_ocup = (huesped_mes / cant_habit_mes) * 100
    # Lo muestro en pantalla
    print("El porcentaje de ocupacion del hotel ",ciudad,"es de: ",porc_ocup,"%")
    
    # Verifico la ciudad con mas habitaciones
    if cant_habitaciones > habitacion_max:
        habitacion_max = cant_habitaciones
        ciudad_max = ciudad
print("La cantidad total de huesped de la cadena de hotel es: ",cant_total_huesped)
print("El nombre de la ciudad con mayor cantidad de habitaciones es: ", ciudad_max)