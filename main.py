import time
import board
import adafruit_pct2075
import busio
import digitalio
import displayio
import adafruit_displayio_ssd1306
from adafruit_display_text import label
import terminalio


# Initialise the LEDs
#Blue LED
led_cool = digitalio.DigitalInOut(board.GP12)
led_cool.direction = digitalio.Direction.OUTPUT
led_cool.value = True
#Red LED
led_hot = digitalio.DigitalInOut(board.GP11)
led_hot.direction = digitalio.Direction.OUTPUT
led_hot.value = True 


# Initialise the I2C bus and display
displayio.release_displays()

i2c1 = busio.I2C(scl=board.GP3, sda=board.GP2)
display_bus = displayio.I2CDisplay(i2c1, device_address=0x3c)
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=32)
splash = displayio.Group()
display.show(splash)
text = "Loading"
text_area = label.Label(terminalio.FONT, text=text, color=0xFFFF00, x=28, y=15)
splash.append(text_area)
display.show(splash)

# Initialise the I2C bus and Temp sensor
i2c = busio.I2C(scl=board.GP21, sda=board.GP20)
pct = adafruit_pct2075.PCT2075(i2c)

# Initial loading LED flashing
loading = 10

while loading > 0:
    loading -= 1
    led_cool.value = False
    led_hot.value = True
    time.sleep(0.2)
    led_cool.value = True
    led_hot.value = False
    time.sleep(0.2)
    

#Once loaded the Pico will run the while True: code every 5 seconds.
while True:
    print("Temperature: %.2f C"%pct.temperature)
    text = "Temp: %.2f C"%pct.temperature
    text_area.text = text
    # WHO recommends a temperature between 18 and 23 degrees 
    # the temperature reading is checked and the corrisponding LED is turned on if temp is outside the recommended range. 
    if pct.temperature > 18.00:
        led_cool.value = False
    else:
        led_cool.value = True
    
    if pct.temperature > 23.00:
        led_hot.value = True
    else:
        led_hot.value = False
    display.show(splash)
    time.sleep(5)