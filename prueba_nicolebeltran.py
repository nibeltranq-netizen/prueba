
def leer_opcion():
    try:
        opcion = int(input("ingrese su opcion "))
        if 1 < opcion < 6 :
            print("ingrese una opcion valida")
    except ValueError:
        print("ingrese una opcion valida")

def mostrar_menu():
    print("***MENU PRINCIPAL***")
    print("1.stock marca")
    print("2.busqueda por precio")
    print("3.actualizar precio")
    print("4.salir")

def stock_marca(marca):
    stock_total = 0
    for codigo, datos in productos.items():
        if datos[2].lower() == marca.lower():
            stock_total += marca[codigo][2]
    print(f"el stock disponible es {stock_total}")

def busqueda_precio(precio_min, precio_max):
    resultados = []
    for codigo, datos_precio in stock.items():
        stock = codigo[2]
        
    if precio_min <= precio <= precio_max and stock != 0:
        
        return 
    if len(datos_precio):
        resultados.append = ({"marca"---"modelo"})
        resultados.sorted(resultados)

def actualizar_precio(modelo, productos):

    if not modelo in productos:
        return False
    else:
        return True
    

def validar_positivos(texto):
    return texto > 0 






productos = {'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
    '2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
    'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
    'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
    'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
    '123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
    '342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
    'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050']
    }
        

stock = {'8475HD': [387990,10], '2175HD': [327990,4], 'JjfFHD': [424990,1],
 'fgdxFHD': [664990,21], '123FHD': [290890,32], '342FHD': [444990,7],
 'GF75HD': [749990,2], 'UWU131HD': [349990,1], 'FS1230HD': [249990,0],
 }




continuar = True
while continuar:
    mostrar_menu()
    try:
        opcion = int(input("ingrese su opcion "))
        if 1 < opcion < 6 :
            print("ingrese una opcion valida")
    except ValueError:
        print("ingrese una opcion valida")

    if opcion == 1:
        marca = input("ingrese la marca a buscar ")
        stock_marca(marca)
    elif opcion == 2:
        precio_min = None
        precio_max = None
        while not precio_min and precio_max is None: 
         precio_min = int(input("ingrese el precio minimo "))
         precio_max = int(input("ingrese el precio max "))
         busqueda_precio()
    elif opcion == 3:
        repetir = "s"
        while repetir:
            validar_positivos(modelo, precio,)
            modelo = input("ingrese el modelo a actualizar")
            precio = int(input("ingrese precio a actualizar "))
            actualizar_precio()
            repetir = input("desea actualizar otro precio (s/n)")
            
    elif opcion == 4:
        print("programa finalizado")
    continuar = False