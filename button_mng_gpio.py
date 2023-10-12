from gpiozero import Button
from subprocess import check_call, CalledProcessError
from signal import pause

def reboot():
    print("Rebooting...")
    try:
        check_call(['/sbin/shutdown', '-r', 'now'])
    except CalledProcessError as e:
        # Handle the exception
        print(f"Command failed with return code {e.returncode}")
        print(f"Command output: {e.output}")
        # Perform error handling or recovery actions

def reactivate_usb():
    print("Reactivating USB...")
    try:
        check_call(['sudo', 'uhubctl', '-l', '1-1', '-a', '1'])
    except CalledProcessError as e:
        # Handle the exception
        print(f"Command failed with return code {e.returncode}")
        print(f"Command output: {e.output}")
        # Perform error handling or recovery actions

gpio_button = 4

print("Button listener started...")
shutdown_btn = Button(gpio_button, hold_time=2)
shutdown_btn.when_held = reboot
shutdown_btn.when_pressed = reactivate_usb
print("Waiting for button press...")
pause()