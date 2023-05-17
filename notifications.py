from pynotifier import Notification
import schedule
import datetime
import time
import keyboard
on = True
def turn_off():
    on = False

def turn_on():
    on = True

amount = int(input("Enter the number of notifications: "))
def run_notification(title_, description_, duration_, urgency_):
    Notification(
            title=title_,
            description=description_,
            duration=int(duration_),
            urgency=urgency_
        ).send()


def notification():
    for number in range(amount):
        title_ = input("Title: ")
        description_ = input('Description: ')
        duration_ = input('Notification duration (seconds): ')
        urgency_ = input('Urgency: ')
        hour = input('Run every how many hours (random/datetime/until): ')
        if hour == 'random':
            start = int(input('Start: '))
            end = int(input('Stop: '))
            schedule.every(start).to(end).seconds.do(run_notification, title_, description_, duration_, urgency_)
        elif hour == 'datetime':
            until = input('Specific datetime (year, month, date, hour, minute, second): ')
            interval = int(input('Interval (hours): '))
            schedule.every(interval).hours.until(datetime.datetime.strptime(until, '%Y-%m-%d %H:%M:%S')).do(run_notification, title_, description_, duration_, urgency_)
        elif hour == 'until':
            until = input('Stop time (hour, minute, second): ')
            interval = input('Interval (h/m): ')
            if interval == 'h':
                interval_time = int(input('Interval time (hours): '))
                schedule.every(interval_time).hours.do(run_notification, title_, description_, duration_, urgency_)
            elif interval == 'm':
                interval_time = int(input('Interval time (minutes): '))
                schedule.every(interval_time).minutes.do(run_notification, title_, description_, duration_, urgency_)
            else:
                print('Invalid argument')
        
keyboard.add_hotkey('ctrl+shift+delete', notification)
keyboard.add_hotkey('ctrl+alt+delete', run_notification)
keyboard.add_hotkey('ctrl+shift+tab', turn_off)
keyboard.add_hotkey('ctrl+alt+tab', turn_on)
keyboard.wait()

notification()
while on:
    schedule.run_pending()
    time.sleep(1)
schedule.cancel_job(run_notification)