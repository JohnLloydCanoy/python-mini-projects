import numpy as np
import tkinter as tk
rgb = np.random.randint(0, 256, size=(1, 3))

print(f"Random RGB Colors:{rgb}")

# identfiying the color it generate based on the rgb values
red, green, blue = rgb[0]
if red > green and red > blue:
    color = "Red"
elif green > red and green > blue:
    color = "Green"
elif blue > red and blue > green:
    color = "Blue"
else:
    color = "Unknown"

print(f"The generated color is: {color}")

# it will post the GUI window with the color
root = tk.Tk()
root.title("Color Generator")
root.geometry("300x200")
color_hex = f'#{red:02x}{green:02x}{blue:02x}'
frame = tk.Frame(root, bg=color_hex)
frame.pack(expand=True, fill=tk.BOTH)
root.mainloop()
