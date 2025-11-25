import tkinter as tk
import random
import time

messages = [
    "YOUR LIFE WILL BE RUINED!",
    "HAHAHAHAHHAHAHAHAHAHA!",
    "YOUR COMPUTER HAS BEEN HACKED!",
    "BOMB PLANTED!"
]

print("DRAG ME BETWEEN OTHER WINDOW TO STOP | USE CTRL+C | WAITING 3 SECONDS...")
time.sleep(3)
print("RUNNING...")
# create main hidden root FIRST
root = tk.Tk() 
root.withdraw()

# get screen size AFTER root exists
screen_w = root.winfo_screenwidth()
screen_h = root.winfo_screenheight()

def spawn_popups():
    for _ in range(25):  # number of windows per burst
        win = tk.Toplevel()
        win.title("VIRUS ALERT, HAHAHAHAHHAHAHAH!")

        # random position anywhere on screen
        x = random.randint(0, screen_w - 250)
        y = random.randint(0, screen_h - 100)

        win.configure(bg="red")
        win.geometry(f"800x600+{x}+{y}")

        label = tk.Label(
            win,
            text=random.choice(messages),
            font=("Arial", 26, "bold"),
            bg="white",
            fg="red"
        )
        label.pack(expand=True)
        win.after(2000, win.destroy)  # auto-close after 10 seconds


try:
    while True:
        spawn_popups()
        root.update()  
        time.sleep(0.5)  # delay between bursts

except KeyboardInterrupt:
    print("\nStopped! (CTRL+C pressed)")
    root.destroy()

