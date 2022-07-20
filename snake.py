import turtle
import time
import random

delay=0.1
score=0
h_score=0

screen=turtle.Screen()
screen.title("Sna")
screen.bgcolor("green")

screen.setup(width=600, height=600)
screen.tracer(0)

colorwheel= ["blue","yellow", "red", "orange", "purple"]

head=turtle.Turtle()
head.shape("square")
head.color(random.choice(colorwheel))
head.penup()
head.goto(0, 0)
head.direction="stop"

segments=[]
dropped=[]

def move():
    for index in range(len(segments)-1, 0, -1):
        x=segments[index-1].xcor()
        y=segments[index-1].ycor()
        segments[index].goto(x, y)
    if len(segments)>0:
        x=head.xcor()
        y=head.ycor()
        segments[0].goto(x, y)
    if head.direction == "up":
        y=head.ycor()
        head.sety(y+20)
    if head.direction == "down":
            y = head.ycor()
            head.sety(y-20)
    if head.direction == "left":
        x=head.xcor()
        head.setx(x-20)
    if head.direction =="right":
        x=head.xcor()
        head.setx(x+20)

pen=turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 250)

def drawscore():
    pen.clear()
    pen.write("Score: {} High Score ,{}"
              .format(score, h_score),
              align="center",
              font=("candara", 24, "bold"))




def turn(direc):
    if direc=="left" and head.direction=="right":
        return
    if direc=="right" and head.direction=="left":
     return
    if direc=="up" and head.direction=="down":
      return
    if direc=="down" and head.direction=="up":
     return
    head.direction=direc

food=turtle.Turtle()
f_shape=random.choice(["circle", "square", "triangle"])
f_color=random.choice(colorwheel)
food.speed(0)
food.shape(f_shape)
food.color(f_color)
food.penup()
food.goto(0, 100)



def checkfood(food):
    global score, delay, segments, h_score
    food.color(random.choice(colorwheel))
    if head.distance(food) < 20:
        x=random.randint(-270, 270)
        y=random.randint(-270, 270)
        food.goto(x,y)
        score += 10
        if score > h_score:
            h_score=score
        delay-=0.001
        new_seg=turtle.Turtle()
        new_seg.speed(0)
        new_seg.shape("square")
        new_seg.color(random.choice(colorwheel))
        new_seg.penup()
        segments.append(new_seg)

def checkFOODEVIL(food):
    global segments
    if head.distance(food)<20:
        x=random.randint(-270, 270)
        y=random.randint(-270, 270)
        for seg in segments:
            dropped.append(seg)
        segments=[]



def checkwalls():
    x=head.xcor()
    y=head.ycor()
    if x>300 or x<-300:
        resetgame()
    if y>300 or y<-300:
        resetgame()

def checksegments():
    for segment in segments:
        segment.color(random.choice(colorwheel))
        if segment.distance(head)<20:
            resetgame()





def resetgame():
    global score, delay, segments
    time.sleep(1)
    head.goto(0,0)
    head.direction="Stop"
    score=0
    delay=0.1
    for segment in segments:
        segment.goto(1000,1000)
    segments=[]









screen.listen()
screen.onkey(lambda: turn("left"), 'Left')
screen.onkey(lambda: turn("right"), 'Right')
screen.onkey(lambda: turn("up"), 'Up')
screen.onkey(lambda: turn("down"), 'Down')






while True:
    screen.update()
    move()
    checkwalls()
    checkFOODEVIL(food)
    checksegments()
    checkfood(food)
    drawscore()
    time.sleep(delay)
screen.mainloop()

