from tkinter import *
from PIL import Image, ImageTk

from src.Game import opponent_played


def show_selected():
    opp_played = opponent_played()
    win_label.config(text = "Opponent played: " + opp_played)
    print("Selected option:", selected_option.get())
    print("Opponent Played:", opp_played)

root = Tk()
root.geometry("500x500")
root.title("Rock Paper Scissors")

frame = Frame(root)
frame.pack(fill="both", expand=0)

label = Label(frame)
label.pack(fill = X,expand = 1)
# Load an image (must be .png, .gif, or .ppm)
rock_image = PhotoImage(file="../images/rock.png")

image_files = ["../images/rock.png","../images/paper.png", "../images/scissors.png"]
# List of options
options = ["Rock", "Paper", "Scissors"]
# List to store resized image objects
images = []

# Resize images using Pillow and store them
for image_file in image_files:
    # Open the image using PIL
    image = Image.open(image_file)

    # Resize the image (e.g., resize to 100x100)
    image = image.resize((100, 100))

    # Convert the PIL image to a PhotoImage object for tkinter
    image_tk = ImageTk.PhotoImage(image)

    # Append the resized image to the images list
    images.append(image_tk)

# Create a variable to store the selected option (default to first option)
selected_option = StringVar()
selected_option.set(options[0])  # Set default image

# Create a set of Radiobuttons
for i, image in enumerate(images):
    Radiobutton(frame, image = image, variable=selected_option, value=options[i]).pack(anchor=W)


button = Button(label, text="Play", font = 20, command=show_selected, width = 10, height = 3)
button.pack(anchor = "center")

win_label = Label(frame, text = "Opponent played: none", font = 20)
win_label.pack(anchor = 'e')



root.mainloop()
