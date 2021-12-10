from tkinter import *
from PIL import ImageTk, Image
import os, os.path
 
 
def forward(img_no):
    global label
    global button_forward
    global button_back
    global button_exit
    label.grid_forget()
 
    label = Label(image=List_images[img_no-1])
 
    label.grid(row=1, column=0, columnspan=3)
    button_for = Button(root, text="forward",
                        command=lambda: forward(img_no+1))
 
    if img_no == 4:
        button_forward = Button(root, text="Forward",
                                state=DISABLED)

    button_back = Button(root, text="Back",
                         command=lambda: back(img_no-1))
 
    button_back.grid(row=5, column=0)
    button_exit.grid(row=5, column=1)
    button_for.grid(row=5, column=2)
 
 
def back(img_no):

    global label
    global button_forward
    global button_back
    global button_exit
    label.grid_forget()
 
    label = Label(image=List_images[img_no - 1])
    label.grid(row=1, column=0, columnspan=3)
    button_forward = Button(root, text="forward",
                            command=lambda: forward(img_no + 1))
    button_back = Button(root, text="Back",
                         command=lambda: back(img_no - 1))
    print(img_no)

    if img_no == 1:
        button_back = Button(root, Text="Back", state=DISABLED)
 
    label.grid(row=1, column=0, columnspan=3)
    button_back.grid(row=5, column=0)
    button_exit.grid(row=5, column=1)
    button_forward.grid(row=5, column=2)
 
root = Tk()
 
root.title("Image Viewer")
 
root.geometry("1000x900")

List_images = []
folder_names = os.listdir("./extracted_frames/video_frames/")
print(folder_names)

for array_size in range(len(folder_names)):
    position = globals()["image_no_%s" % array_size] = ImageTk.PhotoImage(Image.open("./extracted_frames/video_frames/"+folder_names[array_size]))
    List_images.append(position)


 
label = Label(image=List_images[0])
label.grid(row=1, column=0, columnspan=3)
button_back = Button(root, text="Back", command=back,
                     state=DISABLED)
button_exit = Button(root, text="Exit",
                     command=root.quit)
button_forward = Button(root, text="Forward",
                        command=lambda: forward(1))
button_back.grid(row=5, column=0)
button_exit.grid(row=5, column=1)
button_forward.grid(row=5, column=2)
 
root.mainloop()