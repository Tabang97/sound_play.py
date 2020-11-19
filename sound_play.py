from tkinter import *
import pygame
import os
from tkinter import filedialog
root = Tk()
root.title("mp3")
root.geometry("500x300")
pygame.mixer.init()

#adding song funtion
def add_songs():
    song = filedialog.askopenfilename(initialdir='audio/', title="choose a song", filetypes=(("wav Files", "*wav"),))

    song = song.replace("/home/user/PycharmProjects/play_sound.py/audio/", "")
    song = song.replace(".wav", "")

#add song
    song_box.insert(END, song)

#add many songs
def add_many_songs():
        song = filedialog.askopenfilenames(initialdir='audio/', title="choose a song", filetypes=(("wav Files", "*wav"),))
#looping and replace
        for song in song:
            song = song.replace("/home/user/PycharmProjects/play_sound.py/audio/", "")
            song = song.replace(".wav", "")

            song_box.insert(END, song)



#play function
def play():
    song = song_box.get(ACTIVE)
    song = f'/home/user/PycharmProjects/play_sound.py/audio/{song}.wav'

    pygame.mixer.music.load(song)
    pygame.mixer.music.play(add_many_songs)

    pygame.mixer.init()
    pygame.mixer.music.play(-1)
#stop function
def stop():
    pygame.mixer.music.stop()
    song_box.selection_clear(ACTIVE)

#global pause variable
global paused
paused = False

#pause function
def pause(is_paused):
    global paused
    paused = is_paused

    if paused:
        pygame.mixer.music.unpause()
        paused = False
    else:
        pygame.mixer.music.pause()
        paused = True

#prev function
def prev():
    next_song = song_box.curselection()
    next_song = next_song[0]-1
    song = song_box.get(next_song)

    song = f'/home/user/PycharmProjects/play_sound.py/audio/{song}.wav'

    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)

#active bar & clearing
    song_box.selection_clear(0, END)
    song_box.activate(next_song)
#show bar
    song_box.selection_set(next_song, last=None)

#next function
def next():
    next_song = song_box.curselection()
    next_song = next_song[0]+1
    song = song_box.get(next_song)

    song = f'/home/user/PycharmProjects/play_sound.py/audio/{song}.wav'

    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)

#active bar & clearing
    song_box.selection_clear(0, END)
    song_box.activate(next_song)
#show bar
    song_box.selection_set(next_song, last=None)

#playlist box
song_box = Listbox(root, bg="black", fg="green", width=60, selectbackground="gray", selectforeground="black")
song_box.pack(pady=20)

#menu
my_menu = Menu(root)
root.config(menu=my_menu)

#adding songs
add_songs_menu = Menu(my_menu)
my_menu.add_cascade(label="Add Songs", menu=add_songs_menu )
add_songs_menu.add_command(label="Add one song to playlist", command=add_songs)

add_songs_menu.add_command(label="Add many songs to playlist", command=add_many_songs)


#control frame
contrl_frame = Frame(root)
contrl_frame.pack()

#buttons
prev_btn = Button(contrl_frame, text="prev", borderwidth=0, padx=10, command=prev)
prev_btn.grid(row=0, column=0)

play_btn = Button(contrl_frame, text="play", borderwidth=0, padx=10, command=play)
play_btn.grid(row=0, column=1)

pause_btn = Button(contrl_frame, text="pause", borderwidth=0, padx=10, command=lambda: pause(paused))
pause_btn.grid(row=0, column=2)

stop_btn = Button(contrl_frame, text="stop", borderwidth=0, padx=10, command=stop)
stop_btn.grid(row=0, column=3)

next_btn = Button(contrl_frame, text="next", borderwidth=0, padx=10, command=next)
next_btn.grid(row=0, column=4)


root.mainloop()
