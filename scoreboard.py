from turtle import Turtle
ALIGN = "center"
FONT = ("Courier", 24, "normal")

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read()) 
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0,260)
        self.refresh_board()


    def score_up(self):
        self.score += 1  
        self.refresh_board()  

    def refresh_board(self):
         self.clear()
         self.write(f"Score : {self.score} High score : {self.high_score}", align= ALIGN, font= FONT)    
         
    def game_over(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                    data.write(f"{self.high_score}")

        self.home()
        self.write(f"GAME OVER", align= ALIGN, font= FONT) 
        