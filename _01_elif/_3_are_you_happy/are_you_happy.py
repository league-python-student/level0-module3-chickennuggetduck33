from tkinter import Tk, simpledialog, messagebox
import webbrowser
def play_video(url):
    webbrowser.open(url)
if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    # TODO: Look at the AreYouHappy.png image
    #       Use pop-ups to recreate the chart using if and elif statements
    q1 = simpledialog.askstring(title="therapy", prompt="are you happy")
    if q1 == "no":
        q2 = simpledialog.askstring(title="therapy", prompt="do you want to be happy?")
    elif q1 == "yes":
        la1 = messagebox.showinfo(message="Keep doing whatever you are doing.")
    if q2 == "no":
        la1 = messagebox.showinfo(message="Keep doing whatever you are doing.")
        play_video('https://www.youtube.com/watch?v=l60MnDJklnM')
    elif q2 == "yes":
        la2 = messagebox.showinfo(message="Change something.")

    pass
