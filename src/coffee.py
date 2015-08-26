"""
WOU Coffee is licesed under the GNU General Public License (see LICENSE)

Feel free to contact me if you need help setting up your own coffee pot!
tdamron14@mail.wou.edu
"""

from time import sleep
from Tkinter import *
import sys
import datetime
import RPi.GPIO as GPIO

#Main function
def main():

    #Declaring global variables
    global date
    global temp

    #Setting variables
    date = datetime.datetime.now()
    f = open('data/time table', 'r+')
    difference = abs(date.hour - int(f.readline()))
    print "The date is " + str(date) + " coffee was last brewed " + str(difference) + " hour(s) ago" 

    #Is the coffee hot, or cold?
    if difference <= 1:
        temp = "HOT"
    else:
        temp = "COLD"

    print "[Coffee is " + temp + "]"

    #Set up the GPIO
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(18, GPIO.OUT)

    print "Welcome to WOU Coffee! Your request is being processed..."


    #Loop through arguments
    for args in sys.argv[1:]:
        if args == "make" or args == "-m":
            make()
        elif args == "stopall" or args == "-s":
            stopall()
        elif args == "with-gui" or args == "-gui":
            drawwindow()
        elif args == "help" or args == "-h":
            print "WOU Coffee is licensed under the GNU General Public License (See LICENSE)\ncoffee.py make || coffee.py -m >> Make a fresh cup of coffee\ncoffee.py stopall || coffee.py -s >> Stops all current operations\ncoffee.py -reheat || coffee.py -r >> Reheats the coffee in the coffee pot\ncoffee.py with-gui || coffee.py -gui >> Starts the WOU Coffee graphical user interface\ncoffee.py help || coffee.py -h >> Opens the help center" 
        elif args == "reheat" or args == "-r":
            reheat()
        else:
            print args + " is not a recognized command. Please enter \'coffee.py help\' or \'coffee.py -h\' for a list of recognized commands. Terminating."
            sys.exit(1)
    
    #Clean up GPIO
    GPIO.cleanup()

#Function that returns the estimated temperature
def gettemp():
    return "[Coffee is " + temp + "]"

#Reheats coffee in pot by turning coffee pot on for 300 seconds if the coffee is cold
def reheat():
    if temp == "COLD":
        output()
        sleep(300)
        stopall()
        temp = "HOT"
    else:
        print "Coffee already hot!"

#Stops all operations based on type of coffee pot
def stopall():
    f = open('data/conf', 'r+')
    pottype = f.readline()
    if pottype == 'single-function':
        output()
    elif pottype == 'dual-function':
        output()
        sleep(1)
        output()
    else:
        print "Error: " + pottype + " is not a regognized configuration. Please run \'python configure.py [configurations]\' to fix this problem."

#Records time before outputting to coffee pot
def make():
    f = open('data/time table', 'w')
    f.write(str(date.hour))
    output()

#Outputs from GPIO 18 for one second
def output():
    GPIO.output(18, 1)
    sleep(1)
    GPIO.output(18, 0)

#Function that takes a 'root' frame and adds a label with an image to it based on a 'ref' 
def addimage(root, ref):
    img = PhotoImage(file=ref)
    label = Label(root, image=img)
    label.photo = img
    return label

def drawwindow():
    #Declaring graphics variables
    root = Tk()
    root.wm_title("WOU Coffee")
    frame = Frame(bg="", colormap="new", background="white")
    templabel = Label(text=gettemp())
    button = Button(frame, text="Make Coffee", fg="white", background="red", command=make)
    stopbutton = Button(frame, text="Stop All", fg="white", background="blue", command=stopall)
    reheatbutton = Button(frame, text="Reheat", fg="white", background="dark green", command=reheat)
    addimage(frame, "img/wou_coffee.gif").pack()

    #Pack all elements onto the frame
    templabel.pack() 
    button.pack()
    stopbutton.pack()
    reheatbutton.pack()
    frame.pack()

    #Start the main loop
    root.mainloop()

main()
