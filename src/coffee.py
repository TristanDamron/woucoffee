"""
WOU Coffee is licensed under the GNU General Public License (see LICENSE)

Feel free to contact me if you need help setting up your own coffee pot!
tdamron14@mail.wou.edu
"""

from time import sleep
from Tkinter import *
from node import node
import sys
import datetime
import RPi.GPIO as GPIO

#Main function
def main():
    #Declaring global variables
    global date
    global temp
    global nodes
    global f

    #Setting variables
    date = datetime.datetime.now() 
    nodes = []
    f = open('data/time table', 'ar+')

    for line in f:
        nodes.append(node(str(line)))

    difference = calcdifference()
    
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

    findargs()

    #Close file
    f.close()
    
    #Clean up GPIO
    GPIO.cleanup()

#Function that returns the estimated temperature
def gettemp():
    return "[Coffee is " + temp + "]"

def findargs():
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
        elif args == "graph" or args == "-g":
            graph()
        else:
            print args + " is not a recognized command. Please enter \'coffee.py help\' or \'coffee.py -h\' for a list of recognized commands. Terminating."
            sys.exit(1)
    

#Calculate the time difference based on data from the time table
def calcdifference():
    if nodes[len(nodes) - 1].getyear() > date.year:
        difference = "WHAT YEAR IS IT?!"
    elif nodes[len(nodes) - 1].getmonth() > date.month:
        difference = "..."
    elif nodes[len(nodes) - 1].getday() > date.day:
        difference = "OVER 24"
    else:
        difference = date.hour - nodes[len(nodes) - 1].gethour()

    return difference

#Reheats coffee in pot by turning coffee pot on for 300 seconds if the coffee is cold
def reheat():
    if temp == "COLD":
        f.write(str(date.day) + " " + str(date.hour) + " " + str(date.month) + " " + str(date.year) + "\n")
        output()
        sleep(300)
        stopall()
    else:
        print "Coffee already hot!"

#Stops all operations based on type of coffee pot
def stopall():
    fconf = open('data/conf', 'r+')
    pottype = fconf.readline()
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
    f.write(str(date.day) + " " + str(date.hour) + " " + str(date.month) + " " + str(date.year) + "\n")
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

#Function that takes a 'root' and adds a button based on passed in options
def addbutton(root, text, color, background, command):
    button = Button(root, text=text, fg=color, background=background, command=command)
    return button

#Function that draw the WOU Coffee GUI's main window
def drawwindow(): 
    #Declaring graphics variables and packing them into the frame
    root = Tk()
    root.wm_title("WOU Coffee")
    frame = Frame(bg="", colormap="new", background="white")
    templabel = Label(text=gettemp()).pack()
    addimage(frame, "img/wou_coffee.gif").pack()
    addbutton(frame, "Make Coffee", "white", "red", make).pack()
    addbutton(frame, "Stop All", "white", "blue", stopall).pack()
    addbutton(frame, "Reheat", "white", "dark green", reheat).pack()
    frame.pack()

    #Start the main loop
    root.mainloop()

main()
