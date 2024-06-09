import vlc
from random import randint
import platform


#function that changes the frame (page) of the application
def change_frame(old_frame,new_frame):
    #remove old frame from grid and add new frame
    
    old_frame.grid_forget()
    new_frame.grid(row=0, column=0, sticky="nsew")

def play_video_standaard(frame):
    player = vlc.Instance()
    
    # selecting the video to play
    video = randint(1,7)
    media = player.media_new(f"./Videos/{video}.mp4") 
    
    # creating a media player object
    media_player = player.media_player_new()

    #connecting the media player object to the frame (conditional logic for ease of use on different platforms)
    if platform.system() == 'Windows':
        media_player.set_hwnd(frame.winfo_id())
    else:
        media_player.set_xwindow(frame.winfo_id())

    #set the video to the media player
    media_player.set_media(media) 
    
    # start playing video 
    media_player.play() 

def play_video_rollator(frame):
    player = vlc.Instance()
    
    # selecting the video to play
    video = randint(1,7)
    media = player.media_new(f"./Videos/{video}.mp4") 
    
    # creating a media player object
    media_player = player.media_player_new()

    #connecting the media player object to the frame (conditional logic for ease of use on different platforms)
    if platform.system() == 'Windows':
        media_player.set_hwnd(frame.winfo_id())
    else:
        media_player.set_xwindow(frame.winfo_id())

    #set the video to the media player
    media_player.set_media(media) 
    
    # start playing video 
    media_player.play() 

def play_video_rolstoel(frame):
    player = vlc.Instance()
    
    # selecting the video to play
    video = randint(1,7)
    media = player.media_new(f"./Videos/{video}.mp4") 
    
    # creating a media player object
    media_player = player.media_player_new()

    #connecting the media player object to the frame (conditional logic for ease of use on different platforms)
    if platform.system() == 'Windows':
        media_player.set_hwnd(frame.winfo_id())
    else:
        media_player.set_xwindow(frame.winfo_id())

    #set the video to the media player
    media_player.set_media(media) 
    
    # start playing video 
    media_player.play() 