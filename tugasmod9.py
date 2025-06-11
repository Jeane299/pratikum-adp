import os 
import time
from termcolor import colored, cprint
os.system('cls')
for j in range (3):
    cprint("|", 'white', 'on_black', end="")
    time.sleep(0.2)
    cprint(" "*20, 'white', 'on_red', end="")
    time.sleep(0.2)
    print()
for j in range (3):
    cprint("|", 'white', 'on_black', end="")
    time.sleep(0.2)
    cprint(" "*20, 'white', 'on_white', end="")
    time.sleep(0.2)
    print()

for j in range (10):
    cprint("|", 'white', 'on_black', end="")
    time.sleep(0.2)
    print()
# import os
# from termcolor import colored, cprint
# for i in range (3):
#     cprint(" "*20, 'red', 'on_red', end="")
#     cprint(" "*10, 'green', 'on_green', end="")
#     print()
# for i in range (3):
#     cprint(" "*10, 'white', 'on_blue', end="")
#     cprint(" "*10, 'white', 'on_yellow', end="")
#     print()



