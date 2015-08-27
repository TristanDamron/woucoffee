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
<<<<<<< HEAD
    global f
=======
>>>>>>> 2ce7c3f49e402b722499488942f3aea707d5c181

    #Setting variables
    date = datetime.datetime.now() 
    nodes = []
<<<<<<< HEAD
    f = open('data/time table', 'ar+')
=======
    f = open('data/time table', 'r+')
>>>>>>> 2ce7c3f49e402b722499488942f3aea707d5c181

    for line in f:
        nodes.append(node(str(line)))

<<<<<<< HEAD
    difference = calcdifference()
    
=======
    f.close()

    if nodes[len(nodes) - 1].getyear() > date.year:
        difference = "WHAT YEAR IS IT?!"
    elif nodes[len(nodes) - 1].getmonth() > date.month:
        difference = "..."
    elif nodes[len(nodes) - 1].getday() > date.day:
        difference = "OVER 24"
    elif nodes[len(nodes) - 1].gethour() > 0:
        difference = nodes[len(nodes) - 1].gethour() - date.hour
    else:
        difference = "ERROR - 404 (Time table data not found)"

>>>>>>> 2ce7c3f49e402b722499488942f3aea707d5c181
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

<<<<<<< HEAD
    findargs()

    #Close file
    f.close()
    
    #Clean up GPIO
    GPIO.cleanup()

#Function that returns the estimated temperature
def gettemp():
    return "[Coffee is " + temp + "]"

def findargs():
=======
>>>>>>> 2ce7c3f49e402b722499488942f3aea707d5c181
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
<<<<<<< HEAD
        elif args == "graph" or args == "-g":
            graph()
=======
>>>>>>> 2ce7c3f49e402b722499488942f3aea707d5c181
        else:
            print args + " is not a recognized command. Please enter \'coffee.py help\' or \'coffee.py -h\' for a list of recognized commands. Terminating."
            sys.exit(1)
    
<<<<<<< HEAD

#Calculate the time difference based on data from the time table
def calcdifference():
    if nodes[len(nodes) - 1].getyear() > date.year:
        difference = "WHAT YEAR IS IT?!"
    elif nodes[len(nodes) - 1].getmonth() > date.month:
        difference = "..."
    elif nodes[len(nodes) - 1].getday() > date.day:
        difference = "OVER 24"
    elif nodes[len(nodes) - 1].gethour() > 0:
        difference = nodes[len(nodes) - 1].gethour() - date.hour
    else:
        difference = "ERROR - 404 (Time table data not found)"
    
    return difference
=======
    #Clean up GPIO
    GPIO.cleanup()

#Function that returns the estimated temperature
def gettemp():
    return "[Coffee is " + temp + "]"
>>>>>>> 2ce7c3f49e402b722499488942f3aea707d5c181

#Reheats coffee in pot by turning coffee pot on for 300 seconds if the coffee is cold
def reheat():
    if temp == "COLD":
<<<<<<< HEAD
=======
        f = open('data/time table', 'a')
>>>>>>> 2ce7c3f49e402b722499488942f3aea707d5c181
        f.write(str(date.day) + " " + str(date.hour) + " " + str(date.month) + " " + str(date.year) + "\n")
        output()
        sleep(300)
        stopall()
    else:
        print "Coffee already hot!"

#Stops all operations based on type of coffee pot
def stopall():
<<<<<<< HEAD
    fconf = open('data/conf', 'r+')
    pottype = fconf.readline()
=======
    f = open('data/conf', 'r+')
    pottype = f.readline()
>>>>>>> 2ce7c3f49e402b722499488942f3aea707d5c181
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
<<<<<<< HEAD
    f.write(str(date.day) + " " + str(date.hour) + " " + str(date.month) + " " + str(date.year) + "\n")
=======
    f = open('data/time table', 'a')
    f.write(str(date.day) + " " + str(date.hour) + " " + str(date.month) + " " + date.year + "\n")
    f.close()
>>>>>>> 2ce7c3f49e402b722499488942f3aea707d5c181
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

<<<<<<< HEAD
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
=======
#Declaring graphics variables
def drawwindow(): 
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
>>>>>>> 2ce7c3f49e402b722499488942f3aea707d5c181
    frame.pack()

    #Start the main loop
    root.mainloop()

main()
