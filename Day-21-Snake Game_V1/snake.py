from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.boxes = []
        self.create_snake()
        self.snake_head = self.boxes[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_box(position)

    def reset_snake(self):
        for box in self.boxes:
            box.goto(1000, 1000)
        self.boxes.clear()
        self.create_snake()
        self.snake_head = self.boxes[0]

    def add_box(self, position):
        new_box = Turtle()
        new_box.shape("square")
        new_box.color('white')
        new_box.penup()
        new_box.goto(position)
        self.boxes.append(new_box)


    def extend(self):
        self.add_box(self.boxes[-1].position())



    def move(self):
        for box_num in range(len(self.boxes) - 1, 0, -1):
            new_x = self.boxes[box_num - 1].xcor()
            new_y = self.boxes[box_num - 1].ycor()
            self.boxes[box_num].goto(new_x, new_y)
        self.snake_head.forward(MOVE_DISTANCE)

    def up(self):
        if self.snake_head.heading() != DOWN:
            self.snake_head.setheading(UP)

    def down(self):
        if self.snake_head.heading() != UP:
            self.snake_head.setheading(DOWN)

    def left(self):
        if self.snake_head.heading() != RIGHT:
            self.snake_head.setheading(LEFT)

    def right(self):
        if self.snake_head.heading() != LEFT:
            self.snake_head.setheading(RIGHT)