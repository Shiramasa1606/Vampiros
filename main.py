def poblar():
    lista = []
    while True:
        linea = input()
        if linea == "FIN":
            return lista
        
        if linea.isnumeric():
            num = int(linea)
            if num not in lista:
                lista.append(num)

def mostrar(lista, cadena):
    print(cadena, lista)
    print(f"TOTAL NÚMEROS EN LISTA = {len(lista)}\n")

def esPar(num):
    cadena = str(num)
    if (len(cadena) % 2 == 0):
        print(f"PROPIEDAD 1 : LA CUMPLE, YA QUE LARGO({num}) = {len(cadena)}, ES PAR.")
        return True
    else:
        print(f"PROPIEDAD 1 : NO LA CUMPLE, YA QUE LARGO({num}) = {len(cadena)}, ES IMPAR. FIN-PROCESO")
        return False

def buscarColmillos(num):
    colmillos = []
    
    cadenaNum = str(num)
    largo = len(cadenaNum)
    mitad = largo // 2
    
    base = 10 ** (mitad - 1)
    tope = 10 ** mitad
    
    for i in range(base, tope):
        
        if num % i == 0:
            complemento = num // i
            if (i > complemento):
                return colmillos
            else:
                if (len(str(i)) == mitad and len(str(complemento)) == mitad):
                    col = (i, complemento)
                    colmillos.append(col)
            
    return colmillos

def depurarColmillos(lista, num):
    listaDigNum = list(str(num))
    listaDigNum.sort()
    depurados = []
    
    for tupla in lista:
        num1, num2 = tupla
        listaColmillo = list(str(num1)) + list(str(num2))
        listaColmillo.sort()

        
        if listaDigNum == listaColmillo:
            depurados.append(tupla)
    
    return depurados
        

def quitarTerminadosEnCero(lista):
    verdaderos = []
    for tupla in lista:
        num1, num2 = tupla
        num1 = str(num1)
        num2 = str(num2)
        if not (num1[-1] == "0" and num2[-1] == "0"):
            verdaderos.append(tupla)
    
    return verdaderos

def analizarVampiros(lista):
    vampiros = []
    print("-----------    INICIO ANÁLISIS VAMPIROS    -----------\n")
    
    for num in lista:
        print(f"PROCESAMIENTO NÚMERO {num}")
        
        if esPar(num):
            colmillos = buscarColmillos(num)
            
            if len(colmillos) == 0:
                print("PROPIEDAD 2 : NO LA CUMPLE, YA QUE NO EXISTEN COLMILLOS QUE TENGAN LA MITAD DE LOS DÍGITOS DEL Nº ORIGINAL. FIN-PROCESO")
            else:
                print("PROPIEDAD 2 : LA CUMPLE, YA QUE EXISTEN COLMILLOS QUE TIENEN LA MITAD DE LOS DÍGITOS DEL Nº ORIGINAL =", colmillos)
                
                colmillos = depurarColmillos(colmillos, num)
                
                if len(colmillos) == 0:
                    print("PROPIEDAD 3 : NO LA CUMPLE, YA QUE EL Nº NO TIENE LOS MISMOS DÍGITOS QUE LOS COLMILLOS ENCONTRADOS. FIN-PROCESO.")
                else:
                    print("PROPIEDAD 3 : LA CUMPLE. YA QUE EL Nº TIENE LOS MISMOS DÍGITOS QUE LOS SIGUIENTES COLMILLOS =", colmillos)
                    
                    colmillos = quitarTerminadosEnCero(colmillos)
                    
                    if len(colmillos) == 0:
                        print("PROPIEDAD 4 : NO LA CUMPLE. YA QUE LOS COLMILLOS ENCONTRADOS TERMINAN AMBOS EN CERO. FIN-PROCESO.")
                    else:
                        print(f"PROPIEDAD 4 : LA CUMPLE. YA QUE LOS COLMILLOS ENCONTRADOS NO TERMINAN AMBOS EN CERO = {colmillos}.",)
                        print(f"FINALMENTE, COMO EL Nº {num} CUMPLE LAS 4 PROPIEDADES ES VAMPIRO!.")
                        vampiros.append(num)
        print()
    
    print("-----------      FIN ANÁLISIS VAMPIROS     -----------\n")
    return sorted(vampiros)
    
lista = poblar()


if len(lista) == 0:
    print("NO SE INGRESARON NÚMEROS ENTEROS POSITIVOS - FIN DEL PROGRAMA.")
else:
    mostrar(lista, "LISTA NÚMEROS ENTEROS DIFERENTES INGRESADOS =")
    lista.sort(reverse = True)
    mostrar(lista, "LISTA NÚMEROS ENTEROS DIFERENTES ORDENADOS DE MAYOR A MENOR =")
    
    vampiros = analizarVampiros(lista)
    
    if len(vampiros) == 0:
        print("NO SE ENCONTRARON NÚMEROS VAMPIROS.")
    else:
        mostrar(vampiros, "LISTA NÚMEROS VAMPIROS ORDENADOS DE MENOR A MAYOR =")
