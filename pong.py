import turtle
import time
import random

COLORS = ["Red", "Blue", "Green"]
SHAPES = ["square", "arrow", "circle", "turtle", "triangle"]
screen = turtle.Screen()
screen.tracer(0)
screen.title("Pong")
screen.bgcolor("black")
screen.setup(width=1000, height=600)
global p1arr, p2arr, ball, delay
p1arr = []
p2arr = []
ball = turtle.Turtle()
ball.shape("circle")
ball.color("white")
ball.penup()
ball2 = turtle.Turtle()
ball2.shape("circle")
ball2.color("white")
ball2.penup()


for x in range(0, 4):
    p1arr.append(turtle.Turtle())
    p1arr[x].shape(random.choice(SHAPES))
    p1arr[x].color("blue")
    p1arr[x].penup()
    p2arr.append(turtle.Turtle())
    p2arr[x].shape(random.choice(SHAPES))
    p2arr[x].color("red")
    p2arr[x].penup()

def resetGame():
    global delay, p1arr, p2arr
    delay = 0.08
    for x in range(0, 4):
        p1arr[x].goto(-450, 20*x)
        p2arr[x].goto(450, 20*x)

    ball.goto(0,0)
    ball.dx=1
    ball.dy=1
    ball2.goto(0,0)
    ball2.dx=1
    ball2.dy=.5



def p1moveup():
    moveup(p1arr)
def p1movedown():
    movedown(p1arr)
def p2moveup():
    moveup(p2arr)
def p2movedown():
    movedown(p2arr)

screen.listen()
screen.onkeypress(p1moveup, 'w')
screen.onkeypress(p1movedown,'s')
screen.onkeypress(p2moveup, 'Up')
screen.onkeypress(p2movedown, 'Down')

def movedown(turtlearr):
    for turtle in turtlearr:
        y=turtle.ycor()
        if y>-270:
            turtle.sety(turtle.ycor()-20)
        else: return

def moveup(turtlearr):
    for turtle in reversed(turtlearr):
        y=turtle.ycor()
        if y<270:
            turtle.sety(turtle.ycor()+20)
        else: return

def moveball(ball):
    global delay,p1arr, p2arr
    x=ball.xcor()
    y=ball.ycor()

    if y+20*ball.dy>300 or y+20*ball.dy<-300:
        ball.dy=-ball.dy

    for p1 in p1arr:
        if ball.distance(p1) < 20:
            ball.dx = -ball.dx
            delay -= 0.003
    for p2 in p2arr:
        if ball.distance(p2) < 20:
            ball.dx = -ball.dx
            delay -= 0.003
    ball.setx(x+10*ball.dx)
    ball.sety(y+10*ball.dy)


resetGame()
while True:
    screen.update()
    moveball(ball)
    moveball(ball2)
    ball.color(random.choice(COLORS))
    if ball.xcor()>500 or ball.xcor() < -500:
        resetGame()
    time.sleep(delay)

screen.mainloop()        
screen.update()
