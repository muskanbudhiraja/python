import time


def timer():
    user_input = int(input('enter time in seconds:'))
    while user_input:
        mins = int(user_input / 60)
        secs = user_input % 60
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end='\r')
        time.sleep(1)
        user_input -= 1


timer()
