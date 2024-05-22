
def change_frame(old_frame,new_frame):
    old_frame.grid_forget()
    new_frame.grid(row=0, column=0, sticky="nsew")