estudiantes = []

num_estudiantes = int(input("¿Cuántos estudiantes desea registrar? "))

for i in range(num_estudiantes):
    print(f"\n ** Registro del estudiante {i+1} **")
    nombre = input("Nombre del estudiante: ")
    ciudad = input("Ciudad (Quito, Esmeraldas, Ibarra): ")

    notas = []
    print("Ingrese 3 notas académicas:")
    for j in range(3):
        nota = float(input(f"  Nota {j+1}: "))
        notas.append(nota)

    temperaturas = []
    print("Ingrese temperaturas de 7 días en", ciudad)
    for d in range(7):
        temp = float(input(f"  Día {d+1}: "))
        temperaturas.append(temp)

    promedio = round(sum(notas) / 3, 2)
    temp_min = min(temperaturas)
    dia_min = temperaturas.index(temp_min) + 1
    estado = "Aprobado" if promedio >= 7 else "Reprobado"
    nota_min = min(notas)

    estudiante = {
        "nombre": nombre,
        "ciudad": ciudad,
        "promedio": promedio,
        "temp_min": temp_min,
        "dia_min": dia_min,
        "estado": estado,
        "nota_min": nota_min
    }

    estudiantes.append(estudiante)

print("\n*** INFORME FINAL ***")
for est in estudiantes:
    print(f"\nEstudiante: {est['nombre']}")
    print(f"Ciudad: {est['ciudad']}")
    print(f"Promedio de notas: {est['promedio']}")
    print(f"Día más frío: Día {est['dia_min']} con {est['temp_min']} °C")
    print(f"Estado: {est['estado']}")


print("\n--- ANÁLISIS DE CORRELACIÓN ---")
ciudad_mas_fria = min(estudiantes, key=lambda e: e["temp_min"])["ciudad"]
nota_mas_baja = min(estudiantes, key=lambda e: e["nota_min"])
print(f"La ciudad más fría fue: {ciudad_mas_fria}")
print(f"La nota más baja fue de {nota_mas_baja['nombre']} ({nota_mas_baja['nota_min']}) en {nota_mas_baja['ciudad']}")
if ciudad_mas_fria == nota_mas_baja["ciudad"]:
    print("Existe una posible relación entre clima frío y bajo rendimiento.")
else:
    print("No se observa una relación directa entre clima frío y bajo rendimiento.")