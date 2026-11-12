"""joyPet's main function"""

from guts import constants
import time

def core():

  # Settings
  debug_mode = False
  interval = 2 #seconds
  timeout_dur = 30 # seconds
  default_hunger_loss = 1 # per update interval

  # Initialize variables
  running = True
  timeout_timer = 0
  
  # Hunger variables
  starting_hunger = 10
  starving = False
  hunger_loss = default_hunger_loss

  hunger_level_high = starting_hunger*0.8
  hunger_level_medium = starting_hunger*0.6
  hunger_level_low = starting_hunger*0.4

  #First update at start of runtime
  last_update_time = time.time() #first "last update time" is at beginning of runtime
  curr_hunger = starting_hunger

  print("Hello! My name is joyPet! Welcome to a new session!")
  print("My current hunger status is: " + str(curr_hunger))
  print("I'm doing swell :)")
  print("")
  
  
  while running:

    curr_time = time.time()
    time_passed = curr_time - last_update_time

    if debug_mode:
      print("curr_time: " + str(curr_time))
      print("start time: " + str(last_update_time))
      print("time passed:" + str(time_passed))
      print("timeout timer: " + str(timeout_timer))
      print("")

    if timeout_timer > timeout_dur:
      print("I'm joyPet! Goodbye for now!")
      running = False

    else:
      if (curr_time - last_update_time) > interval:
        timeout_timer += time_passed
        last_update_time = time.time()

        if not starving:
          new_hunger = curr_hunger - hunger_loss

          if (new_hunger > 0):
            curr_hunger = new_hunger
          elif not starving:
            curr_hunger = 0
            starving = True

        print("Hello! My name is joyPet!")
        print("My current hunger status is: " + str(curr_hunger))
        if starving:
          print("I am starving! I need food NOW!!! :((((((")
        elif curr_hunger >= hunger_level_high:
          print("I'm satisfied and not hungry. :)")
        elif (curr_hunger < hunger_level_high) and (curr_hunger >= hunger_level_medium):
          print("I'm somewhat hungry, I could eat!")
        elif (curr_hunger < hunger_level_medium) and (curr_hunger >= hunger_level_low):
          print("I'm hungry! I'd love to eat something.")
        elif (curr_hunger < hunger_level_low):
          print("I'm very hungry! Please feed me!!")
        print("")


  
if __name__ == '__main__':
  core()