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

        bg_color = 'white'
        self.configure(fg_color=bg_color)
        self._corner_radius = 0

        # add widgets here
        button1 = customtkinter.CTkButton(master=self, 
        text="Standaard",
        height=120,
        width=115,
        fg_color='#016634',
        hover_color='#00592C',
        corner_radius=5,
        command=lambda: [change_frame(self,page1), play_video(page1, 1)])

        button2 = customtkinter.CTkButton(master=self, 
        text="Rollator", 
        height=120,
        width=115,
        fg_color='#016634',
        hover_color='#00592C',
        corner_radius=5,
        command=lambda: [change_frame(self,page2), play_video(page2, 2)])

        button3 = customtkinter.CTkButton(master=self, 
        text="Rolstoel",
        height=120,
        width=115,
        fg_color='#016634', 
        hover_color='#00592C',
        corner_radius=5, 
        command=lambda: [change_frame(self,page3), play_video(page3, 3)])

        canvas = Canvas(self, width=945, height=242, bg=bg_color, highlightthickness=0)
        canvas.pack()

        mainlogo = Image.open("./images/walkintheparq-logo.png")
        mainlogo = mainlogo.resize((945, 242))
        
        # Ensure image has alpha channel
        mainlogo = mainlogo.convert("RGBA")

        logo = ImageTk.PhotoImage(mainlogo)

        canvas.create_image(0, 0, anchor=NW, image=logo)
        canvas.image = logo
        
        button1.place(relx=0.15, rely=0.7, anchor=customtkinter.CENTER)
        button2.place(relx=0.5, rely=0.7, anchor=customtkinter.CENTER)
        button3.place(relx=0.85, rely=0.7, anchor=customtkinter.CENTER)
        canvas.place(relx=0.5, rely=0.25, anchor=customtkinter.CENTER)


        self.centerphoto = logo

# Currently an empty second page
class NewPage(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        
        # add widgets here

# Currently an empty page for 'Standaard'
class Page1(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # add widgets here

# Currently an empty page for 'Rollator'
class Page2(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # add widgets here

# Currently an empty page for 'Rolstoel'
class Page3(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # add widgets here

        
# The app itself
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Walk In The ParQ")

        # configure screen size & set key to turn off fullscreen
        self.geometry("800x480")
        self.attributes("-fullscreen", True)
        self.state('zoomed')
        self.bind("<Escape>", lambda event: self.attributes("-fullscreen", False)) #press escape to quit fullscreen

        # configure grid system
        self.grid_rowconfigure(0, weight=1)  
        self.grid_columnconfigure(0, weight=1)

        # initiate pages of the app itself
        self.my_frame = MainPage(master=self)
        self.my_frame.grid(row=0, column=0, sticky="nsew")
        
app = App()
main = MainPage(app)
page1 = Page1(app)
page2 = Page2(app)
page3 = Page3(app)

app.mainloop()

