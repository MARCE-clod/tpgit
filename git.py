import json


def crear_archivo_empleados():
    empleados = [
        {"id": 2334, "nombre": "Juan Pérez", "salario": 250.000},
        {"id": 2323, "nombre": "Ana Gómez", "salario": 300.000},
        {"id": 3232, "nombre": "Luis Sánchez", "salario": 270.000},
        {"id": 4454, "nombre": "Marta Fernández", "salario": 320.000},
        {"id": 5467, "nombre": "Carlos López", "salario": 290.000}
    ]
    
    
    with open("empleados.txt", "w") as file:
        for empleado in empleados:
            file.write(json.dumps(empleado) + "\n")
    
    print("Archivo 'empleados.txt' creado con información de empleados.")


def leer_archivo_empleados():
    empleados = []
    try:
        with open("empleados.txt", "r") as file:
            for line in file:
                empleado = json.loads(line.strip())  
                empleados.append(empleado)
    except FileNotFoundError:
        print("El archivo 'empleados.txt' no se encuentra.")
    return empleados


def modificar_salario(empleados):
    id_empleado = int(input("Introduce el ID del empleado cuyo salario deseas modificar: "))
    empleado_encontrado = False
    
   
    for empleado in empleados:
        if empleado["id"] == id_empleado:
            nuevo_salario = float(input(f"Introduce el nuevo salario para {empleado['nombre']}: "))
            empleado["salario"] = nuevo_salario
            empleado_encontrado = True
            print(f"Salario de {empleado['nombre']} actualizado a {nuevo_salario}.")
            break
    
    if not empleado_encontrado:
        print("Error: No se encontró un empleado con ese ID.")
    
    return empleados


def guardar_empleados(empleados):
    with open("empleados.txt", "w") as file:
        for empleado in empleados:
            file.write(json.dumps(empleado) + "\n")
    print("Datos de empleados actualizados en 'empleados.txt'.")


def main():
    crear_archivo_empleados()
    empleados = leer_archivo_empleados()

    
    print("\nLista de empleados antes de la modificación:")
    for empleado in empleados:
        print(f"ID: {empleado['id']}, Nombre: {empleado['nombre']}, Salario: {empleado['salario']}")

    
    empleados = modificar_salario(empleados)

    
    guardar_empleados(empleados)

    
    print("\nLista de empleados después de la modificación:")
    for empleado in empleados:
        print(f"ID: {empleado['id']}, Nombre: {empleado['nombre']}, Salario: {empleado['salario']}")

if __name__ == "__main__":
    main()
