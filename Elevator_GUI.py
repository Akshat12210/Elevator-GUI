import time
import tkinter as tk
from tkinter import *
import tkinter.messagebox

#############Code#####################################################
window = Tk()
window.title("Elevator Animation")
window.geometry("500x600")
window.configure(background="black")
Title = Label (window, text="Elevator", bg="black", fg="white", font="Arial 14 bold")
Title.pack()
canvas = Canvas(window, width=500,height=500)
canvas.pack()
elevator = canvas.create_rectangle(60, 480, 80, 420, fill="grey")
###########################All the boxes and lines##########################################

canvas.create_line(60,60,60,480, fill="black")
canvas.create_line(80,60,80,120, fill="black")
canvas.create_line(80,180,80,240, fill="black")
canvas.create_line(80,300,80,360, fill="black")
canvas.create_line(80,420,80,480,fill='black')
canvas.create_line(480,60,480,480, fill="black")
canvas.create_line(60,60,480,60)
canvas.create_line(60,120,480,120)
canvas.create_line(60,180,480,180)
canvas.create_line(60,240,480,240)
canvas.create_line(60,300,480,300)
canvas.create_line(60,360,480,360)
canvas.create_line(60,420,480,420)
canvas.create_line(60,480,480,480)
canvas.create_text(70, 450, fill="black", font="Arial 10 bold", text="G")
canvas.create_text(70, 330, fill="black", font="Arial 10 bold", text="1")
canvas.create_text(70, 210, fill="black", font="Arial 10 bold", text="2")
canvas.create_text(70, 90, fill="black", font="Arial 10 bold", text="3")

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
    else:
        tkinter.messagebox.showinfo('Alert','You are on the Top Floor')
        
def DOWN():
    if CURRENT_FLOOR>0:
        move(CURRENT_FLOOR-1)
    else:
         tkinter.messagebox.showinfo('Alert','You are on the Bottom Floor')

####################################################################################################################

#lambda - A lambda function can take any number of arguments, but can only have one expression.######

blank1 = Label (window, text="Buttons  ", bg="black", fg="white", font="none 12 bold")
blank1.pack(side=TOP)
new_floor = 0

while True:
    gf = Button (window, text="G",font="Arial 10 bold", width=4,height=1,fg="green", activebackground="white", command=lambda: move(0))
    gf.place(x=132,y=565)
    floor1 = Button (window, text="1",font="Arial 10 bold",width=4,height=1, bg="black", fg="green", activebackground="white", command=lambda: move(1))
    floor1.place(x=200,y=565)
    floor2 = Button (window, text="2",font="Arial 10 bold",width=4,height=1, bg="black", fg="green", activebackground="white", command=lambda: move(2))
    floor2.place(x=260,y=565)
    floor3 = Button (window, text="3",font="Arial 10 bold",width=4,height=1, bg="black", fg="green", activebackground="white", command=lambda: move(3))
    floor3.place(x=320,y=565)
    up=Button(window,bg="black",fg="white",font="Arial 9 bold",width=5,height=2,text="Up",command=lambda: UP())
    up.place(x=10,y=250)
    down=Button(window,bg="black",fg="white",font="ARial 9 bold",width=5,height=2,text="Down",command=lambda: DOWN())
    down.place(x=10,y=300)
    break
mainloop()
