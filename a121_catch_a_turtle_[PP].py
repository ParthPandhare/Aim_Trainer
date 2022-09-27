# a121_catch_a_turtle.py
#-----import statements-----

import turtle as trtl
import random as rand
import leaderboard as lb

#-----game configuration----

# leaderboard variables
leaderboard_file_name = "a122_leaderboard.txt"
player_name = input ("Please enter your name:")

color = ["pink", 'green', 'red', 'black', 'blue']
shape = ["circle", 'triangle', 'arrow', 'square', 'turtle', 'classic']
size = 2

score = 0

#-----initialize turtle-----

turtle = trtl.Turtle()
score_writer = trtl.Turtle()
counter = trtl.Turtle()

turtle.shape('circle')
turtle.color('pink')
turtle.shapesize(size)
turtle.penup()

score_writer.penup()
score_writer.hideturtle()
score_writer.goto(350, 370)
font_setup = ("Arial", 20, "normal")

counter.hideturtle()
counter.penup()
counter.goto(-50, 370)

timer = 30
counter_interval = 1000
timer_up = False

#-----game functions--------

# manages the leaderboard for top 5 scorers
def manage_leaderboard():

    global score
    global turtle

    # get the names and scores from the leaderboard file
    leader_names_list = lb.get_names(leaderboard_file_name)
    leader_scores_list = lb.get_scores(leaderboard_file_name)

    # show the leaderboard with or without the current player
    if (len(leader_scores_list) < 5 or score >= leader_scores_list[4]):
        lb.update_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list, player_name, score)
        lb.draw_leaderboard(True, leader_names_list, leader_scores_list, turtle, score)

    else:
        lb.draw_leaderboard(False, leader_names_list, leader_scores_list, turtle, score)

def spot_clicked(x, y):
    global timer
    if (timer_up == False):
        update_score()
        change_position()
        change_turtle()
        wn.update()
    elif(timer == True):
        turtle.hideturtle()
        wn.update()

def change_position():
    new_xpos = rand.randint(-475, 475)
    new_ypos = rand.randint(-400, 400)

    turtle.hideturtle()
    turtle.goto(new_xpos, new_ypos)
    turtle.showturtle()

def update_score():
    global score
    score += 1
    score_writer.clear()
    score_writer.write("Score: " + str(score), font=font_setup)

def countdown():
    global timer, timer_up
    counter.clear()
    if timer <= 0:
        counter.write("Time's Up", font=font_setup)
        timer_up = True
        manage_leaderboard()
        wn.update()
    else:
        counter.write("Timer: " + str(timer), font=font_setup)
        timer -= 1
        counter.getscreen().ontimer(countdown, counter_interval)
        wn.update() 

def change_turtle():
    turtle.shape(rand.choice(shape))
    turtle.color(rand.choice(color))
    turtle.shapesize(rand.randint(2, 5))
    turtle.setheading(rand.randint(0, 360))

#-----events----------------
turtle.onclick(spot_clicked)

wn = trtl.Screen()

wn.ontimer(countdown, counter_interval)

wn.bgcolor("lime green")

wn.tracer(0)
wn.mainloop()