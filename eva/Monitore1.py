num_usuarios = int(input("Cuántos usuarios desea registrar: "))

lista_usario = []
lista_sede = []
lista_notas = []

for i in range(num_usuarios):
    usuario  = input(f"Seleccione el estudiante {i+1} a registrar: ")
    sede = input(f"Seleccione la sede para el estudiante {i+1}: ")
    notas = input(f"Ingrese las notas del estudiante {i+1}: ")
    
    lista_usario.append(usuario)
    lista_sede.append(sede)
    lista_notas.append(notas)
    
    
promedio = lista_notas / 3

print(promedio)

