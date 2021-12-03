import time
import tkinter as tk
from tkinter import *


#############Code#####################################################
window = Tk()
window.title("Elevator Animation")
window.geometry("500x600")
window.configure(background="black")
Title = Label (window, text="Elevator", bg="black", fg="white", font="Arial 14 bold")
Title.pack()
canvas = Canvas(window, width=500, height=500)
canvas.pack()
elevator = canvas.create_rectangle(60, 500, 80, 440, fill="grey")
###########################All the boxes and lines##########################################

canvas.create_line(60,80,60,500, fill="black")
canvas.create_line(80,80,80,140, fill="black")
canvas.create_line(80,200,80,260, fill="black")
canvas.create_line(80,320,80,380, fill="black")
canvas.create_line(80,440,80,500,fill='black')
canvas.create_line(480,80,480,500, fill="black")
canvas.create_line(60,80,480,80)
canvas.create_line(60,140,480,140)
canvas.create_line(60,200,480,200)
canvas.create_line(60,260,480,260)
canvas.create_line(60,320,480,320)
canvas.create_line(60,380,480,380)
canvas.create_line(60,440,480,440)
canvas.create_line(60,500,480,500)
canvas.create_text(70, 470, fill="black", font="none 10 bold", text="G")
canvas.create_text(70, 350, fill="black", font="none 10 bold", text="1")
canvas.create_text(70, 230, fill="black", font="none 10 bold", text="2")
canvas.create_text(70, 110, fill="black", font="none 10 bold", text="3")

#################################################################################
CURRENT_FLOOR = 0
MOVING = 0
# the move function is passed the floor variable, it moves the elevator up and down
def move(floor):
    # get the global variable CURRENT_FLOOR for use inside the function
    global CURRENT_FLOOR
    global MOVING
    # if the elevator is not moving
    if MOVING == 0:
        # if the current floor (CURRENT_FLOOR) is less that the floor passed to the function(floor)
        if CURRENT_FLOOR < floor:
            #calculate the floor difference between current floor and the required foor
            floors_count = floor - CURRENT_FLOOR
            # set MOVING = 1 to indicate the elevator is moving
            MOVING = 1
            # loop for (12 X the number of floors) moving the elevator up
            for x in range(0, 12*floors_count):
                canvas.move(elevator,0, -10)   #to move any object in tkinter we use .move() function
                window.update()
                time.sleep(0.05)
            # set MOVING = 0 to indicate the elevator has stopped moving
            MOVING = 0
        elif CURRENT_FLOOR > floor:
            floors_count = CURRENT_FLOOR - floor
            # loop for (12 X the number of floors) moving the elevator down
            MOVING = 1
            for x in range(0, 12*floors_count):
                canvas.move(elevator, 0, 10)
                window.update()
                time.sleep(0.05)
            MOVING = 0
    CURRENT_FLOOR = floor
    
def UP():
    if CURRENT_FLOOR<3:
        move(CURRENT_FLOOR+1)
        
def DOWN():
    if CURRENT_FLOOR>0:
        move(CURRENT_FLOOR-1)

####################################################################################################################

#lambda - A lambda function can take any number of arguments, but can only have one expression.######

blank1 = Label (window, text="Buttons  ", bg="black", fg="white", font="none 12 bold")
blank1.pack(side=TOP)
new_floor = 0

while True:
    gf = Button (window, text="G", fg="green", activebackground="white", command=lambda: move(0))
    gf.place(x=132,y=560)
    floor1 = Button (window, text="1", bg="black", fg="green", activebackground="white", command=lambda: move(1))
    floor1.place(x=200,y=560)
    floor2 = Button (window, text="2", bg="black", fg="green", activebackground="white", command=lambda: move(2))
    floor2.place(x=260,y=560)
    floor3 = Button (window, text="3", bg="black", fg="green", activebackground="white", command=lambda: move(3))
    floor3.place(x=320,y=560)
    up=Button(window,bg="cyan",width=3,height=2,text="Up",command=lambda: UP())
    up.place(x=20,y=250)
    down=Button(window,bg="cyan",width=4,height=2,text="Down",command=lambda: DOWN())
    down.place(x=20,y=300)
    break
mainloop()
