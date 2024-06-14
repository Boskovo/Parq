import vlc
from random import randint
import platform
import time
from threading import Thread, Event

# define event that is used to detect the end of the Thread
stop_event = Event()

# define which videos belong to what type
standaard_videos = 7
rollator_videos = 6
rolstoel_videos = randint(1,5)

#function that changes the frame (page) of the application
def show_frame(app, page_name, video_type):

    show_frame.app = app

    # display the page
    frame = app.frames[page_name]
    frame.tkraise()
    
    if page_name == "VideoPage":
        play_video(frame, video_type)

def play_video(frame,video_type):

    #clean up the stop event
    stop_event.clear()

    # define vlc player instance
    player = vlc.Instance()
    play_video.player = player

    # selecting the video to play

    if video_type == 1:
        video = standaard_videos
    if video_type == 2:
        video = rollator_videos
    if video_type == 3:
        video = rolstoel_videos

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

    # start Thread that detects when the end_reached function is called
    Thread(target=detect_reset, args=(media_player,),daemon=True).start()

# set the stop event when the end of the video is reached
def end_reached(event):
    stop_event.set()

#detect when to reset the app
def detect_reset(object):

    #get app and vlc instance
    app = show_frame.app
    player = play_video.player

    #check if stop_event is set
    while not stop_event.is_set():
        time.sleep(0.2)

    #stop and release the media_player
    object.stop()
    object.release()

    #release the vlc instance
    player.release()

    #go back to main page
    show_frame(app, "MainPage")
