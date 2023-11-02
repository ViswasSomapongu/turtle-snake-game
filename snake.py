from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]

class Snake:
    def __init__(self):
        """Initialize the snake object."""
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        """Create the initial segments of the snake."""
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        """Add a new segment to the snake at the specified position."""
        segment = Turtle(shape="square")
        segment.speed("fastest")
        segment.color("white")
        segment.penup()
        segment.goto(position)
        self.segments.append(segment)



    def reset_snake(self):
        for seq in self.segments:
            seq.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
        

    def extend(self):
        """Extend the snake by adding a new segment at the end."""
        self.add_segment(self.segments[-1].position())

    def move(self):
        """Move the snake forward by updating the position of each segment."""
        for seg in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg - 1].xcor()
            new_y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(new_x, new_y)
        self.segments[0].forward(20)

    def snake_up(self):
        """Change the snake's direction to move upwards."""
        if self.head.heading() != 270:
            self.head.setheading(90)

    def snake_down(self):
        """Change the snake's direction to move downwards."""
        if self.head.heading() != 90:
            self.head.setheading(270)

    def snake_left(self):
        """Change the snake's direction to move to the left."""
        if self.head.heading() != 0:
            self.head.setheading(180)

    def snake_right(self):
        """Change the snake's direction to move to the right."""
        if self.head.heading() != 180:
            self.head.setheading(0)
