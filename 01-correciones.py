def validar_telefono(telefono):
    return telefono.isdigit() and len(telefono) <= 11


def mostrar_menu():
    print("\n📒 AGENDA DE CONTACTOS")
    print("1. Agregar contacto")
    print("2. Buscar contacto")
    print("3. Actualizar contacto")
    print("4. Eliminar contacto")
    print("5. Ver todos los contactos")
    print("6. Salir")


def agenda():
    contactos = {}

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        # AGREGAR
        if opcion == "1":
            nombre = input("Nombre: ").strip()
            telefono = input("Teléfono: ").strip()

            if not validar_telefono(telefono):
                print("❌ Teléfono inválido (solo números y máximo 11 dígitos)")
                continue

            contactos[nombre] = telefono
            print("✅ Contacto agregado")

        # BUSCAR
        elif opcion == "2":
            nombre = input("Nombre a buscar: ").strip()
            if nombre in contactos:
                print(f"📞 {nombre}: {contactos[nombre]}")
            else:
                print("❌ Contacto no encontrado")

        # ACTUALIZAR
        elif opcion == "3":
            nombre = input("Nombre a actualizar: ").strip()
            if nombre in contactos:
                nuevo_telefono = input("Nuevo teléfono: ").strip()

                if not validar_telefono(nuevo_telefono):
                    print("❌ Teléfono inválido")
                    continue

                contactos[nombre] = nuevo_telefono
                print("🔄 Contacto actualizado")
            else:
                print("❌ Contacto no existe")

        # ELIMINAR
        elif opcion == "4":
            nombre = input("Nombre a eliminar: ").strip()
            if nombre in contactos:
                del contactos[nombre]
                print("🗑️ Contacto eliminado")
            else:
                print("❌ Contacto no existe")

        # MOSTRAR TODOS
        elif opcion == "5":
            if contactos:
                print("\n📋 Lista de contactos:")
                for nombre, telefono in contactos.items():
                    print(f"- {nombre}: {telefono}")
            else:
                print("📭 Agenda vacía")

        # SALIR
        elif opcion == "6":
            print("👋 Saliendo del programa...")
            break

        else:
            print("❌ Opción inválida")


# Ejecutar programa
agenda()