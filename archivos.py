import tkinter as tk
from tkinter import messagebox, simpledialog

class Archivo:
    def __init__(self, nombre, tamano, tipo):
        self.nombre = nombre
        self.tamano = tamano  # en KB
        self.tipo = tipo        

    def __repr__(self):
        return f"{self.nombre} ({self.tamano} KB) - {self.tipo}"

class BuscadorArchivosApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Buscador de Archivos")
        
        # Arreglo (lista) para almacenar objetos Archivo
        self.archivos = []  # Arreglos
        
        # Matriz (lista de listas) para almacenar información adicional
        self.matrices_archivos = []  # Matrices

        # Archivos predeterminados
        self.archivos_predeterminados = [
            Archivo("foto1.jpg", 250, ".jpg"),
            Archivo("documento1.txt", 15, ".txt"),
            Archivo("presentacion.pptx", 100, ".pptx")
        ]

        # Agregar archivos predeterminados a la lista
        self.archivos.extend(self.archivos_predeterminados)

        # Ordenar los archivos predeterminados
        self.merge_sort(self.archivos)

        self.label = tk.Label(master, text="Buscador de Archivos\nCreado por: Sebastián Hurtado", font=("Arial", 14))
        self.label.pack(pady=10)

        self.boton_agregar = tk.Button(master, text="Agregar Archivo", command=self.agregar_archivo)
        self.boton_agregar.pack(pady=5)

        self.boton_buscar = tk.Button(master, text="Buscar Archivo", command=self.buscar_archivo)
        self.boton_buscar.pack(pady=5)

        self.boton_mostrar = tk.Button(master, text="Mostrar Archivos", command=self.mostrar_archivos)
        self.boton_mostrar.pack(pady=5)

        # Botón para ordenar archivos
        self.boton_ordenar = tk.Button(master, text="Ordenar Archivos", command=self.ordenar_archivos)
        self.boton_ordenar.pack(pady=5)

        self.texto_archivos = tk.Text(master, width=50, height=15)
        self.texto_archivos.pack(pady=10)

    def agregar_archivo(self):
        nombre = simpledialog.askstring("Nombre del archivo", "Ingrese el nombre del archivo:")
        tamano = simpledialog.askinteger("Tamaño del archivo", "Ingrese el tamaño del archivo (KB):")
        tipo = simpledialog.askstring("Tipo del archivo", "Ingrese el tipo del archivo (ejemplo: .txt, .jpg):")
        
        if nombre and tamano and tipo:
            # Agregar objeto Archivo a la lista
            self.archivos.append(Archivo(nombre, tamano, tipo))
            
            # Agregar información a la matriz
            self.matrices_archivos.append([nombre, tamano, tipo])  # Matrices
            
            messagebox.showinfo("Éxito", "Archivo agregado.")
        else:
            messagebox.showwarning("Advertencia", "Por favor, complete todos los campos.")

    def merge_sort(self, archivos):
        if len(archivos) > 1:
            mid = len(archivos) // 2
            izquierda = archivos[:mid]
            derecha = archivos[mid:]

            # Llamadas recursivas para ordenar las dos mitades
            self.merge_sort(izquierda)
            self.merge_sort(derecha)

            i = j = k = 0

            # Copiar datos a la lista original
            while i < len(izquierda) and j < len(derecha):
                if izquierda[i].nombre < derecha[j].nombre:
                    archivos[k] = izquierda[i]
                    i += 1
                else:
                    archivos[k] = derecha[j]
                    j += 1
                k += 1

            # Comprobar si quedan elementos
            while i < len(izquierda):
                archivos[k] = izquierda[i]
                i += 1
                k += 1

            while j < len(derecha):
                archivos[k] = derecha[j]
                j += 1
                k += 1

    def busqueda_binaria(self, nombre):
        bajo = 0
        alto = len(self.archivos) - 1

        while bajo <= alto:
            medio = (bajo + alto) // 2
            if self.archivos[medio].nombre.lower() == nombre.lower():
                return medio
            elif self.archivos[medio].nombre.lower() < nombre.lower():
                bajo = medio + 1
            else:
                alto = medio - 1
        return -1  # No encontrado

    def buscar_archivo(self):
        nombre = simpledialog.askstring("Buscar archivo", "Ingrese el nombre del archivo a buscar:")
        if nombre:
            index = self.busqueda_binaria(nombre)
            if index != -1:
                archivo = self.archivos[index]
                messagebox.showinfo("Archivo encontrado", f"Archivo: {archivo}")
            else:
                messagebox.showinfo("No encontrado", "Archivo no encontrado.")
        else:
            messagebox.showwarning("Advertencia", "Por favor, ingrese un nombre.")

    def ordenar_archivos(self):
        self.merge_sort(self.archivos)  # Ordenar utilizando Merge Sort
        messagebox.showinfo("Éxito", "Archivos ordenados por nombre.")

    def mostrar_archivos(self):
        self.texto_archivos.delete(1.0, tk.END)  # Limpiar el área de texto
        if self.archivos:
            for archivo in self.archivos:
                self.texto_archivos.insert(tk.END, f"{archivo}\n")
        else:
            self.texto_archivos.insert(tk.END, "No hay archivos para mostrar.")

def main():
    root = tk.Tk()
    app = BuscadorArchivosApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
