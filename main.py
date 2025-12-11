from sense_hat import SenseHat
from time import sleep
from random import choice
import random
sense = SenseHat()
sense.clear()
blue = (0, 0, 255)
off = (0,0,0)
yellow = (255,255,0)
orange = (255, 165, 0)

#These display the number in a matrix
def dice_1():
    B = blue
    O = off
    one_num = [
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, B, B, O, O, O,
    O, O, O, B, B, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    ]
    return one_num

def dice_2():
    B = blue
    O = off
    two_num = [
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, B, B, O,
    O, O, O, O, O, B, B, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, B, B, O, O, O, O, O,
    O, B, B, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    ]
    return two_num

def dice_3():
    B = blue
    O = off
    three_num = [
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, B, B, O,
    O, O, O, O, O, B, B, O,
    O, O, O, B, B, O, O, O,
    O, O, O, B, B, O, O, O,
    O, B, B, O, O, O, O, O,
    O, B, B, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    ]
    return three_num

def dice_4():
    B = blue
    O = off
    four_num = [
    O, O, O, O, O, O, O, O,
    O, B, B, O, O, B, B, O,
    O, B, B, O, O, B, B, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, B, B, O, O, B, B, O,
    O, B, B, O, O, B, B, O,
    O, O, O, O, O, O, O, O,
    ]
    return four_num

def dice_5():
    B = blue
    O = off
    five_num = [
    O, O, O, O, O, O, O, O,
    O, B, B, O, O, B, B, O,
    O, B, B, O, O, B, B, O,
    O, O, O, B, B, O, O, O,
    O, O, O, B, B, O, O, O,
    O, B, B, O, O, B, B, O,
    O, B, B, O, O, B, B, O,
    O, O, O, O, O, O, O, O,
    ]
    return five_num

def dice_6():
    B = blue
    O = off
    six_num = [
    O, B, B, O, O, B, B, O,
    O, B, B, O, O, B, B, O,
    O, O, O, O, O, O, O, O,
    O, B, B, O, O, B, B, O,
    O, B, B, O, O, B, B, O,
    O, O, O, O, O, O, O, O,
    O, B, B, O, O, B, B, O,
    O, B, B, O, O, B, B, O,
    ]
    return six_num

dice_roll = [
    (1, dice_1()),
    (2, dice_2()),
    (3, dice_3()),
    (4, dice_4()),
    (5, dice_5()),
    (6, dice_6())
]

def roll_dice():
    #rolls the dice
    #randomly selects a number to display
    number, pixels = choice(dice_roll)
    #Shows the 
    sense.set_pixels(pixels)
    sleep(2)
    sense.clear()
    return number

    
def sparkle():
# Pick a random pixel
    x = random.randint(0, 7)
    y = random.randint(0, 7)
    
    # Pick a random color
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    
    # Set the pixel
    sense.set_pixel(x, y, r, g, b)
    

while True:
    sparkle()
    for event in sense.stick.get_events():
        if event.action == "pressed" and event.direction == "middle":
            card_dice = random.randint(1,10)
            if card_dice <= 9: #!change probablity here
                # Check accelerometer
                acceleration = sense.get_accelerometer_raw() 
                x = abs(acceleration['x'])
                y = abs(acceleration['y'])
                z = abs(acceleration['z'])
                
                # If shaken enough, roll the dice
                if x > 0.75 or y > 0.75 or z > 0.75:
                    sense.clear()#clears the display
                    sleep(.1) #waits a tenth of a second then..
                    roll_dice()  # This rolls and displays the dice
    
            else:
                #Code for alternating color on exclamation mark
                #This signifys that the player must draw a random event car
                sense.clear()
                sense.show_letter("!", text_colour = yellow)
                sleep(.25)
                sense.show_letter("!", text_colour = orange)
                sleep(.25)
                sense.show_letter("!", text_colour = yellow)
                sleep(.25)
                sense.show_letter("!", text_colour = orange)
                sleep(.25)
                sense.show_letter("!", text_colour = yellow)
                sleep(.25)
                sense.show_letter("!", text_colour = orange)
                sleep(.25)
                sense.show_letter("!", text_colour = yellow)
                
    sleep(0.1)
                        
                        
