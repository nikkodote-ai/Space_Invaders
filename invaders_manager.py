import turtle as t
import random

COLORS = ['green', 'blue', 'purple','red', 'orange', 'yellow', ]

class Invaders_Manager():
    def __init__(self):
        self.all_invaders = []
        self.all_invaders_attacks = []
        #limit enemy movement
        self.paces = 0
        self.go_right = True

    def create_invaders(self, startx ,start_y, i):
        new_invader = t.Turtle('turtle')
        new_invader.right(90)
        new_invader.color('green')
        new_invader.penup()
        new_invader.speed(0)
        y_position = start_y
        x_position = startx + (i * 70)
        new_invader.goto(x_position, y_position)
        self.all_invaders.append(new_invader)

    def invader_attack(self, x, y):
        # create ball
        attack = t.Turtle()
        attack.speed('fast')
        attack.shape('triangle')
        attack.color('red')
        attack.penup()
        attack.goto(x, y)
        self.all_invaders_attacks.append(attack)

    def shot(self,invader):
        x = invader.xcor()
        y = invader.ycor()
        if self.paces == random.randint(0,4000):
            self.invader_attack(x,y)

    def no_invaders(self):
        if self.all_invaders == []:
            return True
        else:
            False

    def create_colony(self, level):
        for i in range(9):
            for j in range(level):
                self.create_invaders(-300, 250 - 40 * j, i)
