#Ball_Game
from turtle import Turtle, Screen

window = Screen()
window.bgcolor('green')
window.title('Ball Game -EURO 2024-')

pitch_line = Turtle()
pitch_line.color('white') 
pitch_line.pensize(5)
pitch_line.speed(0)
pitch_line.hideturtle()
#pitch
pitch_line.goto(0, -1)
pitch_line.circle(5)
pitch_line.goto(0, -81)
pitch_line.circle(90)
pitch_line.goto(0,300)
pitch_line.goto(0,-300)
pitch_line.up()
pitch_line.goto(400,300)
pitch_line.down()
pitch_line.goto(400,-300)
pitch_line.goto(-400,-300)
pitch_line.goto(-400,300)
pitch_line.goto(400,300)

#gate1
gate1 = Turtle()
gate1.speed(0)
gate1.hideturtle()
gate1.color('yellow')
gate1.pensize(5)
gate1.up()
gate1.goto(-400,66)
gate1.down()
gate1.goto(-400,-66)
gate1.goto(-420,-66)
gate1.goto(-420,66)
gate1.goto(-400,66)

#gate2
gate2 = Turtle()
gate2.speed(0)
gate2.hideturtle()
gate2.color('yellow')
gate2.pensize(5)
gate2.up()
gate2.goto(400,66)
gate2.down()
gate2.goto(400,-66)
gate2.goto(420,-66)
gate2.goto(420,66)
gate2.goto(400,66)

#ball
ball = Turtle()
ball.shape('circle')
ball.color('red')

#logic of Game
step_x = 3
step_y = 2
while True:
    x, y = ball.position()
    if x + step_x >= 400 or x + step_x <= -400:
        step_x = -step_x
    if y + step_y >= 300 or y + step_y <= -300:
        step_y = -step_y
    
#window display ALWAYS
window.mainloop()






