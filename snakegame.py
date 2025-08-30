                                                    #      SNAKE GAME
# Python project                                              
# NAME : ARYAN PRASHER 
# SAP : 500125413
# BATCH : 50
# E-mail: aryan.125413@stu.upes.ac.in

from tkinter import*
import random
# Here we are declaring the constants which can be used throughout the programs 
GAME_WIDTH = 700
GAME_HEIGHT = 700

SPEED = 150

SPACE_SIZE= 50

BODY_PARTS = 3

SNAKE_COLOR ="#00ff00"

FOOD_COLOR ="#D1233B"

BACKGROUND_COLOR = "#A6FF96"

class Snake:
    def __init__(self): #init (self )  this is used to make an object snake 
        # give the snake size >> them declare the coordinates >>> then using coordinates declare the squares used in the snake 
        self.body_size=BODY_PARTS 
        self.coordinates = []
        self.squares=[]
        
        for i in range (0,BODY_PARTS):  # this is used to make the snake appear in a desired positon [0,0] means top left 
            self.coordinates.append([0,0])  # [0,0] coordinates are used to get the snake from top left corner
            
        for x,y in self.coordinates:      # here we are creating the gui of square which is to be formed on the screen 
            square=canvas.create_rectangle(x,y,x+SPACE_SIZE,y+SPACE_SIZE,fill=SNAKE_COLOR,tags="snake")
            self.squares.append(square) # now the square created is appended into the list of squares
class Food:
    def __init__(self):
        while True:
            x = random.randint(0, (GAME_WIDTH // SPACE_SIZE) - 1) * SPACE_SIZE
            y = random.randint(0, (GAME_HEIGHT // SPACE_SIZE) - 1) * SPACE_SIZE

            # Check if the new food coordinates overlap with the snake
            if (x, y) not in snake.coordinates:
                break

        self.coordinates = [x, y]
        canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tag="food")     
        

        

def next_turn(snake , food):
    x,y = snake.coordinates[0]  # set the coordinates of the snake 
    # now set if else conditions to set the movement of the snake 
    if direction == "up":
        y-=SPACE_SIZE
    elif direction == "down":
        y+=SPACE_SIZE
    elif direction == "left":
        x-=SPACE_SIZE
    elif direction =="right":
        x+=SPACE_SIZE
    
    snake.coordinates.insert(0,(x,y)) # updates new coordinates for the snake after conditions (0,(x,y))indicates the new direction
    
    square =canvas.create_rectangle(x,y,x+SPACE_SIZE,y+SPACE_SIZE,fill=SNAKE_COLOR)# update the canvas 
    snake.squares.insert(0,square) # update the squares 
     # now to delete the remaining part of the snake 
     
  
          
    if x == food.coordinates[0] and y == food.coordinates[1]:
        global score
        global SPEED
        score += 1
        if SPEED > 60: SPEED -= 10
        lable.config(text="Score: {}".format(score))

        canvas.delete("food")
        food = Food()
        # now if the food is eaten then the snake size will increase or else it will be same 
    else:
        del snake.coordinates [-1]  # deletes the last coordinates [-1] 
        canvas.delete(snake.squares[-1])# updates the new snake aftwer deleting the remaining squares into the canvas
        del snake.squares[-1] # delete the squares forming the snake 
    if check_collision(snake):# cheking for collisions using check_collision function 
        game_over()# call game over function if there is a collision 
    else:     # if there are no collision then update the canvas using next turn function    
        window.after(SPEED,next_turn,snake,food)  # call the next turn function without the perameters      
        
def change_direction (new_direction):
    global direction  # THIS  is the old direction of the snake in which it is moving previously 
    
    if new_direction == 'left':
        if direction!='right':# inorder to prevent 180 degree turn 
            #if above conditions are true then direction will get the value  of the new direction 
            direction=new_direction
    
    elif new_direction == 'right':
        if direction!='left':# inorder to prevent 180 degree turn 
            #if above conditions are true then direction will get the value  of the new direction 
            direction=new_direction
            
    elif new_direction == 'up':
        if direction!='down':# inorder to prevent 180 degree turn 
            #if above conditions are true then direction will get the value  of the new direction 
            direction=new_direction
            
    elif new_direction == 'down':
        if direction!='up':# inorder to prevent 180 degree turn 
            #if above conditions are true then direction will get the value  of the new direction 
            direction=new_direction                        
def check_collision(snake):
    x , y = snake.coordinates[0]  # using snake coordinates chechk weather the snake is inside the canvas coordinates or not 
    if x<0 or x>=GAME_WIDTH: # snake in x direction ( if it does the collision then return true and game will stop )
        return True 
    elif y<0 or y>=GAME_HEIGHT:# snake in y direction ( if it does the collision then return true and game will stop )
        return True
    
    for body_part in snake.coordinates[1:] :# creating a variable body_parts which has values from head of snake to the rest of the body 
        if x == body_part[0] and y == body_part[1]:
            return True   # here x and y are head of the snake if they touch the snake coordinates the True isd returned 

            
    # or if there are no collision then it will return 0 ( FALSE)
    return False    
    
def game_over():
    canvas.delete(ALL)  # if the game is ovewr then deletes all things present in the canvas
    canvas.create_text(canvas.winfo_width()/2,canvas.winfo_height()/2,font=('consolas',90) ,text="GAME OVER",
                       fill="#FF6868",tags="gameover")
    
    
def restart_game():
    global snake ,food,score,direction
    canvas.delete(ALL)
    snake=Snake()
    food=Food()
    score=0
    direction='down'
    lable.config(text="Score:{}".format(score))
    next_turn(snake,food )


    restart_button=Button(window,text="RESTART",command=restart_game,font=('consolas',20),fill="#00FF00")
    restart_button.place(x=0,y=0)

        
#now we have to add a game over text into the centre of the canvas ..... using winfi(widthand height)/2 we get the centre of the screen
window = Tk()   # this is using tkinter to create a GUI window for us 
window.title("Snake Game By @ Aryan Prasher") # The tite of our window
window.resizable(False,False) # our window cant be resized 
# now create the initial score andf initial direction
score=0
direction ='down'

lable=Label(window,text="Score:{}".format(score),font=('helvetica',40))# Score will be appearing on the top of the window which is taking input from intial score 
lable.pack()# no further changes can be done
# create a canvas where all this will appear taking the constant values as input     
canvas = Canvas(window,bg=BACKGROUND_COLOR,height=GAME_HEIGHT,width=GAME_WIDTH)
canvas.pack()
window.update() # for making the window to appear in the centre of thew screen 
#creating some variable to store the width and height of the window and the screen ol9
window_width=window.winfo_width()
window_height=window.winfo_height()
screen_width=window.winfo_screenwidth()
screen_height=window.winfo_screenheight()
x =int((screen_width//2)-(window_width//2))# it will get the centre of the screen  width wise
y=int((screen_height//2)-(window_height//2))# it will get the center of the screen height wise 
# now using geometry usinf f string ( format ) width *height*x
window.geometry(f"{window_width}x{window_height}+{x}+{y}")

# now we are binding key to thwe snake using an annonymous function (lambda ) 
window.bind('<a>',lambda event :change_direction('left'))# assigning a to left 
window.bind('<d>',lambda event :change_direction('right'))#d to right 
window.bind('<w>',lambda event :change_direction('up'))#w to up 
window.bind('<s>',lambda event :change_direction('down'))# s to down



snake = Snake()
food = Food()
next_turn(snake,food)



window.mainloop()
