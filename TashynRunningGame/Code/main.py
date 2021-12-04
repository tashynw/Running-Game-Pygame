import pygame
import random
import sys
from pygame import mixer


#initialize pygame
pygame.init()


#create the screen
screen=pygame.display.set_mode((800,800))


#Title and Icon
pygame.display.set_caption("Tashyn Runnning Game")
icon=pygame.image.load("images/icon.png")
pygame.display.set_icon(icon)

#background audience (left)
audiencebackground=pygame.image.load('images/audience.png')
audience_lefty=30

#background audience(right)
audiencebackground_right=pygame.image.load('images/audience2.png')
audience_righty=30



#Function to place title on the screen(permanent)
title=pygame.font.SysFont("Arial",40)
def titletext():
	title_text=title.render("Running Game",True, (102,255,102))
	screen.blit(title_text,(305,20))

#Function to place score board on the screen
score_title=pygame.font.SysFont("Arial",40)
def scoreboard():
	title_text=score_title.render(f"Score: {round(score,2)}",True, (102,255,102))
	screen.blit(title_text,(305,350))

#Function to output score after winning
score_text=pygame.font.SysFont("Arial",20)
def scoreoutput():
	title_text=score_text.render(f"Your Score is {round(score,2)}",True, (102,255,102))
	screen.blit(title_text,(305,350))


#Button classes
main_font = pygame.font.SysFont("cambria", 50)

