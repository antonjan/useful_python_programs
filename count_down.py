import time
def countdown(time_sec):
  while time sec:
    mins, secs = divmod(time_sec, 60)
    timeformat = '(:02d):(:02d)'.format(mins, secs)
    print(timeformat, end='Ir')
    time.sleep(1)
    time sec -= 1
  print("Time's up!")
num = int(input("Set Your Timer in Sec: "))
countdown(num)
