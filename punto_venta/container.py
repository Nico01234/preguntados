from tkinter import *
import tkinter as tk
from ventas import Ventas
from inventario import Inventario
from colores import *
from fuentes import *


class Container(Frame):
    def __init__(self, padre):
        super().__init__(padre)
        self.pack()
        self.place(x= 0, y= 0, width= 800, height= 400)
        self.config(bg= "#BB2808")
        self.widgets()
        
    def show_frames(self, container):
        top_level = tk.Toplevel(self)
        frame = container(top_level)
        frame.config(bg= "#BB2808")
        frame.pack(fill = "both", expand= True)
        top_level.geometry("1100x650+120+20")
        top_level.resizable(False, False)
        
        top_level.transient(self.master)
        top_level.grab_set()
        top_level.focus_set()
        top_level.lift()
        
        
    def ventas(self):
        self.show_frames(Ventas)
        
    def inventario(self):
        self.show_frames(Inventario)
        
    def widgets(self):
        
        frame1 = tk.Frame(self, bg= "#BB2808")
        frame1.pack()
        frame1.place(x=0, y=0, width=800, height=400)
        
        button_ventas = Button(frame1, bg="#E3A792", fg= "#242424", font= font_button,text= "Ir a ventas", command=self.ventas)
        button_ventas.place(x=300, y= 30, width=240, height=60)
        
        button_inventarios = Button(frame1, bg="#E3A792", fg= "#242424", font= font_button, text= "Ir a inventarios", command=self.inventario)
        button_inventarios.place(x=300, y= 130, width=240, height=60)
        