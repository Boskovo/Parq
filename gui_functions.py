import vlc
from random import randint
import platform
import time
from threading import Thread

#function that changes the frame (page) of the application
def show_frame(app,page_name):

    show_frame.app = app

    frame = app.frames[page_name]
    frame.tkraise()
    
    if page_name == "VideoPage":
        play_video(frame)

def play_video(frame):

    # define vlc player instance
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

    Thread(target=detect_reset, args=(media_player,),daemon=True).start()

    # start playing video
    media_player.play()

    #detect an EndReached event and call the end_reached function
    manager.event_attach(vlc.EventType.MediaPlayerEndReached, end_reached)

vidOver = False
def end_reached(event):
    global vidOver
    vidOver = True

def detect_reset(object):
    global vidOver
    app = show_frame.app
    player = play_video.player

    vidOver = False

    while 1:
        if vidOver is True:
            vidOver = False

            object.stop()
            object.release()
            player.release()

            show_frame(app, "MainPage")
            print('reached the end')

        print('checking')
        time.sleep(0.2)
