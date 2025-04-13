from turtle import Turtle


STARTING_POSITION: list[tuple[int, int]] = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
HEAD_COLOR = "green"
BODY_COLOR = "darkgreen"

class Snake:


    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
    def create_snake(self):
        for position in STARTING_POSITION:

            self.add_segment(position)

    def move(self):

        for box_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[box_num - 1].xcor()
            new_y = self.segments[box_num - 1].ycor()
            self.segments[box_num].goto(new_x, new_y)

        self.head.forward(MOVE_DISTANCE)

    def add_segment(self,position):
        new_segment = Turtle("circle")
        new_segment.color("red")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]


    def extend(self):
        # Add a new segment to the snake.
        self.add_segment(self.segments[-1].position())

    def Up(self):
        self.segments[0].setheading(90)
    def Down(self):
        self.segments[0].setheading(270)
    def Left(self):
        self.segments[0].setheading(180)
    def Right(self):
        self.segments[0].setheading(0)
