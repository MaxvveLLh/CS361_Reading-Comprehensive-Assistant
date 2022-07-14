import tkinter as tk
from tkinter import filedialog, Text
from PIL import ImageTk, Image
import os
import time

root = tk.Tk()

canvas = tk.Canvas(root, height = 800, width = 1600, bg = "#263d42")
canvas.pack()

def Take_input():
    #have to set img to global, so that the img variable can be passed out of the scope of the function
    global img
    INPUT = inputtxt.get("1.0", "end-1c") #take input content
    print(INPUT)
    commfile = open("textcomm.txt", "w")
    commfile.write(INPUT) #write content into communication file
    commfile.close()

    time.sleep(2)
    commfile = open("image-service.txt", "r")
    path = commfile.readline() #read returned generated graph path
    commfile.close()
    
    img = ImageTk.PhotoImage(Image.open(path)) #assign the graph
    panel.config(image=img) #update the graph
    #panel.image = img2
    print(path)
    #canvas.itemconfig(image_container, image=img)

#input box    
lable_input = tk.Label(text = "Paste the content here")
inputtxt = Text(root, height = 10,
                width = 25,
                bg = "light yellow")
#graph box label
lable_graph = tk.Label(text = "Transformed graph")

#transform button
tranfrom_button = tk.Button(root, height = 2,
                 width = 15,
                 text ="Transform",
                 
                 command = Take_input)

#input area
inputtxt.pack()
inputtxt.place(relwidth = 0.4, relheight = 0.8, relx = 0.05, rely = 0.1)
#input area lable
lable_input.pack()
lable_input.place(relwidth = 0.1, relheight = 0.05, relx = 0.2, rely = 0.9)
#button
tranfrom_button.pack()
tranfrom_button.place(relx = 0.458, rely = 0.45)
#panel
img = ImageTk.PhotoImage(Image.open("images/5.jpg"))
panel = tk.Label(root, image=img)
panel.pack()
panel.place(relwidth = 0.4, relheight = 0.8, relx = 0.55, rely = 0.1)
#graph's lable
lable_graph.pack()
lable_graph.place(relwidth = 0.1, relheight = 0.05, relx = 0.7, rely = 0.9)

root.mainloop()
