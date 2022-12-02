import pygame 
import random
import math

WHITE = (255, 255, 255) 
BLUE = (44, 198, 222)

 # setting the display screen size to 500 by 500
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption('Bouncing Ball Animation!')

x = random.randint(10, 500) 
# making the ball start at a random y-coordinate
y = random.randint(10, 480) 

# setting the default speed of the ball in the both axises to 2
speedX = 2 
speedY = 2 

#second ball

# making the ball start at a specified x-coordinate
inputX= int(input("Enter the ball's starting coordinate for the x-axis (above 10 and below 500): ")) 
# making the ball start at a specified y-coordinate
inputY = int(input("Enter the ball's starting coordinate for the y-axis (above 10 and below 480): ")) 

inputspeedX = int(input("Enter the ball's speed for the x-axis (1-5 suggested): "))
inputspeedY = int(input("Enter the ball's speed for the y-axis (1-5 suggested): "))

# setting the default ball's colour to black
color = 0 
ballColor = input("Pick a color for the ball: \n1. Red\n2. Pink\n3. Green\n4. Purple\n5. Yellow\nYour answer: ").lower()

if ballColor == "red" or ballColor == "1":
    # setting the variable's value to be the rgb code of red
    color = 255, 0, 0 
elif ballColor == "pink" or ballColor == "2":
    color = 255, 0, 127
elif ballColor == "green" or ballColor == "3":
    color = 0, 255, 0
elif ballColor == "purple" or ballColor == "4":
    color = 178, 87, 194
elif ballColor == "yellow" or ballColor == "5":
    color = 255, 255, 0


clock = pygame.time.Clock()

while True:
    clock.tick(60)

    screen.fill(BLUE)

    # First ball (uncustomized)

    pygame.draw.circle(screen, WHITE, (x, y), 25)

    x = x + speedX
    y = y + speedY

    # setting it to 10 so as soon as it hits the edge, it bounces
    
    if x >= 500 or x <= 10: 
        speedX = - speedX
    elif y >= 480 or y <= 10:
        speedY = - speedY

    # Second ball

    pygame.draw.circle(screen, color, (inputX, inputY), 25)
    inputX = inputX + inputspeedX
    inputY = inputX + inputspeedY

    if inputX >= 500 or inputX <= 10: 
        inputspeedX = - inputspeedX
    elif inputY >= 480 or inputY <= 10: 
        inputspeedY = - inputspeedY

        
  #Applying the Distance formula to deal with collision

    distance_x = (inputX - x) ** 2
    distance_y = (inputY - y) ** 2
        
    distance = distance_x + distance_y
    distance = math.sqrt(distance)

    # if the distance between the balls is 42 or less,
    if distance <= 42: 
        
        # set the first ball's steps of speed to 0 (so it won't move any further
        speedX = 0 
        speedY = 0 

        # set the second ball's steps of speed to 0
        inputspeedX = 0  
        inputspeedY = 0 
        
        print("The two balls have collided and therefore stopped moving.")
        break

        
    pygame.display.flip()
