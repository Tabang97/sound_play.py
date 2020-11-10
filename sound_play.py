from tkinter import*
import pygame
from tkinter import filedialog

window = Tk()
window.title("Soundplay")
window.geometry("400x400")

pygame.mixer.init()

#add song function
def add_song():
    song = filedialog.askopenfilename(initialdir='audio/', title="choose a song", filetypes=(("mp3 files", "*.mp3"), ))
    song = song.replace("C:gui/audio/","")
    song = song.replace(".mp3", "")
    screen.insert(END, song)

#play song function
def play():
    song = screen.get(ACTIVE)
    song = f'C:/gui/audio/{song}.mp3'
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)

#stop song function
def stop():
    pygame.mixer.music.stop()
    screen.selection_clear(ACTIVE)

global paused
paused = FALSE
#pause song
def pause(is_paused):
    global paused
    paused = is_paused

    if paused:
        pygame.mixer.music.unpause()
        paused = FALSE
    else:
        pygame.mixer.music.pause()
        paused = True


#create box
screen = Listbox(window, bg="black", fg="green", width=60, selectbackground="gold")
screen.pack(pady=20)


#buttons
back_btn = Button(window, text="Back", bg="red")
back_btn.pack()

next_btn = Button(window, text="next",)
next_btn.pack()

play_btn = Button(window, text="play", command=play)
play_btn.pack()

pause_btn = Button(window, text="pause", command=lambda: pause(paused))
pause_btn.pack()

stop_btn = Button(window, text="stop", command=stop)
stop_btn.pack()

#create menu
my_menu = Menu(window)
window.config(menu=my_menu)

#add song menu
add_song_menu = Menu(my_menu)
my_menu.add_cascade(label="add songs", menu=add_song_menu)
add_song_menu.add_cascade(label="Add one song to playlist", command=add_song)




#function play
def play():
    pygame.mixer.music.load("Lil Wayne - 6 Foot 7 Foot ft. Cory Gunz (Explicit) (Official Music Video).mp3")
    pygame.mixer.music.play()

#function stop
def stop():
    pygame.mixer.music.stop()



window.mainloop()


from playsound import playsound
playsound("Lil Wayne - 6 Foot 7 Foot ft. Cory Gunz (Explicit) (Official Music Video).mp3")
