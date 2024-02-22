class NotasApp:
    def __init__(self):
        self.tareas = []

    def mostrar_menu_principal(self):
        print("----- TUS NOTAS -----")
        print("1. Agregar Tarea")
        print("2. Ver Notas")
        print("3. Editar Tarea")
        print("4. Eliminar Tarea")
        print("5. Salir")

    def agregar_tarea(self):
        print("\n--- Agregar Tarea ---")
        titulo = input("Título: ")
        descripcion = input("Descripción: ")
        fecha = input("Fecha: ")
        tarea = {"Título": titulo, "Descripción": descripcion, "Fecha": fecha}
        self.tareas.append(tarea)
        print("Tarea agregada con éxito!")

    def ver_tareas(self):
        print("\n--- Lista de Tareas ---")
        for i, tarea in enumerate(self.tareas, start=1):
            print(f"{i}. Título: {tarea['Título']}, Descripción: {tarea['Descripción']}, Fecha: {tarea['Fecha']}")
        print()

    def editar_tarea(self):
        self.ver_tareas()
        opcion = int(input("Seleccione el número de tarea a editar (0 para cancelar): "))
        if opcion == 0:
            return
        if 1 <= opcion <= len(self.tareas):
            tarea = self.tareas[opcion - 1]
            print("\n--- Editar Tarea ---")
            tarea["Título"] = input(f"Nuevo Título ({tarea['Título']}): ") or tarea["Título"]
            tarea["Descripción"] = input(f"Nueva Descripción ({tarea['Descripción']}): ") or tarea["Descripción"]
            tarea["Fecha"] = input(f"Nueva Fecha ({tarea['Fecha']}): ") or tarea["Fecha"]
            print("Tarea editada con éxito!")
        else:
            print("Número de tarea inválido.")

    def eliminar_tarea(self):
        self.ver_tareas()
        opcion = int(input("Seleccione el número de tarea a eliminar (0 para cancelar): "))
        if opcion == 0:
            return
        if 1 <= opcion <= len(self.tareas):
            tarea = self.tareas.pop(opcion - 1)
            print(f"Tarea '{tarea['Título']}' eliminada con éxito!")
        else:
            print("Número de tarea inválido.")

    def ejecutar(self):
        while True:
            self.mostrar_menu_principal()
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.agregar_tarea()
            elif opcion == "2":
                self.ver_tareas()
            elif opcion == "3":
                self.editar_tarea()
            elif opcion == "4":
                self.eliminar_tarea()
            elif opcion == "5":
                print("¡Hasta luego!")
                break
            else:
                print("Opción inválida. Intente de nuevo.")


if __name__ == "__main__":
    app = NotasApp()
    app.ejecutar()