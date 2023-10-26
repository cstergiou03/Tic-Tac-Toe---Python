import tkinter as tk
from tkinter import *

def board_load():

    global window, canvas, score_text1, score_text2

    # Δημιουργία ενός παραθύρου
    window = tk.Tk()
    window.title("Tic-Tac-Toe")
    window.geometry("1000x603")  

    # Δημιουργία Canvas για τις γραμμές
    canvas = tk.Canvas(window, width=1000, height=604)
    canvas.pack()


    # Γραμμές παιχνιδίου αρχή(x1, y1) τέλος(x2, y2) 
    canvas.create_line(200, 0, 200, 600, width=3) 
    canvas.create_line(400, 0, 400, 600, width=3)  
    canvas.create_line(0, 200, 600, 200, width=3)  
    canvas.create_line(0, 400, 600, 400, width=3)  

    #'Όρια παιχνιδιού
    canvas.create_line(600, 0, 600, 600, width=3)  # Όρια παιχνιδιου δεξια
    canvas.create_line(0, 600, 600, 600, width=3)  # Όρια παιχνιδιου κάτω

    #New game button
    New_Game = Button(window, text="New Game", height= 3, width=15, command=new_game)
    New_Game.pack()
    New_Game.place(x = 760, y = 300)

    #Reset game button
    Reset_Game = Button(window, text="Reset Game", height= 3, width=15, command=reset_game)
    Reset_Game.pack()
    Reset_Game.place(x = 760, y = 400)

    # Παίχτες
    canvas.create_text(700, 50, text="X", font=("Helvetica", 48), fill="red")
    canvas.create_text(900, 50, text="O", font=("Helvetica", 48), fill="blue")

    # Σκόρ παιχνιδιού
    score_text1 = canvas.create_text(700, 180, text=score[0], font=("Helvetica", 48), fill="red", tags="score")
    score_text2 = canvas.create_text(900, 180, text=score[1], font=("Helvetica", 48), fill="blue", tags="score")

    canvas.bind("<Button-1>", move)
    canvas.pack() 

def move(event):

    global next, win, game_over, score_text1, score_text2

    if game_over:  
        return
    
    if win:
        return

    if next == "O":
        symbol = "O"
        color = "blue"
        next = "X"
    else:
        symbol = "X"
        color = "red"
        next = "O"

    if(event.x <= 200 and event.y <= 200):
        if board[0][0] == "":
            canvas.create_text(100,100, text=symbol, font=("Helvetica", 90), fill=color, tags="game_board") # 1
            board[0][0] = symbol
    elif(event.x > 200 and event.x <= 400 and event.y <= 200):
        if board[0][1] == "":
            canvas.create_text(300,100, text=symbol, font=("Helvetica", 90), fill=color, tags="game_board") # 2
            board[0][1] = symbol
    elif(event.x > 400 and event.x <= 600 and event.y <= 200):
        if board[0][2] == "":
            canvas.create_text(500,100, text=symbol, font=("Helvetica", 90), fill=color, tags="game_board") # 3
            board[0][2] = symbol
    elif(event.x <= 200 and event.y > 200 and event.y > 200 and event.y <= 400):
        if board[1][0] == "":
            canvas.create_text(100,300, text=symbol, font=("Helvetica", 90), fill=color, tags="game_board") # 4
            board[1][0] = symbol
    elif(event.x > 200 and event.x <= 400 and event.y > 200 and event.y <= 400):
        if board[1][1] == "":
            canvas.create_text(300,300, text=symbol, font=("Helvetica", 90), fill=color, tags="game_board") # 5
            board[1][1] = symbol
    elif(event.x > 400 and event.x <= 600 and event.y > 200 and event.y <= 400):
        if board[1][2] == "":
            canvas.create_text(500,300, text=symbol, font=("Helvetica", 90), fill=color, tags="game_board") # 6
            board[1][2] = symbol
    elif(event.x <= 200 and event.y > 200 and event.y > 400 and event.y <= 600):
        if board[2][0] == "":
            canvas.create_text(100,500, text=symbol, font=("Helvetica", 90), fill=color, tags="game_board") # 7
            board[2][0] = symbol
    elif(event.x > 200 and event.x <= 400 and event.y > 400 and event.y <= 600):
        if board[2][1] == "":
            canvas.create_text(300,500, text=symbol, font=("Helvetica", 90), fill=color, tags="game_board") # 8
            board[2][1] = symbol
    elif(event.x > 400 and event.x <= 600 and event.y > 400 and event.y <= 600):
        if board[2][2] == "":
            canvas.create_text(500,500, text=symbol, font=("Helvetica", 90), fill=color, tags="game_board") # 9
            board[2][2] = symbol

    win = checkWin(board, symbol)

    if win:
        if symbol == "X":
            score[0] += 1
            canvas.create_text(800,520, text=f"{symbol} Wins" , font=("Helvetica", 50), fill=color, tags="game_board") #Winner
        else:
            score[1] += 1
            canvas.create_text(800,520, text=f"{symbol} Wins" , font=("Helvetica", 50), fill=color, tags="game_board") #Winner
        canvas.itemconfig(score_text1, text=score[0])
        canvas.itemconfig(score_text2, text=score[1])
    elif isBoardFull(board):
        canvas.create_text(810,520, text="Tie" , font=("Helvetica", 50), fill="green", tags="game_board") #Winner


def isBoardFull(board):
    for row in range(3):
        for col in range(3):
            if board[row][col] == "":
                return False
    return True



def checkWin(board, symbol):
    
    if(board[0][0] == symbol and board[0][1] == symbol and board[0][2] == symbol): #οριζοντια 1
        return True
    elif(board[1][0] == symbol and board[1][1] == symbol and board[1][2] == symbol): #οριζοντια 2
        return True
    elif(board[2][0] == symbol and board[2][1] == symbol and board[2][2] == symbol): #οριζοντια 3
        return True
    elif(board[0][0] == symbol and board[1][0] == symbol and board[2][0] == symbol): #κάθετη 1
        return True
    elif(board[0][1] == symbol and board[1][1] == symbol and board[2][1] == symbol): #κάθετη 2
        return True
    elif(board[0][2] == symbol and board[1][2] == symbol and board[2][2] == symbol): #κάθετη 3
        return True
    elif(board[0][0] == symbol and board[1][1] == symbol and board[2][2] == symbol): #διαγώνιος 1
        return True
    elif(board[0][2] == symbol and board[1][1] == symbol and board[2][0] == symbol): #διαγώνιος 1
        return True
    
def new_game():
    global board, game_over, canvas, win, score

    game_over = False
    win = False

    for row in range(3):
        for col in range(3):
            board[row][col] = ""

    canvas.delete("game_board")  # Καθαρίζει το Canvas από τα στοιχεία που έχουν ζωγραφιστεί.
    
    
def reset_game():
    global board, game_over, canvas, win

    game_over = False
    win = False

    for row in range(3):
        for col in range(3):
            board[row][col] = ""

    canvas.delete("game_board")  
    score[0] = 0
    score[1] = 0
    canvas.itemconfig(score_text1, text=score[0])
    canvas.itemconfig(score_text2, text=score[1])


board = [["", "", ""],
         ["", "", ""],
         ["", "", ""]]

score = [0, 0]

global win, game_over, window, canvas
win = False
game_over = False


# Εκκίνηση του main loop
board_load()
window.mainloop()
