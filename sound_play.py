from tkinter import *
import pygame
from tkinter import filedialog
root = Tk()
root.title("mp3")
root.geometry("500x300")

#playlist box
song_box = Listbox(root, bg="black", fg="green", width=60)
song_box.pack(pady=20)

#adding song funtion
def add_songs():
    song = filedialog.askopenfilename(initialdir='audio/', title="choose a song", filetypes=(("mp3 Files", "*mp3"),))
    print(song)
#control frame
contrl_frame = Frame(root)
contrl_frame.pack()

#buttons
prev_btn = Button(contrl_frame, text="prev", borderwidth=0, padx=10)
prev_btn.grid(row=0, column=0)

play_btn = Button(contrl_frame, text="play", borderwidth=0, padx=10)
play_btn.grid(row=0, column=1)

pause_btn = Button(contrl_frame, text="pause", borderwidth=0, padx=10)
pause_btn.grid(row=0, column=2)

stop_btn = Button(contrl_frame, text="stop", borderwidth=0, padx=10)
stop_btn.grid(row=0, column=3)

next_btn = Button(contrl_frame, text="next", borderwidth=0, padx=10)
next_btn.grid(row=0, column=4)

#menu
my_menu = Menu(root)
root.config(menu=my_menu)

#adding songs
add_songs_menu = Menu(my_menu)
my_menu.add_cascade(label="Add Songs",menu=add_songs_menu )
add_songs_menu.add_command(label="Add one song to playlist", command=add_songs)

root.mainloop()
