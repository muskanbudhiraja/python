import time


def countdown():
    t = int(input('Enter no:'))
    while t > 0:
        print(t, end='\r')
        time.sleep(1)
        t -= 1

    print("U are ready to go!!")


countdown()
