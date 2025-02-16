from tkinter import *
import tkinter.font as font
import random

player_score = 0
computer_score = 0
options = [('rock',0), ('paper',1), ('scissors',2)]

def choice(player_input):
    global player_score, computer_score

    computer_input = get_computer_choice()

    player_choice_label.config(text = 'Your Selected : ' + player_input[0])
    computer_choice_label.config(text = 'Computer Selected : ' + computer_input[0])

    if(player_input == computer_input):
        winner_label.config(text = "Tie")
    elif((player_input[1] - computer_input[1]) % 3 == 1):
        player_score += 1
        winner_label.config(text="You Won!!!")
        player_score_label.config(text = 'Your Score : ' + str(player_score))
    else:
        computer_score += 1
        winner_label.config(text="Computer Won!!!")
        computer_score_label.config(text='Computer Score : ' + str(computer_score))

#Function to Random-Select Computer Choice
def get_computer_choice():
    return random.choice(options)

rps_window = Tk()
rps_window.title("Rock Paper Scissors Game")
rps_window.geometry('700x300')
rps_font = font.Font(size = 12)

#Displaying the Game Title
rps_title = Label(text = 'Rock-Paper-Scissors', font = font.Font(size = 20), fg = 'grey')
rps_title.pack()

#Label to dispay
winner_label = Label(text = "Let's Start the Game...", fg = 'green', font = font.Font(size = 13), pady = 8)
winner_label.pack()

input_f = Frame(rps_window)
input_f.pack()

#Displaying player options
player_options = Label(input_f, text = "Your Options : ", font = rps_font, fg = 'grey')
player_options.grid(row = 0, column = 0, pady = 8)
#Rock Button
rock_btn = Button(input_f, text = 'Rock', width = 15, bd = 0, bg = 'grey', pady = 10, command = lambda: choice(options[0]))
rock_btn.grid(row = 1, column = 1, padx = 8, pady = 5)
#Paper Button
paper_btn = Button(input_f, text = 'Paper', width = 15, bd = 0, bg = 'white', pady = 10, command = lambda: choice(options[1]))
paper_btn.grid(row = 1, column = 2, padx = 8, pady = 5)
#Scissors Button
scissors_btn = Button(input_f, text = 'Scissors', width = 15, bd = 0, bg = 'blue', pady = 10, command = lambda: choice(options[2]))
scissors_btn.grid(row = 1, column = 3, padx = 8, pady = 5)

#Displaying players choice and player score
score_label = Label(input_f, text = 'Score : ', font = rps_font, fg = 'grey')
score_label.grid(row = 2, column = 0)
player_choice_label = Label(input_f, text = 'Your Choice : ---', font = rps_font,fg='green')
player_choice_label.grid(row = 3, column = 1, pady = 5)
player_score_label = Label(input_f, text = 'Your Score : -', font = rps_font,fg='green')
player_score_label.grid(row = 3, column = 2, pady = 5)
#Displaying computer choice and computer score
computer_choice_label = Label(input_f, text = 'Computer Choice : ---', font = rps_font, fg = 'Red')
computer_choice_label.grid(row = 4, column = 1, pady = 5)
computer_score_label = Label(input_f, text = 'Computer Score : -', font = rps_font, fg = 'Red')
computer_score_label.grid(row = 4, column = 2, padx = (10,0), pady = 5)

rps_window.mainloop()