# Circuitpython temperature monitor

## Intro

Initially, built as a Christmas gift for someone dealing with a dodgy boiler. This was designed to be a quick and easy temperature indicator.

The temperature range is based on recommendations of the World Health Organisation aiming for an optimal temperature of at least 18°C but not higher than 23°C.

If a temperature below 18°C is recorded on the PCT2075 a blue LED is switched on. If it goes above 23°C the red LED switches on. A nice simple indication. The addition of a screen was added to display the current temperature.

![Pico in action showing 12.5°C](image1.jpg =600x800)

A nice simple project

## Parts

- PCT2075 breakout board
- SSD1306 display
- Pico
- Blue LED
- Red LED

## Code

The code initialises the I2C buses along with the temperature sensor and display.

A quick little loading animation plays rapidly switching the LEDs on and off.

Once loaded every 5 seconds the Pico takes a reading from the temperature sensor and updates the display. If the recorded temperature is outside the ideal range then either the blue or the red LED switches on depending whether the temperature is too cold or too hot.