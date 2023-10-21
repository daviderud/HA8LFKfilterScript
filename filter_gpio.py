from gpiozero import LEDBoard
import os
import subprocess
from subprocess import check_call, CalledProcessError

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

#1)GPIO12 purple
#2)GPIO27 blu
#3)GPIO22 green
#4)GPIO23 yellow
#5)GPIO24 orange
#6)GPIO25 red
#7)GPIO26 brown

#8)GPIO13 gray - transistor

gpio_1M6_2M5 = 12
gpio_2M5_4M7 = 27
gpio_4M7_7M5 = 22
gpio_7M5_14M5 = 23
gpio_14M5_21M5 = 24
gpio_21M5_33M = 25
gpio_33M_56M = 26

gpio_transistor = 13


filter_outputs = LEDBoard(gpio_1M6_2M5, gpio_2M5_4M7, gpio_4M7_7M5, gpio_7M5_14M5, gpio_14M5_21M5, gpio_21M5_33M, gpio_33M_56M, gpio_transistor)

status_1M6_2M5 = 0
status_2M5_4M7 = 0
status_4M7_7M5 = 0
status_7M5_14M5 = 0
status_14M5_21M5 = 0
status_21M5_33M = 0
status_33M_56M = 0
transistor_status = 0

filter_outputs.off()

while True:
    # Call the function to clear the console
    clear_console()

    # ask the user which filter ouput to turn on
    print("Current status:")
    print("+---------+---------+---------+----------+-----------+----------+---------+------------+")
    print("| 1M6 2M5 | 2M5 4M7 | 4M7 7M5 | 7M5 14M5 | 14M5 21M5 | 21M5 33M | 33M 56M | Transistor |")
    print(f"|    {status_1M6_2M5}    |    {status_2M5_4M7}    |    {status_4M7_7M5}    |     {status_7M5_14M5}    |     {status_14M5_21M5}     |    {status_21M5_33M}     |    {status_33M_56M}    |     {transistor_status}      |")
    print("+---------+---------+---------+----------+-----------+----------+---------+------------+")
    print("|         |         |         |          |           |          |         |    8 = ON  |")
    print("|   1     |    2    |    3    |     4    |     5     |    6     |    7    |    9 = OFF |")
    print("|         |         |         |          |           |          |         |            |")
    print("+---------+---------+---------+----------+-----------+----------+---------+------------+")
    print("+                                     10 = ALL OFF                                     +")
    print("+--------------------------------------------------------------------------------------+")
    print("USB manager:")
    print("11 - Switch ON USB")
    print("12 - Switch OFF USB")
    print("13 - Read USB status")
    print("RTL-SDR server:")
    print("14 - Run RTL-SDR TCP (bias tee OFF)")


    print("Select one of the numbers - 0 to exit:")
#    print("1) 1.6 - 2.5 MHz")
#    print("2) 2.5 - 4.7 MHz")
#    print("3) 4.7 - 7.5 MHz")
#    print("4) 7.5 - 14.5 MHz")
#    print("5) 14.5 - 21.5 MHz")
#    print("6) 21.5 - 33 MHz")
#    print("7) 33 - 56 MHz")
#    print("---")
#    print("8) Transistor ON")
#    print("9) Transistor OFF")
#    print("---")
#    print("0) Exit")

    user_input = input(">")
    if user_input == "":
        selected_option = 0
    else:
        selected_option = int(user_input)

    if selected_option == 1:
        status_1M6_2M5 = 1
        status_2M5_4M7 = 0
        status_4M7_7M5 = 0
        status_7M5_14M5 = 0
        status_14M5_21M5 = 0
        status_21M5_33M = 0
        status_33M_56M = 0  
    elif selected_option == 2:
        status_1M6_2M5 = 0
        status_2M5_4M7 = 1
        status_4M7_7M5 = 0
        status_7M5_14M5 = 0
        status_14M5_21M5 = 0
        status_21M5_33M = 0
        status_33M_56M = 0  
    elif selected_option == 3:
        status_1M6_2M5 = 0
        status_2M5_4M7 = 0
        status_4M7_7M5 = 1
        status_7M5_14M5 = 0
        status_14M5_21M5 = 0
        status_21M5_33M = 0
        status_33M_56M = 0  
    elif selected_option == 4:
        status_1M6_2M5 = 0
        status_2M5_4M7 = 0
        status_4M7_7M5 = 0
        status_7M5_14M5 = 1
        status_14M5_21M5 = 0
        status_21M5_33M = 0
        status_33M_56M = 0  
    elif selected_option == 5:
        status_1M6_2M5 = 0
        status_2M5_4M7 = 0
        status_4M7_7M5 = 0
        status_7M5_14M5 = 0
        status_14M5_21M5 = 1
        status_21M5_33M = 0
        status_33M_56M = 0  
    elif selected_option == 6:
        status_1M6_2M5 = 0
        status_2M5_4M7 = 0
        status_4M7_7M5 = 0
        status_7M5_14M5 = 0
        status_14M5_21M5 = 0
        status_21M5_33M = 1
        status_33M_56M = 0  
    elif selected_option == 7:
        status_1M6_2M5 = 0
        status_2M5_4M7 = 0
        status_4M7_7M5 = 0
        status_7M5_14M5 = 0
        status_14M5_21M5 = 0
        status_21M5_33M = 0
        status_33M_56M = 1  
    elif selected_option == 8:
        transistor_status = 1
    elif selected_option == 9:
        transistor_status = 0    
    elif selected_option == 10:
        status_1M6_2M5 = 0
        status_2M5_4M7 = 0
        status_4M7_7M5 = 0
        status_7M5_14M5 = 0
        status_14M5_21M5 = 0
        status_21M5_33M = 0
        status_33M_56M = 0 
        transistor_status = 0
        
    filter_outputs.value = (status_1M6_2M5, status_2M5_4M7, status_4M7_7M5, status_7M5_14M5, status_14M5_21M5, status_21M5_33M, status_33M_56M, transistor_status)

    if selected_option == 11:
        print("Activating USB...")
        try:
            check_call(['sudo', 'uhubctl', '-l', '1-1', '-a', '1'])
        except CalledProcessError as e:
            # Handle the exception
            print(f"Command failed with return code {e.returncode}")
            print(f"Command output: {e.output}")
        input("Press Enter to continue...")

    if selected_option == 12:
        print("De-activating USB...")
        try:
            check_call(['sudo', 'uhubctl', '-l', '1-1', '-a', '0'])
        except CalledProcessError as e:
            # Handle the exception
            print(f"Command failed with return code {e.returncode}")
            print(f"Command output: {e.output}")
        input("Press Enter to continue (via Vnc)...")

    if selected_option == 13:
        print("Checking USB...")
        try:
            check_call(['sudo', 'uhubctl'])
        except CalledProcessError as e:
            # Handle the exception
            print(f"Command failed with return code {e.returncode}")
            print(f"Command output: {e.output}")
        input("Press Enter to continue...")

    if selected_option == 14:
        print("Launching rtl-tcp...")
        subprocess.Popen(["rtl-tcp", "-a", "192.168.2.82"], shell=True, stdin=None, stdout=None, stderr=None)
        print("Done")


    if selected_option == 0:
        print("Exiting... Switch off everything? Y/n")
        answer = input()
        if answer == "Y" or answer == "y" or answer == "":
            print("Switching off everything...")
            filter_outputs.off()
        break

print("Bye!")