agenda = {}

def validar_telefono(numero):
    return numero.isdigit() and len(numero) <= 11


def insertar_contacto():
    nombre = input("Nombre: ").strip()
    telefono = input("Teléfono: ").strip()

    if not validar_telefono(telefono):
        print("❌ Número inválido (solo números y máximo 11 dígitos)")
        return

    agenda[nombre] = telefono
    print("✅ Contacto agregado")


def buscar_contacto():
    nombre = input("Nombre a buscar: ").strip()
    if nombre in agenda:
        print(f"📞 {nombre}: {agenda[nombre]}")
    else:
        print("❌ Contacto no encontrado")


def actualizar_contacto():
    nombre = input("Nombre a actualizar: ").strip()

    if nombre in agenda:
        telefono = input("Nuevo teléfono: ").strip()

        if not validar_telefono(telefono):
            print("❌ Número inválido")
            return

        agenda[nombre] = telefono
        print("✅ Contacto actualizado")
    else:
        print("❌ Contacto no existe")


def eliminar_contacto():
    nombre = input("Nombre a eliminar: ").strip()

    if nombre in agenda:
        del agenda[nombre]
        print("🗑️ Contacto eliminado")
    else:
        print("❌ Contacto no existe")


def mostrar_menu():
    print("\n--- AGENDA ---")
    print("1. Insertar contacto")
    print("2. Buscar contacto")
    print("3. Actualizar contacto")
    print("4. Eliminar contacto")
    print("5. Salir")


def ejecutar():
    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ").strip()

        if opcion == "1":
            insertar_contacto()
        elif opcion == "2":
            buscar_contacto()
        elif opcion == "3":
            actualizar_contacto()
        elif opcion == "4":
            eliminar_contacto()
        elif opcion == "5":
            print("👋 Saliendo...")
            break
        else:
            print("❌ Opción inválida")


# Ejecutar programa
ejecutar()
print("melo")