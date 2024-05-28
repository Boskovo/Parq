from tkinter import *
import customtkinter
from gui_functions import *
from PIL import ImageTk, Image

#gui scale for widgets
customtkinter.set_widget_scaling(1.8)

#Main page
class MainPage(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # add widgets here
        button1 = customtkinter.CTkButton(master=self, 
        text="Standaard", 
        fg_color='#006633',
        hover_color='#00592C',
        corner_radius=5,
        command=lambda: change_frame(self,page1))

        button2 = customtkinter.CTkButton(master=self, 
        text="Rollator", 
        fg_color='#006633',
        hover_color='#00592C',
        corner_radius=5,
        command=lambda: change_frame(self,page2))

        button3 = customtkinter.CTkButton(master=self, 
        text="Rolstoel",
        fg_color='#006633', 
        hover_color='#00592C',
        corner_radius=5, 
        command=lambda: change_frame(self,page3))

        mainlogo = Image.open("./images/walkintheparq-logo.png")
        
        mainlogo = mainlogo.resize((945, 242))

        test = ImageTk.PhotoImage(mainlogo)
        
        label = Label(image=test)
        
        button1.place(relx=0.15, rely=0.5, anchor=customtkinter.CENTER)
        button2.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)
        button3.place(relx=0.85, rely=0.5, anchor=customtkinter.CENTER)
        label.place(relx=0.5, rely=0.25, anchor=customtkinter.CENTER)

        self.centerphoto = test

#Currently an empty second page
class NewPage(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        
        #add widgets here
        

#The app itself
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Walk In The ParQ")
        self.geometry("1024x600")
        self.grid_rowconfigure(0, weight=1)  # configure grid system
        self.grid_columnconfigure(0, weight=1)

        self.my_frame = MainPage(master=self)
        self.my_frame.grid(row=0, column=0, sticky="nsew")


app = App()
page1 = NewPage(app)
page2 = NewPage(app)
page3 = NewPage(app)

app.mainloop()