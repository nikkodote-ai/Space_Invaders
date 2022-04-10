import turtle as t

class Bullet_Manager():
    def __init__(self):
        self.all_bullets= []
        self.bullet_limit = 4

    def create_bullet(self, x, y):
        # create ball
        bullet = t.Turtle()
        bullet.speed('fast')
        bullet.shape('circle')
        bullet.color('white')
        bullet.penup()
        bullet.goto(x,y)
        self.all_bullets.append(bullet)



