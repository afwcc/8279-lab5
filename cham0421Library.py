import math
from random import randrange
import time 

# Calculates Area of a Circle
# Input:  radius(float): Radius of the circle
# Output: Area  (float): Area of the circle
def calculateAreaOfCircle(radius):
  return math.pi * (radius**2)

# Calculates miles per gallon
# Input:  miles  (float): miles travelled  
#         gallons(float): gallons consumed
# Output: miles per gallon (float)
def calculateMpg(miles,gallons):
  return miles / gallons

# Convert Fahrenheit to Celsius 
# Input:  Fahrenheit(float): Tempurature in Fahrenheit
# Output: Celsius   (float): Tempurature in Celsius
def convertFahrenheitToCelsius(fahrenheit):
  return (fahrenheit - 32) * (5/9)

# Calculates Distance between 2 points
# Input: x  : x-corrdinate for point 1
#        y  : y-corrdinate for point 1
#        x1 : x-corrdinate for point 2
#        y1 : y-corrdinate for point 2
# Output: Distance (float): distance between the 2 points 
def calculateDistanceBetweenPoints(x,y,x1,y1):
  return math.sqrt(((x1-x)**2)+((y1-y)**2))

def clearScreen(lcd):
    lcd.clear()
    lcd.show()

def vertical(x):
    y = 0
    while (y < 63):
        lcd.set_pixel(x,y,1) # lcd.set_pixel(x,y,1)
        y = y + 1

def horonztail(y):
    x = 0
    while (x < 127):
        lcd.set_pixel(x,y,1) # lcd.set_pixel(x,y,1)
        x = x + 1

def staircase():
  x = 10
  y = 50
  width = 2
  hieght = 2

  while (x < 127 and y > 0):
    cw = 0
    ch = 0
    while (cw < width):
      lcd.set_pixel(x,y,1)
      x = x + 1
      cw = cw + 1
      if x > 127 and y < 0:
          break

    while (ch < hieght):
        lcd.set_pixel(x,y,1)
        y = y - 1
        ch = ch + 1
        if x > 127 and y < 0:
            break

def random_pixel()
    for a in range(0, 11):
        x = randrange(0, 127)
        y = randrange(0, 63)
        lcd.set_pixel(x,y,1)
        time.sleep(1)



def clearBacklight()
    backlight.set_pixel(x, r, g, b)
