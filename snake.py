from turtle import Turtle

STARTING_POS = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self) -> None:
        self.segments: list[Turtle] = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for pos in STARTING_POS:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(pos)
            self.segments.append(new_segment)

    def move(self):
        for segment_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[segment_num - 1].xcor()
            new_y = self.segments[segment_num - 1].ycor()
            self.segments[segment_num].goto(new_x, new_y)
        self.head.forward(15)

    def new_segment(self):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        last_seg = self.segments[len(self.segments) - 1]
        if last_seg.heading() == UP:
            coord_x = last_seg.xcor()
            coord_y = last_seg.ycor() - 20
            new_segment.goto(coord_x, coord_y)

        elif last_seg.heading() == DOWN:
            coord_x = last_seg.xcor()
            coord_y = last_seg.ycor() + 20
            new_segment.goto(coord_x, coord_y)

        elif last_seg.heading() == RIGHT:
            coord_x = last_seg.xcor() - 20
            coord_y = last_seg.ycor()
            new_segment.goto(coord_x, coord_y)

        elif last_seg.heading() == LEFT:
            coord_x = last_seg.xcor() + 20
            coord_y = last_seg.ycor()
            new_segment.goto(coord_x, coord_y)

        self.segments.append(new_segment)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
