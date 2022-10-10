import time

def countdown(t):
  
  if ((t == 10) or (t == 0)):
    while t:
      mins, secs = divmod(t, 60)
      timer = '{:02d}:{:02d}'.format(mins, secs)
      print(timer, end="\r")
      time.sleep(1)
      t -= 1
      
    print("Fire in the hole!!")
  
t = 10

countdown(int(t))