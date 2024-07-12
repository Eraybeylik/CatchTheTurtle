import turtle
import random

# Screen
gameWindow = turtle.Screen()
gameWindow.title("Catch The Turtle")
gameWindow.bgcolor("light blue")
gameWindow.setup(width=600, height=600)


# Creating Frog
frog = turtle.Turtle()
frog.shape("turtle")
frog.color("green")
frog.penup()
frog.speed(0)

# Score
score = 0
scoreDisplay = turtle.Turtle()
scoreDisplay.color("white")
scoreDisplay.hideturtle()
scoreDisplay.penup()
scoreDisplay.goto(0, 260)
scoreDisplay.write("Score: 0", align="center", font=("Arial", 24, "normal"))

# Timer
timeLimit = 30
timerDisplay = turtle.Turtle()
timerDisplay.color("white")
timerDisplay.hideturtle()
timerDisplay.penup()
timerDisplay.goto(0, 230)
timerDisplay.write("Time: 30", align="center", font=("Arial", 24, "normal"))

# Frog Movement
def moveFrog():
    x = random.randint(-290, 290)
    y = random.randint(-290, 290)
    frog.goto(x, y)
    gameWindow.ontimer(moveFrog, 750)


# İncrease score
def increaseScore(x, y):
    global score
    score += 1
    scoreDisplay.clear()
    scoreDisplay.write(f"Score: {score}", align="center", font=("Arial", 24, "normal"))

# Timer
def countdown(time):
    if time > 0:
        timerDisplay.clear()
        timerDisplay.write(f"Time: {time}", align="center", font=("Arial", 24, "normal"))
        gameWindow.ontimer(lambda: countdown(time - 1), 1000)
    else:
        frog.hideturtle()
        timerDisplay.clear()
        timerDisplay.write("Time is up!", align="center", font=("Arial", 24, "normal"))

# Game Start
frog.onclick(increaseScore)
moveFrog()
countdown(timeLimit)

gameWindow.mainloop()