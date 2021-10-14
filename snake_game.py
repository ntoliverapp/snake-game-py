from turtle import *
from random import randrange
from freegames import square,vector

food=vector(0,0)
snake=[vector(10,0)]
aim=vector(0,-10)

def change(x,y): #we are given two parameters(x,y). 2D game. aim.x represents x axis. aim.y = y axis
    aim.x=x
    aim.y=y
    
def inside(head): #boundary values in the game. Snake stays inside boundary values. If out, illegal move.
    return -200 <head.x < 190 and -200 < head.y < 190

def move(): #give movement to our snake. Snake always move in forward direction. This is logic. -1 is forward movement value. Give the copy object --> move in forwar direction throughout the entire game.
    head=snake[-1].copy()
    head.move(aim)
    
    if not inside(head) or head in snake: #if head of snake crosses boundary or crosses its own body then the user is out of the game
        square(head.x, head.y,9,'red') #red square to indicate two outs. 
        update()
        return

    snake.append() #adda a red square if these conditions are satisfied

    if head == food: # if the head of the snake eats the food, it gets points
        print('snake',len(snake))
        food.x=randrange(-15,15)*10 #when snake catches food, new food will randomly appear
        food.y=randrange(-15,15)*10
    else:
        snake.pop(0)
    
clear()

for body in snake: #create snake element by creating for loop. snake is a combination solve square. 
    square(body.x,body.y,9,'green')

square(food.x,food.y,9,'red')
update() #update object 
ontimer(move, 100)

hideturtle()
tracer(False) #brings back the elements tot the initial state
listen() #continuously updates game
onkey(lambda:changes(10,0),'Right') #game controls using onkey, set the controls and give graph values
onkey(lambda:changes(-10,0),'Left')
onkey(lambda:changes(0,10),'Up')
onkey(lambda:changes(0,-10),'Down')

move()
done()







    
    