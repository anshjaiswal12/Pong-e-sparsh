#the following code is written by me Ansh jaiswal if you find any problem inbox me on instagram my id:arthjaiswal_12
import turtle #importing the turtle module from python
import winsound

wn = turtle.Screen()#made the turtle screen appear
wn. title("The Sparsh -Pong")#here is the title of the game
wn.bgcolor("black")#here is the background color of the game
wn.setup(width=800,height=600)#setting width and height of the screen 
wn.tracer(0)#this stops the window from updating becuase we later update it manually with wn.update() code



#scores
score_a=0
score_b=0


#ADDING Paddles and ball

#Paddle A
paddle_a = turtle.Turtle() #we are making turtle appear on the screen with the below given characterstics
paddle_a.speed(0)#we are going to set speed externaly not internally so we setit 0 at default
paddle_a.shape("square")#we are goig to give a shape to the tutrle
paddle_a.color("white")#we are giving it a color
paddle_a.penup()#this stops the tutle to create a line ,because that is its basic nature
paddle_a.goto(-350,0)#it will start from the following place
paddle_a.shapesize(stretch_wid=5,stretch_len=1)#we are creating a specific space 
#Paddle B
paddle_b = turtle.Turtle() #we are making turtle appear on the screen with the below given characterstics
paddle_b.speed(0)#we are going to set speed externaly not internally so we setit 0 at default
paddle_b.shape("square")#we are goig to give a shape to the tutrle
paddle_b.color("red")#we are giving it a color
paddle_b.penup()#this stops the tutle to create a line ,because that is its basic nature
paddle_b.goto(350,0)#it will start from the following place
paddle_b.shapesize(stretch_wid=5,stretch_len=1)#we are creating a specific space 

#adding ball to the game
ball = turtle.Turtle() #we are making turtle appear on the screen with the below given characterstics
ball.speed(0)#we are going to set speed externaly not internally so we setit 0 at default
ball.shape("square")#we are goig to give a shape to the tutrle
ball.color("grey")#we are giving it a color
ball.penup()#this stops the tutle to create a line ,because that is its basic nature
ball.goto(0,0)#it will start from the following place 
ball.dx=1
ball.dy=-1




#pen
pen=turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)





#Functions
def paddle_a_up():
	y=paddle_a.ycor()
	y+=20
	paddle_a.sety(y)

def paddle_a_down():
	y=paddle_a.ycor()
	y-=20
	paddle_a.sety(y)



def paddle_b_up():
	y=paddle_b.ycor()
	y+=20
	paddle_b.sety(y)

def paddle_b_down():
	y=paddle_b.ycor()
	y-=20
	paddle_b.sety(y)
#Keyboard Reaction

wn.listen()
wn.onkeypress(paddle_a_up,"w")
wn.onkeypress(paddle_a_down,"s")
wn.onkeypress(paddle_b_up,"Up")
wn.onkeypress(paddle_b_down,"Down")


#primary loop of the game where the game works 
while True:
	wn.update()
	ball.setx(ball.xcor() + ball.dx)
	ball.sety(ball.ycor() + ball.dy)

	#Border checking
	if ball.ycor() >280:
		ball.sety(280)
		ball.dy*=-1
		winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)

	if ball.ycor() <-280:
		ball.sety(-280)
		ball.dy*=-1
		winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)
		

	if ball.xcor() >389:
		ball.goto(0,0)
		ball.dx*=-1
		score_a+=1
		pen.clear()
		pen.write("Player A:{} Player B:{}".format(score_a,score_b),align ="center",font=("Courier",24,"normal"))
	if ball.xcor() <-389:
		ball.goto(0,0)
		ball.dx*=-1
		score_b+=1
		pen.clear()
		pen.write("Player A:{} Player B:{}\n An Ansh Jaiswal production".format(score_a,score_b),align ="center",font=("Courier",24,"normal"))



	#paddle and ball collission
	if (ball.xcor() > 340 and ball.xcor() <350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() -40):
		ball.setx(340)
		ball.dx*=-1

	if (ball.xcor() <- 340 and ball.xcor() >-350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() -40):
		ball.setx(-340)
		ball.dx*=-1


