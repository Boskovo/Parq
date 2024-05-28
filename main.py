from tkinter import *
import customtkinter
from gui_functions import *
from PIL import ImageTk, Image

# gui scale for widgets
customtkinter.set_widget_scaling(1.8)

# Main page
class MainPage(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.configure(fg_color='white')

        # add widgets here
        button1 = customtkinter.CTkButton(master=self, 
        text="button1", 
        fg_color='#006633',
        hover_color='#00592C', 
        command=lambda: change_frame(self, newpage))

        button2 = customtkinter.CTkButton(master=self, text="button2", fg_color='#006633', hover_color='#00592C')
        button3 = customtkinter.CTkButton(master=self, text="button3", fg_color='#006633', hover_color='#00592C')

        canvas = Canvas(self, width=945, height=242, bg='white', highlightthickness=0)
        canvas.pack()

        mainlogo = Image.open("./images/walkintheparq-logo.png")
        mainlogo = mainlogo.resize((945, 242))
        
        # Ensure image has alpha channel
        mainlogo = mainlogo.convert("RGBA")

        test = ImageTk.PhotoImage(mainlogo)

        canvas.create_image(0, 0, anchor=NW, image=test)
        canvas.image = test

        button1.place(relx=0.15, rely=0.5, anchor=customtkinter.CENTER)
        button2.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)
        button3.place(relx=0.85, rely=0.5, anchor=customtkinter.CENTER)
        canvas.place(relx=0.5, rely=0.25, anchor=customtkinter.CENTER)

        self.centerphoto = test

# Currently an empty second page
class NewPage(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # add widgets here

# The app itself
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
