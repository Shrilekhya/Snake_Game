import pygame
import random

pygame.mixer.init()
pygame.init()

#Defining colors with  their rgb values
white = (255,255,255)
red = (255,0,0)
black = (0,0,0)

#Creating game window
screen_width = 900
screen_height = 600

gameWindow = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("SnakesBySasi")
font = pygame.font.SysFont(None, 55)


#Creating clock as we need to update the frames of the game according to some time
clock = pygame.time.Clock()

def text_screen(text, color, x, y):
      screen_text = font.render(text, True, color)
      gameWindow.blit(screen_text , [x,y])

def plot_snake(gameWindow, color, list, size):
      for x,y in list:
       pygame.draw.rect(gameWindow, black, [x, y, size, size]) 


def welcome():
      exit_game = False
      while not exit_game:
            gameWindow.fill(white)
            text_screen("Lets play Snakes",black,250,200)
            text_screen("Click Enter to start the game",red,200,250)
            for event in pygame.event.get():
                  if event.type == pygame.QUIT:
                        exit_game = True
                  
                  if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                              pygame.mixer.music.load('song1.mp3')
                              pygame.mixer.music.play()
                              gameLoop()

            pygame.display.update()
            clock.tick(30)


#Creating game loop
def gameLoop():
      #Creating game specific variables
      exit_game = False
      game_over = False
      snake_x = 100
      snake_y = 100
      velocity_x = 0
      velocity_y = 0

      init_v = 4

      score = 0
      snk_list = []
      snk_length = 1

      food_x = random.randint(0,screen_width)
      food_y = random.randint(0,screen_height)

      snake_size = 20
      fps = 30  #fps is frames per second so here we need 30 frames in 1 sec
      while not exit_game:
            if(game_over):
                  gameWindow.fill(white)
                  text_screen("Game Over, Press Enter to restart",red , screen_width/5 , screen_height/3 )
                  for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                              exit_game = True

                        if event.type == pygame.KEYDOWN:
                              gameLoop()

            else:
                  for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                              exit_game = True

                        if event.type == pygame.KEYDOWN:
                              if event.key == pygame.K_RIGHT:
                                    velocity_x = init_v 
                                    velocity_y = 0        # We make 1 velocity 0 so that snake doesnt go diagonally
                              
                              if event.key == pygame.K_LEFT:
                                    velocity_x = -init_v 
                                    velocity_y = 0

                              if event.key == pygame.K_UP:
                                    velocity_y = -init_v 
                                    velocity_x = 0

                              if event.key == pygame.K_DOWN:
                                    velocity_y = init_v 
                                    velocity_x = 0

                  snake_x += velocity_x
                  snake_y += velocity_y

                  if(abs(snake_x - food_x)<6 and abs(snake_y - food_y)<6):  # ie if food and snake come to proximity then increase score and change the position of food
                        score += 10
                        food_x = random.randint(20,screen_width/2)
                        food_y = random.randint(20,screen_height/2)
                        snk_length += 5


                  gameWindow.fill(white)  #here we are filling the entire screen with white color
                  text_screen("Score: " + str(score), red, 10, 10 )  #calling function to print score on screen
                  
                  head = []
                  head.append(snake_x)
                  head.append(snake_y)
                  snk_list.append(head)

                  if(len(snk_list) > snk_length):
                        del snk_list[0]
                  
                  if head in snk_list[:-1]:   #head is the last element .. so if the head's coordinates match with any other coordinates the game over
                        game_over=True
                        pygame.mixer.music.load('gameOver.mp3')
                        pygame.mixer.music.play()

                  if(snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height):
                        game_over=True
                        pygame.mixer.music.load('gameOver.mp3')
                        pygame.mixer.music.play()

                  pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])
                  # (surface to draw, color, [x position, y position, width, height])

                  plot_snake(gameWindow,red, snk_list, snake_size)
                  #pygame.draw.rect(gameWindow, black, [snake_x, snake_y, snake_size, snake_size])  


            pygame.display.update() #here we update our changes
            clock.tick(fps)  #inside while loop what ever is there that is one frame and we wish to update it 30 times in 1 sec



      pygame.quit()
      quit()

welcome()
