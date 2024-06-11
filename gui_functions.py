import vlc
from random import randint
import platform

#function that changes the frame (page) of the application
def show_frame(app,page_name):

    show_frame.app = app

    frame = app.frames[page_name]
    frame.tkraise()
    
    if page_name == "VideoPage":
        play_video(frame)

def play_video(frame):

    player = vlc.Instance()
    play_video.player = player

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
    app = show_frame.app
    media_player = play_video.media_player
    player = play_video.player

    print('executing end reached function')
    try:
        media_player.stop()
    except Exception as e:
        print("error stopping media player", e)

    try:
        media_player.release()
    except Exception as e:
        print("error releasing media player", e)

    try:
        player.release()
    except Exception as e:
        print("error releasing vlc instance", e)

    app.update()
    app.update_idletasks()

    show_frame(app, "MainPage")

    print('end reached')
