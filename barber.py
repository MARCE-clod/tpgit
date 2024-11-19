
import json
import tkinter as tk
from tkinter import messagebox

class Cliente:
    def __init__(self, nombre, fecha, hora):
        self.nombre = nombre
        self.fecha = fecha
        self.hora = hora

class Barberia:
    def __init__(self, archivo):
        self.archivo = archivo
        self.clientes = self.cargar_clientes()

    def cargar_clientes(self):
        try:
            with open(self.archivo, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def guardar_clientes(self):
        with open(self.archivo, 'w') as f:
            json.dump(self.clientes, f, indent=4)

    def agregar_clientes(self, nombre, fecha, hora):
        cliente = {
            'nombre': nombre,
            'fecha': fecha,
            'hora': hora
        }
        self.clientes.append(cliente)
        self.guardar_clientes()

    def eliminar_cliente(self, nombre):
        self.clientes = [c for c in self.clientes if c['nombre'] != nombre]
        self.guardar_clientes()

    def obtener_clientes(self):
        return self.clientes

class InterfazBarberia:
    def __init__(self, root, barberia):
        self.barberia = barberia
        self.root = root
        self.root.title("Gestión de Barbería")

        self.label_nombre = tk.Label(root, text="Nombre:")
        self.label_nombre.grid(row=0, column=0, padx=5, pady=5)
        self.entry_nombre = tk.Entry(root)
        self.entry_nombre.grid(row=0, column=1, padx=5, pady=5)

        self.label_fecha = tk.Label(root, text="Fecha :")
        self.label_fecha.grid(row=1, column=0, padx=5, pady=5)
        self.entry_fecha = tk.Entry(root)
        self.entry_fecha.grid(row=1, column=1, padx=5, pady=5)

        self.label_hora = tk.Label(root, text="Hora (HH:MM):")
        self.label_hora.grid(row=2, column=0, padx=5, pady=5)
        self.entry_hora = tk.Entry(root)
        self.entry_hora.grid(row=2, column=1, padx=5, pady=5)

        self.btn_agregar = tk.Button(root, text="Agregar Cliente", command=self.agregar_cliente)
        self.btn_agregar.grid(row=3, column=0, columnspan=2, pady=10)

        self.btn_eliminar = tk.Button(root, text="Eliminar Cliente", command=self.eliminar_cliente)
        self.btn_eliminar.grid(row=4, column=0, columnspan=2, pady=10)

        self.btn_mostrar = tk.Button(root, text="Mostrar Clientes", command=self.mostrar_clientes)
        self.btn_mostrar.grid(row=5, column=0, columnspan=2, pady=10)

        self.text_area = tk.Text(root, height=10, width=40)
        self.text_area.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

    def agregar_cliente(self):
        nombre = self.entry_nombre.get()
        fecha = self.entry_fecha.get()
        hora = self.entry_hora.get()

        if not nombre or not fecha or not hora:
            messagebox.showerror("Error", "Todos los campos son obligatorios.")
            return

        self.barberia.agregar_clientes(nombre, fecha, hora)
        messagebox.showinfo("Éxito", f"Cliente {nombre} agregado exitosamente.")
        self.limpiar_campos()

    def eliminar_cliente(self):
        nombre = self.entry_nombre.get()

        if not nombre:
            messagebox.showerror("Error", "El nombre es obligatorio para eliminar un cliente.")
            return

        self.barberia.eliminar_cliente(nombre)
        messagebox.showinfo("Éxito", f"Cliente {nombre} eliminado exitosamente.")
        self.limpiar_campos()

    def mostrar_clientes(self):
        self.text_area.delete("1.0", tk.END)  # Limpiar área de texto
        clientes = self.barberia.obtener_clientes()
        if not clientes:
            self.text_area.insert(tk.END, "No hay clientes registrados.\n")
        else:
            for cliente in clientes:
                self.text_area.insert(tk.END, f"Nombre: {cliente['nombre']}\n")
                self.text_area.insert(tk.END, f"Fecha: {cliente['fecha']}\n")
                self.text_area.insert(tk.END, f"Hora: {cliente['hora']}\n\n")

    def limpiar_campos(self):
        self.entry_nombre.delete(0, tk.END)
        self.entry_fecha.delete(0, tk.END)
        self.entry_hora.delete(0, tk.END)

# Inicializar la aplicación
if __name__ == "__main__":
    archivo = 'cliente.json'
    barberia = Barberia(archivo)
    root = tk.Tk()
    app = InterfazBarberia(root, barberia)
    root.mainloop()

