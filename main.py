import turtle as t

playerAscore=0
playerBscore=0

window=t.Screen()
window.title("Ping Pong")
window.bgcolor("black")
window.setup(width=800,height=600)
window.tracer(0)

paddle1=t.Turtle()
paddle1.speed(0)
paddle1.shape("square")
paddle1.color("gray")
paddle1.shapesize(stretch_wid=5,stretch_len=1)
paddle1.penup()
paddle1.goto(-350,0)

paddle2=t.Turtle()
paddle2.speed(0)
paddle2.shape("square")
paddle2.color("gray")
paddle2.shapesize(stretch_wid=5,stretch_len=1)
paddle2.penup()
paddle2.goto(350,0)

ball=t.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ballxdir=0.2
ballydir=0.2

pen=t.Turtle()
pen.speed(0)
pen.color("red")
pen.penup()
pen.hideturtle()
pen.goto(0,250)
pen.write("score",align="center",font=('Arial',24,'normal'))

def paddle1up():
    y=paddle1.ycor()
    y=y+90
    paddle1.sety(y)
def paddle1down():
    y=paddle1.ycor()
    y=y-90
    paddle1.sety(y)

def paddle2up():
    y=paddle2.ycor()
    y=y+90
    paddle2.sety(y)
def paddle2down():
    y=paddle2.ycor()
    y=y-90
    paddle2.sety(y)

window.listen()
window.onkeypress(paddle1up,'w')
window.onkeypress(paddle1down,'s')
window.onkeypress(paddle2up,'Up')
window.onkeypress(paddle2down,'Down')

while True:
    window.update()
    ball.setx(ball.xcor()+ballxdir)
    ball.sety(ball.ycor()+ballydir)

    if ball.ycor()>290:
        ball.sety(290)
        ballydir=ballydir*-1
    if ball.ycor()<-290:
        ball.sety(-290)
        ballydir=ballydir*-1

    if ball.xcor()>390:
        ball.goto(0,0)
        ballxdir=ballxdir*-1
        playerAscore=playerAscore+1
        pen.clear()
        pen.write("Player A:{}   Player B:{}".format(playerAscore,playerBscore),align='center',font=('Arial',24,'normal'))

    if ball.xcor()<-390:
        ball.goto(0,0)
        ballxdir=ballxdir*-1
        playerBscore=playerBscore+1
        pen.clear()
        pen.write("Player A:{}   Player B:{}".format(playerAscore,playerBscore),align='center',font=('Arial',24,'normal'))

    if(ball.xcor()>340)and(ball.xcor()<350)and(ball.ycor()<paddle2.ycor()+40 and ball.ycor()>paddle2.ycor()-40):
        ball.setx(340)
        ballxdir=ballxdir*-1

    if (ball.xcor() <-340) and (ball.xcor() >-350) and (ball.ycor() < paddle1.ycor() + 40 and ball.ycor() > paddle1.ycor() - 40):
        ball.setx(-340)
        ballxdir = ballxdir*-1



