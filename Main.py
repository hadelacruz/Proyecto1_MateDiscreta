def leer_conjuntos(archivo):
    conjuntos = {}
    with open(archivo, 'r') as f:
        for linea in f:
            nombre, elementos = linea.strip().split(":={")
            elementos = elementos.rstrip('}')
            if elementos:
                if nombre.strip() == 'E':
                    elementos = [tuple(e.strip('() ').split(',')) for e in elementos.split('),(')]
                else:
                    elementos = [e.strip() for e in elementos.split(',')]
                conjuntos[nombre.strip()] = set(elementos)
            else:
                conjuntos[nombre.strip()] = set()
    return conjuntos

def union(A, C):
    return A | C

def interseccion(A, C):
    return A & C

def diferencia(A, B):
    return A - B

def complemento(A, U):
    return U - A

#DUDA
def producto_cartesiano(A, B):
    resultado = {(a, b) for a in A for b in B}
    if not resultado:
        return "{}"  # O puedes devolver un mensaje como "Conjunto vacío"
    return resultado

def es_funcion(E):
    elementos_vistos = set()
    for x, y in E:
        if x in elementos_vistos:
            return False, f"El elemento {x} tiene más de una imagen."
        elementos_vistos.add(x)
    return True, "El conjunto es una función."

def seleccionar_operacion():
    print("\n------------OPERACIONES DISPONIBLES------------")
    print("1. A ∪ C")
    print("2. A ∩ C")
    print("3. A - B")
    print("4. Complemento de A")
    print("5. (A ∪ B) ∩ C")
    print("6. Función (fun(E))")
    print("7. Complemento de D")
    print("8. D - U")
    print("9. Producto cartesiano y función (fun(A × B))")
    print("0. Salir")

    seleccion = int(input("Selecciona una operación (0-9): "))
    return seleccion

def realizar_operacion(conjuntos, seleccion):
    U = conjuntos['U']
    A = conjuntos['A']
    B = conjuntos['B']
    C = conjuntos['C']
    D = conjuntos['D']
    E = conjuntos['E']

    if seleccion == 1:
        resultado = union(A, C)
    elif seleccion == 2:
        resultado = interseccion(A, C)
    elif seleccion == 3:
        resultado = diferencia(A, B)
    elif seleccion == 4:
        resultado = complemento(A, U)
    elif seleccion == 5:
        resultado = interseccion(union(A, B), C)
    elif seleccion == 6:
        funcion, mensaje = es_funcion(E)
        print(f"El conjunto E {'es' if funcion else 'no es'} una función. {mensaje}")
        resultado = None
    elif seleccion == 7:
        resultado = complemento(D, U)
    elif seleccion == 8:
        resultado = diferencia(D, U)
        if resultado == set():
            print("El resultado es un conjunto vacío.")
    elif seleccion == 9:
        resultado = producto_cartesiano(A, B)
        funcion = es_funcion(resultado)
        print(f"El conjunto A × B {'es' if funcion else 'no es'} una función.")
    else:
        resultado = None

    if resultado is not None:
        print("\nRESULTADO:", resultado)

def main():
    archivo = 'datos.txt'
    conjuntos = leer_conjuntos(archivo)
    
    while True:
        seleccion = seleccionar_operacion()
        if seleccion == 0:
            print("Saliendo del programa...")
            break
        realizar_operacion(conjuntos, seleccion)

if __name__ == "__main__":
    main()
