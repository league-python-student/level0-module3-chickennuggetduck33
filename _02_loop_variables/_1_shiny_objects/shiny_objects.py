from tkinter import simpledialog, Tk
from playsound import playsound

can_play_sounds = False
import webbrowser

def play_mister_zee():
    if can_play_sounds:
        playsound('shiny-objects.wav')
    else:
        print("Mister Zee requires shiny objects")


def many_shiny_objects():
    # TODO 1) Call the method above to play Mister Zee
    play_mister_zee()
    # TODO 2) Ask the user how many shiny objects they want
    n = simpledialog.askinteger(None, prompt="How many shiny objects do you want?")
    # TODO 3) Play the sound that many times
    for i in range(n):
        play_mister_zee()
    if n == 24:
        webbrowser.open('https://www.youtube.com/watch?v=nX6N2tgLmaQ')
    pass


if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    many_shiny_objects()
