import vlc
from random import randint
import platform

#function that changes the frame (page) of the application
def change_frame(old_frame,new_frame):

    #define the frames as variables for use by other functions
    change_frame.old_frame = old_frame
    change_frame.new_frame = new_frame

    #remove old frame from grid and add new frame
    old_frame.grid_forget()
    new_frame.grid(row=0, column=0, sticky="nsew")

    play_video(new_frame)

def play_video(frame):
    player = vlc.Instance()
    
    # selecting the video to play
    video = randint(1,7)
    media = player.media_new(f"./Videos/{video}.mp4") 
    
    # creating a media player object
    media_player = player.media_player_new()

    play_video.media_player = media_player

    #connecting the media player object to the frame (conditional logic for ease of use on different platforms)
    if platform.system() == 'Windows':
        media_player.set_hwnd(frame.winfo_id())
    else:
        media_player.set_xwindow(frame.winfo_id())

    #set the video to the media player
    media_player.set_media(media) 

    #define the manager for the media player
    manager = media_player.event_manager()

    # start playing video 
    media_player.play()

    #detect an EndReached event and call the end_reached function
    manager.event_attach(vlc.EventType.MediaPlayerEndReached, end_reached)

def end_reached(event):

    media_player = play_video.media_player

    #media_player.stop()
    #media_player.get_media().release()
    #media_player.release()
    #media_player.get_instance.release()

    change_frame.new_frame.grid_forget()
    change_frame.old_frame.grid(row=0, column=0, sticky="nsew")
    
    print('end reached')
