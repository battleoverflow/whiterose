"""
This example allows the user to choose their preferred method of time. The library currently support seconds, minutes, and hours.

timer_s() - Time updates in real-time every second
timer_m() - Time updates in real-time every minute
timer_h() - Time updates in real-time every hour

Example: python3 example.py
"""

###############################################
#                                             #
#   example.py                                #
#   Author: Hifumi1337                        #
#   GitHub: https://github.com/Hifumi1337     #
#                                             #
###############################################

from whiterose.whiterose import Whiterose

wr = Whiterose()

def one_s_timer():
    wr.timer_s(1) # Real-time timer ever 1 second.

def one_m_timer():
    wr.timer_m(1) # Real-time timer ever 1 minute

def one_h_timer():
    wr.timer_h(1) # Real-time timer ever 1 hour

print("Seconds  =>  0")
print("Minutes  =>  1")
print("Hours    =>  2")

timer_method = input("Choose your timer method (ex: 1): ")

if timer_method == "0":
    try:
        one_s_timer()
    except KeyboardInterrupt:
        timer_method = input("\nChoose your timer method (If done, press Ctrl+C again): ")
elif timer_method == "1":
    try:
        one_m_timer()
    except KeyboardInterrupt:
        timer_method = input("\nChoose your timer method (If done, press Ctrl+C again): ")
elif timer_method == "2":
    try:
        one_h_timer()
    except KeyboardInterrupt:
        timer_method = input("\nChoose your timer method (If done, press Ctrl+C again): ")
else:
    print("Please choose one of the following options")
