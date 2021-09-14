#game.py
import turtle
import math
import random
from playsound import playsound

#create a window screen
wn=turtle.Screen()
wn.title("TOUCH BALL")
wn.bgcolor('grey')
wn.bgpic('gamebac.gif')

#create a player
p=turtle.Turtle()
p.shape('triangle')
p.color('blue')

#score
s=turtle.Turtle()
global score
def scor(sc):
    s.color('white')
    s.up()
    score=sc
    s.hideturtle()
    s.goto(-200,260)
    scorestr="Score:{}".format(score)
    s.write(scorestr,False,align='left',font=('Arial',16))


#create a circle
c=turtle.Turtle()
c.color('red')
c.up()
c.goto(-100,100)
c.shape('circle')


#set border
b=turtle.Turtle()
b.up()
b.goto(-255,-255)
b.down()
b.color('yellow')
b.pensize(3)
for i in range(4):
    b.fd(513)
    b.left(90)
b.hideturtle()

#movement
p.up()
def turnleft():
    p.left(45)

def turnright():
    p.right(45)
    
def increasespeed():
    global speed
    speed=speed+1

    
turtle.listen()
turtle.onkey(turnleft,"Left")
turtle.onkey(turnright,"Right")
turtle.onkey(increasespeed,"Up")
speed=0
score=0
while(True):
    p.fd(speed)

    if(p.xcor()>230) or (p.xcor()<-230):
        playsound('col.mp3')
        p.right(180)
    
    if(p.ycor()>230) or (p.ycor()<-230):
        playsound('col.mp3')
        p.right(180)

    #collision
    d=math.sqrt(math.pow(p.xcor()-c.xcor(),2) + math.pow(p.ycor()-c.ycor(),2))
    if(d<20):
        playsound('tou.mp3')
        score=score+10
        s.undo()
        scor(score)
        c.goto(random.randint(-210,200),random.randint(-200,210))
    


