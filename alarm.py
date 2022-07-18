import datetime
from playsound import playsound
alarmHour = int(input("enter hour:"))
alarmMin = int(input("enter min:"))
#alarmAm = input("am / pm: ")

#f alarmAM=="pm":
   #14alarmHour+=12

while True:
    if alarmHour==datetime.datetime.now().hour and alarmMin==datetime.datetime.now().minute:
        print("playing..")
        playsound("punky.mp3")
        break

