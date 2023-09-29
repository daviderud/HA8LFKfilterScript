from gpiozero import LEDBoard
from time import sleep
from signal import pause

#1)GPIO4 purple
#2)GPIO27 blu
#3)GPIO22 green
#4)GPIO23 yellow
#5)GPIO24 orange
#6)GPIO25 red
#7)GPIO5 brown

#8)GPIO6 gray - transistor

gpio_1M6_2M5 = 4
gpio_2M5_4M7 = 27
gpio_4M7_7M5 = 22
gpio_7M5_14M5 = 23
gpio_14M5_21M5 = 24
gpio_21M5_33M = 25
gpio_33M_56M = 5

gpio_transistor = 6

filter_outputs = LEDBoard(gpio_1M6_2M5, )

leds.on()
sleep(1)
leds.off()
sleep(1)
leds.value = (1, 0, 1, 0, 1)
sleep(1)
leds.blink()

pause()