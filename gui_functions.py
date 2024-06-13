import vlc
from random import randint
import platform


standaard_videos = 7
rollator_videos = 6
rolstoel_videos = randint(1,5)


#function that changes the frame (page) of the application
def change_frame(old_frame,new_frame):
    #remove old frame from grid and add new frame
    
    old_frame.grid_forget()
    new_frame.grid(row=0, column=0, sticky="nsew")

def play_video(frame, pagenumber):
    player = vlc.Instance()
    
    # selecting the video to play
    if pagenumber == 1:
        video = standaard_videos
    if pagenumber == 2:
        video = rollator_videos
    if pagenumber == 3:
        video = rolstoel_videos
    
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