from tkinter import Tk, Frame
from container import *
from colores import *
from ttkthemes import *

class Manager(Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Caja Registradora version 1.0")
        self.resizable(False, False)
        self.configure(bg="#BB2808")
        self.geometry("800x400+120+20")
        
        self.container = Frame(self, bg="#BB2808")
        self.container.pack(fill="both", expand=True)
        
        self.frames = {
            Container : None
        }
        
        self.load_frames()
        
        self.show_frames(Container)
        
        self.set_theme()
        
    def load_frames(self):
        for FrameClass in self.frames.keys():
            frame = FrameClass(self.container)
            self.frames[FrameClass] = frame
            
    def show_frames(self, frame_class):
        frame = self.frames[frame_class]
        frame.tkraise()
        
    def set_theme(self):
        style = ThemedStyle(self)
        style.set_theme("breeze")
        
    def main():
        app = Manager()
        app.mainloop()
    
    if __name__ == "__main__":
        main()
        