import tkinter as tk
from PIL import Image, ImageTk
import winsound
import threading

# Create fullscreen window
root = tk.Tk()
root.attributes("-fullscreen", True)
root.configure(bg="black")
root.title("CS2 External Loader")

# Load trollface image (must be trollface.png in same folder)
img = Image.open("trollface.png")
img = img.resize((600, 600))
photo = ImageTk.PhotoImage(img)

# Display trollface
label = tk.Label(root, image=photo, bg="black")
label.pack(expand=True)

# Display message
text = tk.Label(
    root,
    text="There is no such thing as free CS2 cheats.\nYou've been trolled 😈",
    font=("Consolas", 40, "bold"),
    fg="white",
    bg="black"
)
text.pack()

# Play sound in background
def play_sound():
    winsound.PlaySound("trolled.wav", winsound.SND_FILENAME)

threading.Thread(target=play_sound, daemon=True).start()

# Press ESC to close
root.bind("<Escape>", lambda e: root.destroy())

root.mainloop()





