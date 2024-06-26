import vlc
from random import choice
import platform
import time
from threading import Thread, Event

# Define event that is used to detect the end of the Thread
stop_event = Event()

# Define which videos belong to what type
standaard_videos = [7, 10, 11, 13]
rollator_videos = [6, 8, 9, 12]
rolstoel_videos = [1, 2, 3, 4, 5]

# Function that changes the frame (page) of the application
def show_frame(app, page_name, video_type):
    show_frame.app = app

    # Display the page
    frame = app.frames[page_name]
    frame.tkraise()
    
    if page_name == "VideoPage":
        play_video(frame, video_type)

def play_video(frame, video_type):
    # Clean up the stop event
    stop_event.clear()

    # Define VLC player instance
    player = vlc.Instance('--no-xlib')  # Disable Xlib to avoid issues on RPi
    play_video.player = player

    # Selecting the video to play
    if video_type == 1:
        video = choice(standaard_videos)
    elif video_type == 2:
        video = choice(rollator_videos)
    elif video_type == 3:
        video = choice(rolstoel_videos)

    media = player.media_new(f"./Videos/{video}.mp4") 
    
    # Creating a media player object
    media_player = player.media_player_new()
    play_video.media_player = media_player

    # Ensure the video_frame is mapped before setting the window ID
    frame.video_frame.update_idletasks()

    # Connecting the media player object to the frame (conditional logic for ease of use on different platforms)
    if platform.system() == 'Windows':
        media_player.set_hwnd(frame.video_frame.winfo_id())
    else:
        media_player.set_xwindow(frame.video_frame.winfo_id())

    # Set the video to the media player
    media_player.set_media(media) 

    # Define the manager for the media player
    manager = media_player.event_manager()

    # Start playing video
    media_player.play()

    # Detect an EndReached event and call the end_reached function
    manager.event_attach(vlc.EventType.MediaPlayerEndReached, end_reached)

    # Start Thread that detects when the end_reached function is called
    Thread(target=detect_reset, args=(media_player,), daemon=True).start()

def pause_or_play_video(pause_button):
    media_player = play_video.media_player

    # Check if the video is currently playing
    if media_player.get_state() == vlc.State.Playing:
        # If the video is playing, pause it and change the button text to "Play"
        media_player.pause()
        pause_button.configure(text="Afspelen")
    else:
        # If the video is paused, play it and change the button text to "Pause"
        media_player.play()
        pause_button.configure(text="Pauze")

# Set the stop event when the end of the video is reached
def end_reached(event):
    stop_event.set()

# Detect when to reset the app
def detect_reset(media_player):
    # Get app and VLC instance
    app = show_frame.app
    player = play_video.player

    # Check if stop_event is set
    while not stop_event.is_set():
        time.sleep(0.2)

    # Stop and release the media player
    media_player.stop()
    media_player.release()

    # Release the VLC instance
    player.release()

    # Go back to main page
    show_frame(app, "MainPage", 0)

def stop_and_reset():
    # Set the stop event
    stop_event.set()
    