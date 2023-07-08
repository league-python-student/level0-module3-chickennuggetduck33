from tkinter import simpledialog, messagebox, Tk
import webbrowser


if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    n = 1
    messagebox.showinfo(message="You are an underwater explorer. You are leaving to explore the deepest oceans. You must find the lost city of Atlantis. This is your most challenging assignment. It is morning and the sun pushes up on the horizon. The sea is calm. You climb into the narrow pilot's compartment of the underwater vessel Seeker with your special gear. The crew of the research vessel Maray screws down the hatch clamps. Now begins the plunge into the depths of the ocean. The Seeker crew begins lowering by a strong, but thin cable. Within minutes, you are so deep in the ocean that little light filters down to you. The silence is eerie as the Seeker slips deeper and deeper. You peer out the thick glass porthole and see fish drifting past, sometimes stopping to look at you—an intruder from another world.Now the cable attaching you to Maray is extended almost to its limit. You have come to rest on a ledge near the canyon in the ocean floor that supposedly leads to the lost city of Atlantis. You have a special sea suit that will protect you from the intense pressure of the deep if you choose to walk about on the sea bottom. You can cut loose from the cable if you wish because the Seeker is self-propelled. You are now in another world.")
    while True:
        q1 = simpledialog.askinteger(None, prompt="If you decide to explore the ledge where the Seeker has come to rest, type 1. If you decide to cut loose from the Maray and dive with the Seeker into the canyon in the ocean floor, type 2.")
        if q1 == 1:
            messagebox.showinfo(message="Your sea suit will protect you from the intense pressures of the deep. It is a tight fit and takes you some time to put it on. Finally you slip from the airlock of the Seeker and stand on the ocean floor. It is a strange and marvelous world where your every move is slowed down. You begin to explore with your special hand-held searchlight. You examine the ledge by the canyon. Suddenly, a school of bright yellow angel fish dart by, almost brushing you. What made them move so fast? Are they being chased? Then you see it. The Seeker is in the grips of a huge sea monster. It is similar to a squid, but it is enormous. The Seeker is just a toy in its long, powerful tentacles. You seek shelter behind a rock formation. You know the spear gun you carry will be useless against this monster. It looks as though it will destroy the Seeker. Fish of all sizes huddle with you in an attempt to escape the monster.")
            webbrowser.open('https://external-preview.redd.it/CtCUffYJfJZqZzgSgFTUWqYARfz3o5nfd9c6NbzOP6Y.png?auto=webp&s=be06bfe1d47db73f178c33b945e0879695a24bb8')
            break
        elif q1 == 2:
            messagebox.showinfo(message="You radio a status report to the Moray and tell them that you are going to cast off from the line and descend under your own power. Your plan is approved and you cast off your line. Now you are on your own. The Seeker slips noiselessly into the undersea canyon. As you drop into the canyon, you turn on the Seeker's powerful searchlight. Straight ahead is a dark wall covered with a strange type of barnacle growth. To the left (port) side you see what appears to be a grotto. The entrance is perfectly round, as if it had been cut by human hands. Lantern fish give off a pale, greenish light. To the right (starboard) side of the Seeker you see bubbles rising steadily from the floor of the canyon.")
            webbrowser.open('https://external-preview.redd.it/CtCUffYJfJZqZzgSgFTUWqYARfz3o5nfd9c6NbzOP6Y.png?auto=webp&s=be06bfe1d47db73f178c33b945e0879695a24bb8')
            break
        else:
            messagebox.showinfo(message="Sorry, that was not an option please try again.")

# TODO Tell the user a story, but give them options so they can decide the
#  path of the plot.
#  Use pop-ups, if statements, and your imagination to make an interesting
#  story
