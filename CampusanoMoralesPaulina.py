import csv
import json

lista_alumnos=[]
alumnos={}
def carga_masiva():
    with open ("ListaCurso5B.csv", "r") as archivocsv:
        lecturacsv= csv.DictReader(archivocsv)
        for alumnos in lecturacsv:
            if " " in alumnos:
                print("hay valor vacio")
                return None
            else:
                print(alumnos["promedio"])
                promedio=float(alumnos["Nota 1"])+ float(alumnos["Nota 2"])/2
                lista_alumnos.append({
                    "Rut": alumnos["Rut"],
                    "Nombre": alumnos["Nombre"],
                    "Nota 1":alumnos["Nota 1"],
                    "Nota 2": alumnos["Nota 2"],
                    "Promedio": alumnos["promedio"],

                })
#Aqui debe validar el registro                
#while True:
#        try:
#            for alumnos in lista_alumnos:
#                rut = input(int(num))
#            break
#        except ValueError:

def registrar_estudiante():
    rut=input("Ingrese rut del estudiante")
    nombre=input("ingrese nombre del estudiante")
    nota_1=input("ingrese la nota 1 del estudiante")
    nota_2=input("ingrese la nota 2 del estudiante")
    
    lista_alumnos.append({
        "Rut": rut,
        "Nombre": nombre,
        "Nota 1": nota_1,
        "Nota 2": nota_2,
    })
print("El ingreso se ha realizado correctamente, volverá al menú principal")
def modificar_nota():
    modificar= input("ingrese el rut del estudiante que desea modificar")
    for alumnos in lista_alumnos:
        if alumnos["Rut"]== modificar:
            alumnos["Nota 1"]= input("ingrese la nueva nota 1")
            alumnos["Nota 2"]= input("ingrese la nueva nota 2")
print("La modificación se ha realizado correctamente, volverá al menú principal")

def eliminar_estudiante():
    eliminar= input("ingrese el rut del estudiante que desea modificar")
    for alumnos in lista_alumnos:    
        if alumnos["Rut"]== eliminar:
            opcion =input(print(f"¿Esta seguro que desea eliminar a {eliminar}? 1.Si / 2.No"))
            if opcion == 1:
                    lista_alumnos.remove(alumnos)
print("La eliminación se ha realizado correctamente")

def promedio_notas():
    with open("ListaCurso5B.json","w") as promedio_notas:
        for alumnos in lista_alumnos:
            promedio= {"Nombre":alumnos["Nombre"], "promedio": alumnos["promedio"]}
            json.dump(promedio_notas)
print("El proceso de ha terminado, volverá al menú principal")

def acta_cierre():
    with open("Acta_cierre_5B.csv","w") as archivocsv2:
        escribircsv = csv.DictWriter(archivocsv2)
        for alumnos in escribircsv:
            if " " in lista_alumnos:
                print("hay valor vacio")
                return None
            else: 
                lista_alumnos.append({
                    "Rut": alumnos["Rut"],
                    "Nombre": alumnos["Nombre"],
                    "Nota 1":alumnos["Nota 1"],
                    "Nota 2": alumnos["Nota 2"],
                    "Promedio": alumnos["promedio"],
                    "Estado": alumnos["Estado"]

                })
print("El proceso de ha terminado, volverá al menú principal")

def menu():
    print("\n------ Menú ------")
    print("1. Procesar lista de estudiantes.")
    print("2. Registrar estudiante.")
    print("3. Modificar nota.")
    print("4. Eliminar estudiante.")
    print("5. Generar promedio de notas.")
    print("6. Generar acta de cierre de curso.")
    print("7. Salir..")

def main():
    while True:
        menu()
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            carga_masiva()
        elif opcion == '2':
            registrar_estudiante()
        elif opcion == '3':
            modificar_nota()
        elif opcion == '4':
            eliminar_estudiante()
        elif opcion == '5':
            promedio_notas()
        elif opcion == '6':
            acta_cierre()    
        elif opcion == '7':
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()