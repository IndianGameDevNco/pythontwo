import turtle, random, time

# Setup the screen
screen = turtle.Screen()
screen.title("Snake Food Collection Game")
screen.bgcolor("khaki")
screen.setup(width=600, height=600)
screen.tracer(0)  # Turn off automatic animation

# Create the snake
snake = turtle.Turtle()
snake.shape('square')
snake.color("black")
snake.penup()  # Don't draw lines when moving
snake.speed(0)  # Fastest animation speed
snake.goto(0, 0)  # Start at center

# Game variables
NUM_FOODS = 10
foods = []
segments = []
caught = [False] * NUM_FOODS
steps = 0
game_over = False
score = 0

# Create boundary
boundary = turtle.Turtle()
boundary.penup()
boundary.hideturtle()
boundary.color("red")
boundary.pensize(2)
boundary.goto(-250, -250)
boundary.pendown()
for _ in range(4):
    boundary.forward(500)
    boundary.left(90)

# Create food
for i in range(NUM_FOODS):
    food = turtle.Turtle()
    food.penup()
    food.speed(0)
    food.shape("circle")
    food.color("blue")
    food.shapesize(0.7)  # Make food slightly smaller
    food.goto(random.randint(-230, 230), random.randint(-230, 230))
    foods.append(food)

# Create score display
score_display = turtle.Turtle()
score_display.penup()
score_display.hideturtle()
score_display.color("black")
score_display.goto(220, 260)

# Create steps display
steps_display = turtle.Turtle()
steps_display.penup()
steps_display.hideturtle()
steps_display.color("black")
steps_display.goto(-220, 260)

# Create message display for center
message = turtle.Turtle()
message.penup()
message.hideturtle()
message.color("green")


# Movement functions
def go_right():
    if snake.heading() != 180:  # Not going left
        snake.setheading(0)


def go_left():
    if snake.heading() != 0:  # Not going right
        snake.setheading(180)


def go_up():
    if snake.heading() != 270:  # Not going down
        snake.setheading(90)


def go_down():
    if snake.heading() != 90:  # Not going up
        snake.setheading(270)


# Keyboard bindings
screen.listen()
screen.onkey(go_right, "Right")
screen.onkey(go_left, "Left")
screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")

# Main game loop
while not game_over:
    screen.update()  # Update the screen

    # Update displays
    score_display.clear()
    score_display.write(f"Score: {score}/{NUM_FOODS}", align="right", font=("Arial", 16, "normal"))

    steps_display.clear()
    steps_display.write(f"Steps: {steps}", align="left", font=("Arial", 16, "normal"))

    # Check for food collection
    for i in range(NUM_FOODS):
        if not caught[i]:
            if snake.distance(foods[i]) < 15:
                caught[i] = True
                foods[i].color('green')
                score += 1

                # Create new segment
                segment = turtle.Turtle()
                segment.speed(0)
                segment.shape("square")
                segment.color("gray")
                segment.penup()
                segments.append(segment)

    # Move segments
    for i in range(len(segments) - 1, 0, -1):
        x = segments[i - 1].xcor()
        y = segments[i - 1].ycor()
        segments[i].goto(x, y)

    # Move first segment to where the snake is
    if segments:
        segments[0].goto(snake.xcor(), snake.ycor())

    # Move the snake
    snake.forward(15)
    steps += 1

    # Check for wall collision
    if (snake.xcor() > 250 or snake.xcor() < -250 or
            snake.ycor() > 250 or snake.ycor() < -250):
        message.goto(0, 0)
        message.color("red")
        message.write("GAME OVER! Hit the wall!", align="center", font=("Arial", 24, "bold"))
        game_over = True

    # Check for win condition - all food collected and back to center
    if score == NUM_FOODS:
        message.goto(0, 30)
        message.write("All food collected!", align="center", font=("Arial", 20, "normal"))
        message.goto(0, -30)
        message.write("Return to center to win", align="center", font=("Arial", 16, "normal"))

        # Check if snake is back at center
        if abs(snake.xcor()) < 20 and abs(snake.ycor()) < 20:
            message.clear()
            message.goto(0, 0)
            message.color("green")
            message.write(f"YOU WIN! Steps taken: {steps}", align="center", font=("Arial", 24, "bold"))
            game_over = True

    time.sleep(0.1)  # Control game speed

# Keep window open until clicked
screen.exitonclick()