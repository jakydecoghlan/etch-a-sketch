from turtle import Turtle, Screen

rafael = Turtle()
screen = Screen()
rafael.shape("turtle")
rafael.color("red")

def move_forwards():
    rafael.forward(10)
def move_backwards():
    rafael.backward(10)
def turn_right():
    rafael.right(10)
def turn_left():
    rafael.left(10)
def clear_screen ():
    rafael.clear()


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=clear_screen)
screen.exitonclick()
