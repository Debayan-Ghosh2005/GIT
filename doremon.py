import turtle as t

# Set up the Turtle screen
t.bgcolor("white")
t.title("Doraemon and Nobita")

# Function to draw a filled circle
def draw_circle(color, radius, x, y):
    t.penup()
    t.fillcolor(color)
    t.goto(x, y)
    t.pendown()
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

# Function to draw Doraemon's face
def draw_doraemon_face():
    draw_circle("#00a0de", 80, 0, -100)
    draw_circle("white", 30, -25, 20)
    draw_circle("white", 30, 25, 20)

# Function to draw Doraemon's eyes
def draw_doraemon_eye(x, y):
    draw_circle("white", 15, x, y)
    draw_circle("black", 6, x, y)

# Function to draw Doraemon's nose
def draw_doraemon_nose(x, y):
    draw_circle("red", 6, x, y)

# Function to draw Doraemon's mouth
def draw_doraemon_mouth(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.setheading(-60)
    t.circle(20, 120)
    t.setheading(0)
    t.circle(-20, 120)

# Function to draw Nobita's face
def draw_nobita_face():
    draw_circle("pink", 60, -130, -100)

# Function to draw Nobita's eyes
def draw_nobita_eye(x, y):
    draw_circle("white", 15, x, y)
    draw_circle("black", 6, x, y)

# Draw Doraemon's face
draw_doraemon_face()

# Draw Doraemon's eyes
draw_doraemon_eye(-20, 60)
draw_doraemon_eye(20, 60)

# Draw Doraemon's nose
draw_doraemon_nose(0, 40)

# Draw Doraemon's mouth
draw_doraemon_mouth(0, 10)

# Draw Nobita's face
draw_nobita_face()

# Draw Nobita's eyes
draw_nobita_eye(-160, 20)
draw_nobita_eye(-100, 20)

# Hide the Turtle cursor
t.hideturtle()

# Close the Turtle graphics window when clicked
t.exitonclick()
