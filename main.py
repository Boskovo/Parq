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
        text="button1", 
        fg_color='#006633',
        hover_color='#00592C', 
        command=lambda: change_frame(self,newpage))

        button2 = customtkinter.CTkButton(master=self, text="button2", fg_color='#006633',hover_color='#00592C')
        button3 = customtkinter.CTkButton(master=self, text="button3", fg_color='#006633',hover_color='#00592C')

        image = Image.open("./images/image.jpg")
        test = ImageTk.PhotoImage(image)
        self.photo = test
        label = Label(image=test)
        label.place(relx=0.5, rely=0.25, anchor=customtkinter.CENTER)

        button1.place(relx=0.15, rely=0.5, anchor=customtkinter.CENTER)
        button2.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)
        button3.place(relx=0.85, rely=0.5, anchor=customtkinter.CENTER)

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
newpage = NewPage(app)
app.mainloop()