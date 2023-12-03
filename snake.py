from turtle import Turtle

STRING_POSITION = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20

class Snake:
    def __init__(self):
        self.segments =[]
        self.createSnake()
        self.head = self.segments[0]
        self.speed = MOVE_DISTANCE

    def createSnake(self):
         for position in STRING_POSITION:
            self.addSegment(position)
        
    def addSegment(self,position):
         new_segmant = Turtle()
         new_segmant.shape("square")
         new_segmant.color("white")
         new_segmant.penup()
         new_segmant.goto(position)
         self.segments.append(new_segmant)


    def moveUp(self):
         if(self.head.heading() != 270): 
            self.head.setheading(90)

    def moveDown(self):
         if(self.head.heading() != 90): 
            self.head.setheading(270)

    def moveLeft(self):
         if(self.head.heading() != 0): 
            self.head.setheading(180)

    def moveRight(self):
         if(self.head.heading() != 180): 
            self.head.setheading(0)

    def move(self):
         for seg_num in range(len(self.segments)-1,0,-1):
            new_x = self.segments[seg_num-1].xcor()
            new_y = self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(new_x,new_y)
         self.head.forward(self.speed)

    def x_HeadSnake(self):
        return self.head.xcor()
    
    def y_HeadSnake(self):
        return self.head.ycor()

    def eaten(self):
        new_segmant = Turtle()
        new_segmant.shape("square")
        new_segmant.color("white")
        new_segmant.penup()
        new_segmant.goto(self.segments[len(self.segments)-1].xcor(),self.segments[len(self.segments)-1].ycor())
        new_segmant.speed("fastest")
        self.segments.append(new_segmant)

    def touchHimself(self) -> bool:
      for seg_num in range(len(self.segments)-1,0,-1):
        if self.head.distance(self.segments[seg_num]) < 10:
            pass
        if self.head.distance(self.segments[seg_num]) < 10:
            return True
        
    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.createSnake()
        self.head = self.segments[0]
    
    def speedUp(self):
        self.speed = MOVE_DISTANCE + 1

       