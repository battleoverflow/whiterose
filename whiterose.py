import time, os, platform
from datetime import datetime

###############################################
#                                             #
#   Whiterose Timing Library                  #
#   Author: battleoverflow                    #
#   GitHub: https://github.com/battleoverflow #
#                                             #
###############################################

VERSION = "0.1.7"

class Whiterose:

    def timer_s(self, seconds):

        while True:
            time.sleep(seconds) # Number of seconds

            if platform.system() == 'Windows':
                os.system('cls')
            else:
                os.system("clear")
            
            timer = datetime.now().strftime("%I:%M:%S %p")

            print(timer)
    
    def timer_m(self, minutes):
        minutes = minutes * 60
        
        while True:
            time.sleep(minutes) # Number of minutes

            if platform.system() == 'Windows':
                os.system('cls')
            else:
                os.system("clear")
            
            timer = datetime.now().strftime("%I:%M:%S %p")

            print(timer)
    
    def timer_h(self, hours):
        hours = hours * 3600

        while True:
            time.sleep(hours) # Number of hours

            if platform.system() == 'Windows':
                os.system('cls')
            else:
                os.system("clear")
            
            timer = datetime.now().strftime("%I:%M:%S %p")

            print(timer)
