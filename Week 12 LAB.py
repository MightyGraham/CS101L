import time

class Clock():

    def __init__(self, hour = 0, minute = 0, second = 0, mode = 0): #constructor
        self.hour = hour
        self.minute = minute
        self.second = second
        self.mode = mode

        
    def tick(self):
        self.second += 1 #start incrementing the seconds first
        if self.second > 59:
            self.second = 0
            self.minute += 1
            return self.minute
        elif self.minute > 59:
            self.minute = 0
            self.hour += 1
            return self.hour
        elif self.hour > 24:
            self.hour = 0
            self.second += 1
            return self.second
            

    def __str__(self):
        if self.mode == 0:
            return '{:02} : {:02} : {:02}'.format(self.hour, self.minute, self.second)
        elif self.mode == 1:
            return '{:02} : {:02} : {:02}'.format(self.hour, self.minute, self.second)


hour = input("What is the current hour ==> ")
minute = input("What is the current minute ==> ")
second = input("What is the current second ==> ")
mode = input("what mode? 0 for 24 hour clock, 1 for 12 hour clock => \n")
clock = Clock(hour, minute, second, mode)
print(clock)
while True:
    time.sleep(clock.tick())
