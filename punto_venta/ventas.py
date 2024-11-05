# The `Ventas` class in the provided Python code represents a GUI application for managing sales
# transactions, including functionalities for adding products, calculating totals, processing
# payments, and viewing sales invoices.
from tkinter import *
import tkinter as tk
from tkinter import messagebox, ttk
from colores import *
from fuentes import *
import sqlite3
import tkinter.font as tkFont
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.platypus import Table
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
import datetime
import os
import subprocess



class Ventas(tk.Frame):
    
    db_name = "index.db"
    
    def __init__(self, parent):
        super().__init__(parent)
        self.pack()
        self.numero_factura_actual = self.obtener_numero_factura_actual()
        self.widgets()
        self.configurar_autocompletado()  
        self.mostrar_numero_factura()
        
    def widgets(self):
        
        self.font_productos = tkFont.Font(family="Helvetica", size=20)

        
        frame1 = tk.Frame(self, bg= color_principal)
        frame1.pack()
        #contiene el titulo
        frame1.place(x= 0, y= 0, width=1100, height=100)
        
        titulo = tk.Label(self, text="VENTAS", font=font_venta,fg= blanco,bg= color_principal)
        titulo.pack()
        titulo.place(x=5, y=0, width=1090, height=90)
        
        frame2 = tk.Frame(self, bg= gris )
        frame2.place(x=0, y=100, width=1100, height=550)
        
        lblframe = LabelFrame(frame2, text="Informacion de la venta", bg= gris, font= font_venta)
        lblframe.place(x=10, y=10, width=1060, height= 450)
        
        label_numero_factura = tk.Label(lblframe, text="Numero de\nfactura: ", bg= gris, font= font_venta)
        label_numero_factura.place(x=10, y=5)
        self.numero_factura = tk.StringVar()
        
        self.entry_numero_factura = ttk.Entry(lblframe, textvariable= self.numero_factura, state= "readonly", font= font_venta )
        self.entry_numero_factura.place(x=260, y=10, width=350)


        label_nombre = tk.Label(lblframe, text="Productos: ", bg= gris, font= font_venta)
        label_nombre.place(x=160, y=12)
        self.entry_nombre = ttk.Combobox(lblframe, font=self.font_productos)
        self.entry_nombre.place(x=260, y=10, width=350, height=40)
        
        self.entry_nombre.bind('<KeyRelease>', self.buscar_productos)
        self.entry_nombre.bind('<Return>', self.actualizar_precio)  
        self.entry_nombre.bind("<<ComboboxSelected>>", self.actualizar_precio)
        self.entry_nombre.bind('<Up>', self.navegar_sugerencias)


        self.cargar_productos()

        label_valor = tk.Label(lblframe, text= "Precio: ", bg= gris, font= font_venta)
        label_valor.place(x= 620, y=12)
        self.entry_valor = ttk.Entry(lblframe, font=font_venta)
        self.entry_valor.place(x=690, y=12, width=120)
    
        
        label_cantidad = tk.Label(lblframe, text="Cantidad: ", bg=gris, font=font_venta)
        label_cantidad.place(x= 810, y= 12)
        self.entry_cantidad = ttk.Entry(lblframe, font= font_venta)
        self.entry_cantidad.place(x= 900, y=10, width=150)
        
        self.entry_cantidad.bind("<Return>", self.registrar_conteo)
        
        treFrame = tk.Frame(frame2, bg=gris)
        treFrame.place(x=180, y=120, width=800, height=200)
        
        scrol_y = ttk.Scrollbar(treFrame, orient=VERTICAL)
        scrol_y.pack(side=RIGHT, fill=Y)
        
        scrol_x = ttk.Scrollbar(treFrame, orient=HORIZONTAL)
        scrol_x.pack(side=BOTTOM, fill=X)
        
        self.tree = ttk.Treeview(treFrame, columns= ("Producto", "Precio", "Cantidad", "Subtotal"), show="headings", height=10, yscrollcommand=scrol_y.set, xscrollcommand=scrol_x.set)
        scrol_y.config(command= self.tree.yview)
        scrol_x.config(command= self.tree.xview)
        
        self.tree.heading("#1", text="Producto")
        self.tree.heading("#2", text="Precio")
        self.tree.heading("#3", text="Cantidad")
        self.tree.heading("#4", text="Subtotal")
        
        self.tree.column("Producto", anchor= "center")
        self.tree.column("Precio", anchor= "center")
        self.tree.column("Cantidad", anchor= "center")
        self.tree.column("Subtotal", anchor= "center")
        
        self.tree.pack(expand=True, fill=BOTH)
        
        lblframe1 = LabelFrame(frame2, text="Opciones", bg=gris, font=font_venta)
        lblframe1.place(x=10, y=300, width=1060, height=100)
        
        
        boton_agregar = tk.Button(lblframe1, text="Agregar Articulo", bg=blanco, font=font_venta, command=self.registrar)
        boton_agregar.place(x=50, y=10, width=240, height=50)
        
        boton_eliminar = tk.Button(lblframe1, text="Eliminar Artículo", bg=blanco, font=font_venta, command=self.eliminar_producto)
        boton_eliminar.place(x=300, y=10, width=240, height=50)
        
        boton_pagar = tk.Button(lblframe1, text="Pagar", bg=blanco, font=font_venta, command=self.abrir_ventana_pago)
        boton_pagar.place(x=550, y=10, width=240, height=50)
        
        boton_ver_facturas = tk.Button(lblframe1, text="Ver Facturas", bg=blanco, font=font_venta, command=self.abrir_ventana_factura)
        boton_ver_facturas.place(x=800, y=10, width=240, height=50)

        
        self.label_suma_total = tk.Label(frame2, text="Total a pagar: $ 0", bg=blanco, font=font_venta_total)
        self.label_suma_total.place(x=420, y=430)
        
    
    def eliminar_producto(self):
        selected_item = self.tree.selection()
        if selected_item:
            self.tree.delete(selected_item)
            self.actualizar_total()
        else:
            messagebox.showerror("Error", "Seleccione un artículo para eliminar.")    
        
    def buscar_productos(self, event):
        texto_busqueda = self.entry_nombre.get().lower()
        tecla_presionada = event.keysym

        # Si se presiona "Backspace" o "Delete", no hacer autocompletado
        if tecla_presionada in ("BackSpace", "Delete"):
            return
        if texto_busqueda == "":
            self.cargar_productos()
            return

        try:
            conn = sqlite3.connect(self.db_name)
            c = conn.cursor()
            c.execute("SELECT nombre FROM inventario WHERE LOWER(nombre) LIKE ?", ('%' + texto_busqueda + '%',))
            productos = c.fetchall()
    
            self.sugerencias.delete(0, tk.END)
            for producto in productos:
                self.sugerencias.insert(tk.END, producto[0])
    
            # Si hay productos, mostrar la lista de sugerencias
            if productos:
                self.sugerencias.place(x=270, y=180, width=350)
    
                # Si hay exactamente un producto, actualiza automáticamente el precio
                if len(productos) == 1:
                    self.entry_nombre.set(productos[0][0])
                    self.actualizar_precio(None)
    
            else:
                self.sugerencias.place_forget()
    
            conn.close()

        except sqlite3.Error as e:
            print("Error al buscar productos en la base de datos:", e)


    def seleccionar_sugerencia(self, event):
        seleccion = self.sugerencias.curselection()
        if seleccion:
            producto = self.sugerencias.get(seleccion[0])
            self.entry_nombre.set(producto)
            self.sugerencias.place_forget()  # Ocultar el Listbox después de seleccionar
    
            # Llamar a actualizar_precio después de seleccionar el producto
            self.actualizar_precio(None)

        
    def configurar_autocompletado(self):
        self.sugerencias = tk.Listbox(self, font=self.font_productos, height=5)
        self.sugerencias.place(x=270, y=180, width=350)
        self.sugerencias.place_forget()
        self.sugerencias.bind("<ButtonRelease-1>", self.seleccionar_sugerencia)
        self.sugerencias.bind("<Up>", self.navegar_sugerencias)
        self.sugerencias.bind("<Down>", self.navegar_sugerencias)
        self.sugerencias.bind("<Return>", self.seleccionar_sugerencia)

    def navegar_sugerencias(self, event):
        if self.sugerencias.size() > 0:
            # Obtiene la selección actual
            seleccion = self.sugerencias.curselection()
            if len(seleccion) > 0:
                nuevo_indice = seleccion[0] - 1
            else:
                nuevo_indice = self.sugerencias.size() - 1
            
            if nuevo_indice < 0:
                nuevo_indice = self.sugerencias.size() - 1
            
            self.sugerencias.selection_clear(0, tk.END)
            self.sugerencias.activate(nuevo_indice)
            self.sugerencias.selection_set(nuevo_indice)
            self.sugerencias.see(nuevo_indice)
            self.entry_nombre.set(self.sugerencias.get(nuevo_indice))

        
    def buscar_productos(self, event):
        texto_busqueda = self.entry_nombre.get().lower()
        tecla_presionada = event.keysym
    
        # Si se presiona "Backspace" o "Delete", no hacer autocompletado
        if tecla_presionada in ("BackSpace", "Delete"):
            return
        if texto_busqueda == "":
            self.sugerencias.place_forget()
            return
    
        try:
            conn = sqlite3.connect(self.db_name)
            c = conn.cursor()
            c.execute("SELECT nombre FROM inventario WHERE LOWER(nombre) LIKE ?", ('%' + texto_busqueda + '%',))
            productos = c.fetchall()
            
            self.sugerencias.delete(0, tk.END)
            for producto in productos:
                self.sugerencias.insert(tk.END, producto[0])
            
            if productos:
                self.sugerencias.place(x=270, y=180, width=350)  # Mostrar el Listbox
            else:
                self.sugerencias.place_forget()  # Ocultar el Listbox
            
            conn.close()
                
        except sqlite3.Error as e:
            print("Error al buscar productos en la base de datos:", e)
            

    def seleccionar_producto(self, event):
        seleccion = self.entry_nombre["values"]
        if seleccion:
            producto = self.sugerencias.curselection()
            self.entry_nombre.set(producto[0])  # Selecciona el primer producto filtrado
            self.actualizar_precio(None)  # Actualiza el precio del producto seleccionado
            self.sugerencias.place_forget()
            
    def seleccionar_sugerencia(self, event):
        seleccion = self.sugerencias.curselection()
        if seleccion:
            producto = self.sugerencias.get(seleccion[0])
            self.entry_nombre.set(producto)
            self.sugerencias.place_forget()  # Ocultar el Listbox después de seleccionar
            self.actualizar_precio(None)
        
    def cargar_productos(self):
        try:
            conn = sqlite3.connect(self.db_name)
            c = conn.cursor()
            c.execute("SELECT nombre FROM inventario")
            productos = c.fetchall()
            self.entry_nombre["values"] = [producto[0] for producto in productos]
            if not productos:
                print("Producto no encontrado")
            conn.close()
        except sqlite3.Error as e:
            print("Error al cargar productos desde la base de datos:", e)
            
            
    def actualizar_precio(self, event):
        nombre_producto = self.entry_nombre.get()
        
        
        try:
            conn = sqlite3.connect(self.db_name)
            c = conn.cursor()
            c.execute("SELECT Precio FROM inventario WHERE nombre = ?", (nombre_producto,))
            precio = c.fetchone() #obtiene resultado de la consulta
            if precio:
                self.entry_valor.config(state="normal")
                self.entry_valor.delete(0, tk.END)
                self.entry_valor.insert(0, precio[0])
                self.entry_valor.config(state="readonly")
            else:
                self.entry_valor.config(state="normal")
                self.entry_valor.delete(0, tk.END)
                self.entry_valor.insert(0, "Precio no disponible")
                self.entry_valor.config(state="readonly")
                
        except sqlite3.Error as e:
            messagebox.showerror("Error", f"Error al obtener el precio: {e}")
        finally:
            conn.close()
            
    def actualizar_total(self):
        total = 0.0
        for child in self.tree.get_children():
            subtotal = float(self.tree.item(child, "values") [3])
            total += subtotal
        self.label_suma_total.config(text=f"Total a pagar: $ {total:.0f}")
        
    def registrar_conteo(self, event=None):
        self.registrar()

        
    def registrar(self, event=None):
        producto = self.entry_nombre.get()
        precio = self.entry_valor.get()
        cantidad = self.entry_cantidad.get()
        
        if producto and precio and cantidad:
            try:
                cantidad = int(cantidad)
                if not self.verificar_stock(producto, cantidad):
                    messagebox.showerror("Error", "Stock Insuficiente para el producto seleccionado")
                    return 
                precio = float(precio)
                subtotal = cantidad * precio
                
                self.tree.insert("","end", values = (producto, f"{precio:.0f}", cantidad, f"{subtotal:.0f}"))
                
                self.entry_nombre.set("")
                self.entry_valor.config(state="normal")
                self.entry_valor.delete(0, tk.END)
                self.entry_valor.config(state="readonly")
                self.entry_cantidad.delete(0, tk.END)
                
                self.actualizar_total()
                
            except ValueError:
                messagebox.showerror("Error", "Cantidad o precio no validos")
        else:
            messagebox.showerror("Error", "Debe completar todos los campos")
            
    def verificar_stock(self, nombre_producto, cantidad):
        try:
            conn = sqlite3.connect(self.db_name)
            c = conn.cursor()
            c.execute("SELECT stock FROM Inventario WHERE nombre = ?", (nombre_producto,))
            stock = c.fetchone()
            if stock and stock[0] >= cantidad:
                return True
            return False
        except sqlite3.Error as e:
            messagebox.showerror("Error", f"Error al verficar el stock: {e}")
            return False
        finally:
            conn.close()
            
    def obtener_total(self):
        total = 0.0
        for child in self.tree.get_children():
            subtotal = float(self.tree.item(child, "values")[3])
            total += subtotal
        return total 
    
    def abrir_ventana_pago(self):
        if not self.tree.get_children():
            messagebox.showerror("Error", "No hay articulos para pagar")
            return
        
        ventana_pago = Toplevel(self)
        ventana_pago.title("Realizar Pago")
        ventana_pago.geometry("400x400")
        ventana_pago.config(bg=gris)
        ventana_pago.resizable(False, False)
        ventana_pago.lift()
        

        label_total = tk.Label(ventana_pago, bg=gris, text=f"Total a pagar: $ {self.obtener_total():.0f}", font=font_ventana_pagar)
        label_total.place(x=70, y=20)
        
        label_cantidad_pagada = tk.Label(ventana_pago, bg=gris, text="Cantidad pagada: ", font=font_venta)
        label_cantidad_pagada.place(x=100, y=90)
        entry_cantidad_pagada = ttk.Entry(ventana_pago, font=font_venta)
        entry_cantidad_pagada.place(x=100, y=130)
        entry_cantidad_pagada.focus()
        
        label_cambio = tk.Label(ventana_pago, bg=gris, text="", font=font_venta)
        label_cambio.place(x=100, y=190)
        
        
        def calcular_cambio():
            try:
                cantidad_pagada = float(entry_cantidad_pagada.get().strip())
                total = self.obtener_total()
                cambio = cantidad_pagada - total
                if cambio < 0:
                    messagebox.showerror("Error", "Pago Insuficiente")
                    return
                label_cambio.config(text=f"Vuelto: $ {cambio:.0f}")
            except ValueError:
                messagebox.showerror("Error", "Cantidad pagada no valido")
                
        ventana_pago.bind('<Return>', lambda event: calcular_cambio())
        
        button_calcular = tk.Button(ventana_pago, text="Calcular Vuelto", bg=blanco, font=font_venta, command=calcular_cambio)
        button_calcular.place(x=100, y=240, width= 240, height=40)
        
        ventana_pago.bind('<Control-p>', lambda event: self.pagar(ventana_pago, entry_cantidad_pagada, label_cambio))

        button_pagar = tk.Button(ventana_pago, text="Pagar", bg=blanco, font=font_venta, command=lambda: self.pagar(ventana_pago, entry_cantidad_pagada, label_cambio))
        button_pagar.place(x=100, y=300, width= 240, height=40)
        
    def pagar(self, ventana_pago, entry_cantidad_pagada, label_cambio):
        try:
            cantidad_pagada = float(entry_cantidad_pagada.get())
            total = self.obtener_total() 
            cambio = cantidad_pagada - total
            if cambio < 0:
                messagebox.showerror("Error", "La cantidad pagada es insuficiente")
                return

            conn = sqlite3.connect(self.db_name)
            c = conn.cursor()
            try:
                productos = []
                for child in self.tree.get_children():
                    item = self.tree.item(child, "values")
                    producto = item[0]
                    precio = float(item[1])
                    cantidad_vendida = int(item[2])
                    subtotal = float(item[3])
                    productos.append((producto, precio, cantidad_vendida, subtotal))
                    # if not self.verificar_stock(producto, cantidad_vendida):
                    #     messagebox.showerror("Error", f"Stock insuficiente para el producto: {producto}")
                    #     return
                    
                    c.execute("INSERT INTO ventas (factura, articulo, valor, cantidad, subtotal) VALUES (?,?,?,?,?)",(self.numero_factura_actual, producto, float(precio), cantidad_vendida, subtotal))

                    c.execute("UPDATE inventario SET stock = stock - ? WHERE Nombre = ?", (cantidad_vendida, producto))
        
                conn.commit()
                messagebox.showinfo("Exito", "Venta registrada exitosamente")
                
                self.numero_factura_actual += 1 
                self.mostrar_numero_factura()
                
                for child in self.tree.get_children():
                    self.tree.delete(child)
                self.label_suma_total.config(text="Total a pagar: $ 0")
                
                ventana_pago.destroy()
                
                fecha = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                self.generar_factura_pdf(productos, total, self.numero_factura_actual -1, fecha)
                
                
            except sqlite3.Error as e:
                conn.rollback()
                messagebox.showerror("Error", f"Error al registrar la venta: {e}")
            finally:
                conn.close()
                
        except ValueError:
            messagebox.showerror("Error", "Cantidad pagada no valida")
            
    def generar_factura_pdf(self, productos, total, factura_numero, fecha):
        if not os.path.exists("facturas"):
            os.makedirs("facturas")
        archivo_pdf = f"facturas/factura_{factura_numero}.pdf"
        
        c = canvas.Canvas(archivo_pdf, pagesize=letter)
        width, height = letter
        
        style = getSampleStyleSheet()
        estilo_titulo = style["title"]
        estilo_normal = style["Normal"]
        
        c.setFont("Helvetica-Bold", 16)
        c.drawString(100, height - 50, f"factura #{factura_numero}")
        
        c.setFont("Helvetica-Bold", 16)
        c.drawString(100, height - 70, f"fecha #{fecha}")
        
        c.setFont("Helvetica-Bold", 16)
        c.drawString(100, height - 90, "Informacion de la venta")
        
        data = [["Producto", "Precio", "Cantidad", "Subtotal"]] + productos
        table = Table(data)
        table.wrapOn(c, width - 100, height - 150)
        table.drawOn(c, 100, height - 150)
        
        c.setFont("Helvetica-Bold", 16)
        c.drawString(100, height - 250, f"total a pagar: $ {total:.0f}")
        
        c.setFont("Helvetica-Bold", 12)
        c.drawString(100, height - 270, "Gracias por su compra :)")
        
        c.save()
        
        messagebox.showinfo("Factura Generada", f"Factura N° {factura_numero} ha sido creada exitosamente")
        
        subprocess.call(["open",archivo_pdf])
        
    def obtener_numero_factura_actual(self):
        conn = sqlite3.connect(self.db_name)
        c = conn.cursor()
        try:
            c.execute("SELECT MAX(factura) FROM ventas")
            max_factura = c.fetchone()[0]
            if max_factura:
                return max_factura + 1 
            else:
                return 1
        except sqlite3.Error as e:
            messagebox.showerror("Error", f"Error al obtener el numero de factura: {e}")
            return 1
        finally:
            conn.close()
            
    def mostrar_numero_factura(self):
        self.numero_factura.set(self.numero_factura_actual)
        
    def abrir_ventana_factura(self):
        ventana_facturas = Toplevel(self)
        ventana_facturas.title("Factura")
        ventana_facturas.geometry("800x500")
        ventana_facturas.config(bg=gris)
        ventana_facturas.resizable(False, False)
        
        
        facturas = Label(ventana_facturas, bg=negro, text="Facturas Registradas", font=font_venta_total)
        facturas.place(x=150, y=15)
        
        treFrame = tk.Frame(ventana_facturas, bg=blanco)
        treFrame.place(x=10, y=100, width= 700, height=380)
        
        scrol_y = ttk.Scrollbar(treFrame, orient=VERTICAL)
        scrol_y.pack(side=RIGHT, fill=Y)
        
        scrol_x = ttk.Scrollbar(treFrame, orient=HORIZONTAL)
        scrol_x.pack(side=BOTTOM, fill=X)
        
        tree_facturas = ttk.Treeview(treFrame, columns= ("ID", "Factura", "Producto", "Precio", "Cantidad", "Subtotal"), show="headings", height=10)
        tree_facturas.pack(expand=True, fill=BOTH)

        tree_facturas.config(yscrollcommand=scrol_y.set, xscrollcommand=scrol_x.set)
        scrol_y.config(command= tree_facturas.yview)
        scrol_x.config(command= tree_facturas.xview)
        
        tree_facturas.heading("#1", text="ID")
        tree_facturas.heading("#2", text="Factura")
        tree_facturas.heading("#3", text="Producto")
        tree_facturas.heading("#4", text="Precio")
        tree_facturas.heading("#5", text="Cantidad")
        tree_facturas.heading("#6", text="Subtotal")
        
        tree_facturas.column("ID", width=70 , anchor= "center")
        tree_facturas.column("Factura", width=100 , anchor= "center")
        tree_facturas.column("Producto", width=200 , anchor= "center")
        tree_facturas.column("Precio", width=130 , anchor= "center")
        tree_facturas.column("Cantidad", width=130 , anchor= "center")
        tree_facturas.column("Subtotal", width=130 , anchor= "center")
        
        #tree_facturas.pack(expand=True, fill=BOTH)
        
        self.cargar_facturas(tree_facturas)
        
    def cargar_facturas(self, tree):
        try:
            conn = sqlite3.connect(self.db_name)
            c = conn.cursor()
            c.execute("SELECT * FROM ventas")
            facturas = c.fetchall()
            
            for row in tree.get_children():
                tree.delete(row)
                
            for factura in facturas:
                tree.insert("", "end", values= factura)
            
        except sqlite3.Error as e:
            messagebox.showerror("Error", f"Error al cargar las facturas: {e}")
            
        finally:
            conn.close()