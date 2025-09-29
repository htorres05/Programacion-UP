# Inicio contadores y acumuladores
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

# Inicio bucle para pedir las 10 sucursales
for suc in range(1, 11):
    print("Ingrese los datos del hotel",suc)
    
    # Pido datos requeridos y verifico el ingreso correcto
    ciudad = input("Ingrese el nombre de la ciudad: ")
    while ciudad == "":
        print("Debe ingresar el nombre de una ciudad")
        ciudad = input("Ingrese el nombre de la ciudad: ")

    capacidad_huesped = int(input("Ingrese la capacidad total de huespedes: "))
    while capacidad_huesped <= 0:
        print("Debe ingresar el dato correcto")
        capacidad_huesped = int(input("Ingrese la capacidad total de huespedes: "))

    cant_habitaciones = int(input("Ingrese la cantidad de habitaciones: "))
    while cant_habitaciones <= 0:
        print("Debe ingresar el dato correcto")
        cant_habitaciones = int(input("Ingrese la cantidad de habitaciones: "))

    huesped_mensual = int(input("Ingrese la cantidad de huespedes en el mes: "))
    while huesped_mensual < 0:
        print("Ingrese cantidad correcta")
        huesped_mensual = int(input("Ingrese la cantidad de huespedes en el mes: "))
    
    # Acumulo la capacidad total del hotel
    cant_total_huesped += capacidad_huesped
    
    
    # Entiendo que pide el % de ocupacion mensual ya que pide ingresar como dato la cantidad de huespedes en un mes (tomo 30 dias)
    # por eso * 30 la capacidad de huespedes de cada hotel
    capacidad_huesped *= 30

    # Calculo el porcentaje de ocupación con 2 decimales
    # Busque en internet el flag round para redondear a 2 decimales el porcentaje (queda mas lindo)
    porc_ocup = round((huesped_mensual / capacidad_huesped) * 100,2)

    
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
    
    # Verifico y guardo la ciudad con más habitaciones
    if cant_habitaciones > habitacion_max:
        habitacion_max = cant_habitaciones
        ciudad_max = ciudad

# Muestro los resultados finales pedidos
print("La cantidad total de huéspedes de la cadena de hoteles es: ",cant_total_huesped)
print("El nombre de la ciudad con mayor cantidad de habitaciones es: ",ciudad_max)
print("Porcentaje de ocupación por Hotel es: ")
print(ciudad_suc1,": ",porc_ocup_suc1,"%")
print(ciudad_suc2,": ",porc_ocup_suc2,"%")
print(ciudad_suc3,": ",porc_ocup_suc3,"%")
print(ciudad_suc4,": ",porc_ocup_suc4,"%")
print(ciudad_suc5,": ",porc_ocup_suc5,"%")
print(ciudad_suc6,": ",porc_ocup_suc6,"%")
print(ciudad_suc7,": ",porc_ocup_suc7,"%")
print(ciudad_suc8,": ",porc_ocup_suc8,"%")
print(ciudad_suc9,": ",porc_ocup_suc9,"%")
print(ciudad_suc10,": ",porc_ocup_suc10,"%")