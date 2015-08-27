import datetime

class node(object):

    global day
    global hour
    global month
    global year

    def __init__(self, line):
        words = line.split(" ")
        self.day = words[0]
        self.hour = words[1]
        self.month = words[2]
        self.year = words[3]

    def getinfo(self):
        return self.day + " " + self.hour + " " + self.month + " " + self.year + "\n"
        
    def getday(self):
        return int(self.day)

    def gethour(self):
        return int(self.hour)

    def getmonth(self):
        return int(self.month)

    def getyear(self):
        return int(self.year)