#Start Button
class Button():
	def __init__(self, image, x_pos, y_pos, text_input):
		self.image = image
		self.x_pos = x_pos
		self.y_pos = y_pos
		self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
		self.text_input = text_input
		self.text = main_font.render(self.text_input, True, "white")
		self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

	def update(self):
		screen.blit(self.image, self.rect)
		screen.blit(self.text, self.text_rect)

	def checkForInput(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			maingameloop()

	def changeColor(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			self.text = main_font.render(self.text_input, True, "green")
		else:
			self.text = main_font.render(self.text_input, True, "white")


#Close Button
class Button_Close():
	def __init__(self, image, x_pos, y_pos, text_input):
		self.image = image
		self.x_pos = x_pos
		self.y_pos = y_pos
		self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
		self.text_input = text_input
		self.text = main_font.render(self.text_input, True, "white")
		self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

	def update(self):
		screen.blit(self.image, self.rect)
		screen.blit(self.text, self.text_rect)

	def checkForInput(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			pygame.quit()
			sys.exit()

	def changeColor(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			self.text = main_font.render(self.text_input, True, "green")
		else:
			self.text = main_font.render(self.text_input, True, "white")




button_surface = pygame.image.load("images/button.png")
button_surface = pygame.transform.scale(button_surface, (200, 100))

button = Button(button_surface, 240, 600, "Start")
close_button= Button_Close(button_surface, 550, 600, "Close")

refresh_button = Button(button_surface, 240, 600, "Restart")

#Functions to display start page

startpage=pygame.font.SysFont("Arial",100)
def starttext():
	start_text=title.render("THIS IS MY START PAGE I AM TESTING!",True, (102,255,102))
	screen.blit(start_text,(400,300))



def startloop():

	start_status=True

	state=0
	while start_status:

		mouse=pygame.mouse.get_pos()

		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				pygame.quit()
				sys.exit()

			#Logic to perform functions when the buttons on start page are clicked
			if event.type==pygame.MOUSEBUTTONDOWN:
				button.checkForInput(mouse)
				close_button.checkForInput(mouse)
			

		button.update()
		button.changeColor(mouse)

		close_button.update()
		close_button.changeColor(mouse)
		
		instructions=pygame.font.SysFont("Arial",20)
		title_text=instructions.render("Click the arrow keys repeatedly in order to move your character",True, (102,205,80))
		
		screen.blit(title_text,(170,400))
		title_text2=instructions.render("Click the Start Button when ready",True, (102,205,80))
		screen.blit(title_text2,(250,450))
		
			
		pygame.display.update()



def maingameloop():
	
	#backgroundpics(the running lanes)
	background1=pygame.image.load('images/backgroundtrack(lane1).png')
	background2=pygame.image.load('images/backgroundtrack(lane2).png')

	#background audience (left)
	audiencebackground=pygame.image.load('images/audience.png')
	audience_lefty=30

	#background audience(right)
	audiencebackground_right=pygame.image.load('images/audience2.png')
	audience_righty=30

	
	#backgroundmusic

	pygame.mixer.init()
	mixer.music.load('audio/background.wav')
	mixer.music.play(-1)
	

	#Runner(user player)
	runnerimg=pygame.image.load("images/runner.png")
	runnerx=120
	runnery=645
	runnery_change=0

	#Runner (ENEMY player)
	enemyrunnerimg=pygame.image.load("images/runner.png")
	enemyrunnerx=610
	enemyrunnery=645
	enemyrunnerychange=random.uniform(0.15,0.25)

	#functions to load characters unto screen
	def runner(x,y):
		screen.blit(runnerimg,(x,y))

	def enemyrunner(x,y):
		screen.blit(enemyrunnerimg,(x,y))


	#Function to place title on the screen(permanent)
	title=pygame.font.SysFont("Arial",40)
	def titletext():
		title_text=title.render("Running Game",True, (102,255,102))
		screen.blit(title_text,(305,20))



	
	running=True
	#clear the screen to start fresh
	screen.fill((255,255,255))
	global score
	score=0

	statelst=[]
	statelst2=[]
	
	
	while running:

		#clear the screen to start fresh
		screen.fill((204,102,0))
		
		#background images loader(2 track lanes)
		screen.blit(background1,(100,3))
		screen.blit(background2,(600,0))


		score+=0.0065
		scoreboard()

		#Background spectators (loading 10 distance y apart)

		#spectators on the left
		
		screen.blit(audiencebackground,(10,audience_lefty))
		screen.blit(audiencebackground,(10,audience_lefty+100))
		screen.blit(audiencebackground,(10,audience_lefty+200))
		screen.blit(audiencebackground,(10,audience_lefty+300))
		screen.blit(audiencebackground,(10,audience_lefty+400))
		screen.blit(audiencebackground,(10,audience_lefty+500))
		screen.blit(audiencebackground,(10,audience_lefty+600))
		screen.blit(audiencebackground,(10,audience_lefty+700))
		
		#spectators on the right
		screen.blit(audiencebackground_right,(730,audience_righty))
		screen.blit(audiencebackground_right,(730,audience_righty+100))
		screen.blit(audiencebackground_right,(730,audience_righty+200))
		screen.blit(audiencebackground_right,(730,audience_righty+300))
		screen.blit(audiencebackground_right,(730,audience_righty+400))
		screen.blit(audiencebackground_right,(730,audience_righty+500))
		screen.blit(audiencebackground_right,(730,audience_righty+600))
		screen.blit(audiencebackground_right,(730,audience_righty+700))

		#place title on the screen
		titletext()


		#Gameover script
		if enemyrunnery<=0:
			#Complete script!
			gameoverscreen_lost()
		elif runnery<=0:
			#Complete script!
			gameoverscreen_win()
		
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				running=False
				pygame.quit()
				sys.exit()

			#Binding left and right arrow keys to move character up the screen
			
			if event.type==pygame.KEYDOWN:
				if len(statelst)>8 or len(statelst2)>8:
					if event.key==pygame.K_LEFT:
						runnery_change=0

					if event.key==pygame.K_RIGHT:
						runnery_change=0

				else:

					if event.key==pygame.K_LEFT:
						runnery_change=0.45

					if event.key==pygame.K_RIGHT:
						runnery_change=0.45

					
			if event.type==pygame.KEYUP:
				if event.key==pygame.K_RIGHT or event.key==pygame.K_LEFT:
					runnery_change = 0
					statelst=[]
					statelst2=[]
	
		#To prevent user from cheating by holding down the arrow key

		if pygame.key.get_pressed()[pygame.K_LEFT]:
			statelst.append(pygame.key.get_pressed()[pygame.K_LEFT])
			
		if pygame.key.get_pressed()[pygame.K_RIGHT]:
			statelst2.append(pygame.key.get_pressed()[pygame.K_LEFT])
			
		
		if len(statelst)>50 or len(statelst2)>50:
			runnery_change=0


		#Logic to move characters up the screen
		runnery-=runnery_change
		enemyrunnery-=enemyrunnerychange


		#Loading back characters unto screen		
		runner(runnerx,runnery)
		enemyrunner(enemyrunnerx,enemyrunnery)


		pygame.display.update()


#Functions to display gameover screen

#If user has won
def gameoverscreen_win():

	start_status=True

	state=0
	screen.fill((204,102,0))

	
	while start_status:

		mouse=pygame.mouse.get_pos()

		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				pygame.quit()
				sys.exit()

			#Logic to perform functions when the buttons on page are clicked
			if event.type==pygame.MOUSEBUTTONDOWN:
				close_button.checkForInput(mouse)
				refresh_button.checkForInput(mouse)


		
		instructions=pygame.font.SysFont("Arial",20)
		title_text=instructions.render("You win!",True, (102,205,80))
		
		screen.blit(title_text,(350,400))
		title_text2=instructions.render("Click the restart button or quit",True, (102,205,80))
		screen.blit(title_text2,(270,450))

		scoreoutput()

		refresh_button.update()
		refresh_button.changeColor(pygame.mouse.get_pos())

		close_button.update()
		close_button.changeColor(pygame.mouse.get_pos())

			
		pygame.display.update()



def gameoverscreen_lost():
	start_status=True

	state=0
	screen.fill((204,102,0))
	while start_status:

		mouse=pygame.mouse.get_pos()

		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				pygame.quit()
				sys.exit()

			#Logic to perform functions when the buttons on start page are clicked
			if event.type==pygame.MOUSEBUTTONDOWN:
				close_button.checkForInput(mouse)
				refresh_button.checkForInput(mouse)

		
		instructions=pygame.font.SysFont("Arial",20)
		title_text=instructions.render("You lost!",True, (102,205,80))
		
		screen.blit(title_text,(350,400))
		title_text2=instructions.render("Click the restart button or quit",True, (102,205,80))
		screen.blit(title_text2,(270,450))

		refresh_button.update()
		refresh_button.changeColor(pygame.mouse.get_pos())

		close_button.update()
		close_button.changeColor(pygame.mouse.get_pos())
			
		pygame.display.update()


#Game Loop

if __name__=="__main__":
	running=True
	while running:
		
		#background color RGB
		screen.fill((204,102,0))

		#Background spectators (loading 10 distance y apart)

		#spectators on the left
		
		screen.blit(audiencebackground,(10,audience_lefty))
		screen.blit(audiencebackground,(10,audience_lefty+100))
		screen.blit(audiencebackground,(10,audience_lefty+200))
		screen.blit(audiencebackground,(10,audience_lefty+300))
		screen.blit(audiencebackground,(10,audience_lefty+400))
		screen.blit(audiencebackground,(10,audience_lefty+500))
		screen.blit(audiencebackground,(10,audience_lefty+600))
		screen.blit(audiencebackground,(10,audience_lefty+700))
		
		#spectators on the right
		screen.blit(audiencebackground_right,(730,audience_righty))
		screen.blit(audiencebackground_right,(730,audience_righty+100))
		screen.blit(audiencebackground_right,(730,audience_righty+200))
		screen.blit(audiencebackground_right,(730,audience_righty+300))
		screen.blit(audiencebackground_right,(730,audience_righty+400))
		screen.blit(audiencebackground_right,(730,audience_righty+500))
		screen.blit(audiencebackground_right,(730,audience_righty+600))
		screen.blit(audiencebackground_right,(730,audience_righty+700))

		#place title on the screen
		titletext()


		startloop()
		
				
		pygame.display.update()