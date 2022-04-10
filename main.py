import turtle as t

from bullet_manager import Bullet_Manager
from invaders_manager import Invaders_Manager
from scoreboard import ScoreBoard

playerA_score = 0
playerB_score = 0

window = t.Screen()
window.title("BreakOut Game")
window.bgcolor('black')
window.setup(width=800, height=600)
window.tracer(0, 0)
window.delay(0)

invaders_manager = Invaders_Manager()
bullet_manager = Bullet_Manager()
scoreboard = ScoreBoard()

# make invaders objects


# create invaders
for i in range(9):
    for j in range(1):
        invaders_manager.create_invaders(-300, 250 - 40 * j, i)

# create paddle
paddle = t.Turtle()
paddle.speed(0)
paddle.shape('square')
paddle.color('blue')
paddle.shapesize(stretch_len=2)
paddle.penup()
paddle.goto(0, -200)


# create scorecard update


def paddle_right():
    x = paddle.xcor()
    x += 40
    paddle.setx(x)


def paddle_left():
    x = paddle.xcor()
    x -= 40
    paddle.setx(x)


def player_shot(player):
    x = player.xcor()
    y = player.ycor()
    if len(bullet_manager.all_bullets) < bullet_manager.bullet_limit:
        bullet_manager.create_bullet(x, y)


def collision():
    pass


def updatescore():
    pass


window.listen()
window.onkey(paddle_right, 'Right')
window.onkey(paddle_left, 'Left')
window.onkey(lambda x=paddle: player_shot(x), 'space')

continue_game = True
while continue_game:
    window.update()
    # time.sleep(0.0000000000000001)
    # move bullets
    if len(bullet_manager.all_bullets):
        for bullet in bullet_manager.all_bullets:
            bullet.sety(bullet.ycor() + 0.5)
            if bullet.ycor() > 400:
                bullet_manager.all_bullets.remove(bullet)
                bullet.hideturtle()

    if len(invaders_manager.all_invaders_attacks):
        for attack in invaders_manager.all_invaders_attacks:
            attack.sety(attack.ycor() - 0.5)

    # move invaders
    if invaders_manager.go_right:
        for invader in invaders_manager.all_invaders:
            invader.setx(invader.xcor() + 0.2)
            invaders_manager.paces += 0.5
            invaders_manager.shot(invader)
            if invaders_manager.paces > 1800:
                invaders_manager.go_right = False
    else:
        for invader in invaders_manager.all_invaders:
            invader.setx(invader.xcor() - 0.2)
            invaders_manager.paces -= 0.5
            invaders_manager.shot(invader)
            if invaders_manager.paces < 1:
                invaders_manager.go_right = True
    t.delay(50)

    # check player shot an invader
    for bullet in bullet_manager.all_bullets:
        for invader in invaders_manager.all_invaders:
            if bullet.distance(invader) < 20:
                invaders_manager.all_invaders.remove(invader)
                invader.hideturtle()
                try:
                    bullet_manager.all_bullets.remove(bullet)
                except:
                    pass
                bullet.hideturtle()
                scoreboard.add_score()
                if invaders_manager.no_invaders():
                    scoreboard.level += 1
                    invaders_manager.create_colony(scoreboard.level)
                # update_score

    # if player got hit
    for attack in invaders_manager.all_invaders_attacks:
        if attack.distance(paddle) < 20:
            # game over sequence
            scoreboard.game_over()
            continue_game = False

window.exitonclick()
