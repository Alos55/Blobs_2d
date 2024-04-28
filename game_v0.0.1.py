import tkinter as tk
import random
import keyboard
from PIL import ImageTk , Image


game = tk.Tk()

# Open the text file in read mode
with open('cordinate.txt', 'r') as file:
    x = []
    y = []
    z = []
    line_number = 1
    for line in file:
        x_start = line.find('x')
        y_start = line.find('y')
        z_start = line.find('z')
        e_start = line.find('e')
        if x_start != -1 and y_start != -1 and z_start != -1 and e_start != -1:
            # Extract the content between 'x' and 'y'
            x_content = line[x_start + 1:y_start]
            x.append(x_content)
            # Extract the content between 'y' and 'z'
            y_content = line[y_start + 1:z_start]
            y.append(y_content)
            # Extract the content between 'z' and 'e'
            z_content = line[z_start + 1:e_start]
            z.append(z_content)
            line_number += 1

#who invented python like whhyyyyyyyyy7yyyyyyyyyyyyyyyyyyyyyyyy
#i cant automate the block placement lol
idk = 0
idk = 0
name = ""
img = 0
stone1 = Image.open("stone.png")
stone2 = stone1.resize((30,30))
stone = ImageTk.PhotoImage(stone2)

water1 = Image.open("water.png")
water2 = water1.resize((30,30))
water = ImageTk.PhotoImage(water2)
 

 

 

 








def place(xsuffer , yhelp, ps):
    print(ps)
    if ps == 1:
        img = stone
    if ps == 2:
        img = water
    name = str(object= xsuffer) + str(object = yhelp)
    name = tk.Button(image = img, relief= "flat")
    name.grid(row= xsuffer ,column= yhelp,sticky="nsew")
try:
    while True:
        if int(z[idk]) == 1:
            place( int(x[idk]) , y[idk], 1)
            idk = idk + 1
            print("stone")
        if int(z[idk]) == 2:
            place( int(x[idk]), int(y[idk]), 2)
            idk = idk + 1
            print("water")

except:
    pass    

        
            
                








game.mainloop()