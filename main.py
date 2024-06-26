from tkinter import *
import customtkinter
from gui_functions import *
from PIL import ImageTk, Image

# GUI scale for widgets
customtkinter.set_widget_scaling(1.8)

# Main page
class MainPage(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        bg_color = 'white'
        self.configure(fg_color=bg_color)
        self._corner_radius = 0
        
        # Add widgets here
        
        # Laad de afbeelding
        lopend_image = Image.open("./images/lopend.png")
        lopend_image = lopend_image.resize((200, 200))  # Pas de grootte aan indien nodig
        lopend_photo = ImageTk.PhotoImage(lopend_image)

        rollator_image = Image.open("./images/rollator.png")
        rollator_image = rollator_image.resize((200, 200))  # Pas de grootte aan indien nodig
        rollator_photo = ImageTk.PhotoImage(rollator_image)

        rolstoel_image = Image.open("./images/rolstoel.png")
        rolstoel_image = rolstoel_image.resize((200, 200))  # Pas de grootte aan indien nodig
        rolstoel_photo = ImageTk.PhotoImage(rolstoel_image)

        # Voeg de afbeelding toe aan de knop
        button1 = customtkinter.CTkButton(master=self, 
        text="Lopend",
        height=120,
        width=115,
        fg_color='#016634',
        hover_color='#00592C',
        corner_radius=5,
        image=lopend_photo,  # Voeg de afbeelding toe
        compound="top",  # Positie van de tekst ten opzichte van de afbeelding
        command=lambda: show_frame(master,"VideoPage", 1))

        button1.image = lopend_photo  # Houd een referentie naar de afbeelding

        button2 = customtkinter.CTkButton(master=self, 
        text="Met een Rollator", 
        height=120,
        width=115,
        fg_color='#016634',
        hover_color='#00592C',
        corner_radius=5,
        image=rollator_photo,  # Voeg de afbeelding toe
        compound="top",  # Positie van de tekst ten opzichte van de afbeelding
        command=lambda: show_frame(master,"VideoPage", 2))

        button1.image = rollator_photo  # Houd een referentie naar de afbeelding

        button3 = customtkinter.CTkButton(master=self, 
        text="Met een Rolstoel",
        height=120,
        width=115,
        fg_color='#016634', 
        hover_color='#00592C',
        corner_radius=5, 
        image=rolstoel_photo,  # Voeg de afbeelding toe
        compound="top",  # Positie van de tekst ten opzichte van de afbeelding
        command=lambda: show_frame(master,"VideoPage", 3))

        button1.image = rolstoel_photo  # Houd een referentie naar de afbeelding


        canvas = Canvas(self, width=945, height=242, bg=bg_color, highlightthickness=0)
        canvas.pack()
        mainlogo = Image.open("./images/walkintheparq-logo.png")
        mainlogo = mainlogo.resize((700, 179))
    
        # Ensure image has alpha channel
        mainlogo = mainlogo.convert("RGBA")
        logo = ImageTk.PhotoImage(mainlogo)
        canvas.create_image(120, 0, anchor=NW, image=logo)
        canvas.image = logo

        # Tekstlabel "Hoe verplaatst u zich?" toevoegen
        question_label = customtkinter.CTkLabel(master=self, text="Hoe verplaatst u zich?", fg_color=bg_color, text_color="#626262", font=("Roboto", 17))
        question_label.pack(pady=(85, 20))  # Pas de padding aan om de positie te verfijnen

        button1.place(relx=0.15, rely=0.7, anchor=customtkinter.CENTER)
        button2.place(relx=0.5, rely=0.7, anchor=customtkinter.CENTER)
        button3.place(relx=0.85, rely=0.7, anchor=customtkinter.CENTER)
        canvas.place(relx=0.5, rely=0.25, anchor=customtkinter.CENTER)

        # Bring buttons to the front
        button1.lift()
        button2.lift()
        button3.lift()

        self.centerphoto = logo

# Currently an empty second page
class VideoPage(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        bg_color = 'white'
        self.configure(fg_color=bg_color)

        # Add widgets here
        # Create a new frame for the video
        self.video_frame = customtkinter.CTkFrame(self)
        self.video_frame.configure(fg_color=bg_color)
        self.video_frame.pack(side=customtkinter.TOP, fill=customtkinter.BOTH, expand=True)

        # Create a new frame for the buttons
        button_frame = customtkinter.CTkFrame(self)
        button_frame.configure(fg_color=bg_color)
        button_frame.pack(side=customtkinter.BOTTOM, fill=customtkinter.X)

        # Create pause and play buttons
        pause_button = customtkinter.CTkButton(
            button_frame, 
            text="Pauze",
            height=35,
            width=110, 
            fg_color='#016634', 
            hover_color='#00592C',
            command=lambda: pause_or_play_video(pause_button))

        back_button = customtkinter.CTkButton(
            button_frame, 
            text="Terug",
            height=35,
            width=110, 
            fg_color='#016634', 
            hover_color='#00592C',
            command=stop_and_reset)

        back_button.place(relx=0.05, rely=0.75, anchor=customtkinter.SW)
        pause_button.place(relx=0.95, rely=0.75, anchor=customtkinter.SE)
        
# The app itself
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Walk In The ParQ")

        # configure screen size & set key to toggle off fullscreen
        self.geometry("800x480")
        self.bind("<Escape>", lambda event: self.attributes("-fullscreen", False)) #press escape to quit fullscreen
        self.bind("f", lambda event: self.attributes("-fullscreen", True))

        # Configure grid system
        self.grid_rowconfigure(0, weight=1)  
        self.grid_columnconfigure(0, weight=1)

        # Initiate Page of the app itself
        self.frames = {}
        for f in (MainPage, VideoPage):
            page_name = f.__name__
            frame = f(master=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        
        #set app to fullscreen after a second to ensure it works on the pi
        self.after(1000,lambda: self.attributes("-fullscreen",True))
        
        show_frame(self, "MainPage", 0)
        
app = App()
main = MainPage(app)

app.mainloop()