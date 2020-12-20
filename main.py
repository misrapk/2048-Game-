from tkinter import *
from tkinter import messagebox
import random

class Board:
    bgColor = {
        '2': '#eee4da',
        '4': '#2B89C6',
        '8': '#22CC7E',
        '16':'#E6358B',
        '32':'#CE5404',
        '64':'#F47070',
        '128': '#65A549',
        '256': '#F27C4F',
        '512': '#2ecc72',
        '1024': '#EEC213',
        '2048':'#FF3031',	
        
    }
    color={
         '2': '#0045BE',
        '4': '#f9f6f2',
        '8': '#f9f6f2',
        '16': '#f9f6f2',
        '32': '#f9f6f2',
        '64': '#f9f6f2',
        '128': '#f9f6f2',
        '256': '#f9f6f2',
        '512': '#776e65',
        '1024': '#f9f6f2',
        '2048': '#f9f6f2',
    }
    
    def __init__(self):
        self.n=4
        self.window = Tk()   #main tkinter window
        self.window.title('2048 Game')
        
        #tkinter frame widget
        self.gameArea = Frame(self.window, bg = 'azure3')
        self.board = []   #4x4 grid which displays the value
        self.gridCell = [[0]*4 for i in range(4)] #4x4 intgr matrix which displays the value of the cell
        self.compress = False
        self.merge = False
        self.moved = False
        self.score = 0   #stroe the score of player
        
        for i in range(4):
            rows = []
            for j in range(4):
                l = Label(self.gameArea, text = '', bg='azure4',
                          font = ('arial',22,'bold'), width=4, height=2)
                l.grid(row = i, column=j, padx=7, pady=7)
                
                rows.append(l);
            self.board.append(rows)
        self.gameArea.grid()
       
       
    #TODO: reverse the grid cell matrix 
    def reverse(self):
        for idx in range(4):
            i = 0
            j=3
            while(i<j):
                self.gridCell[idx][i], self.gridCell[idx][j] = self.gridCell[idx][j], self.gridCell[idx][i]
                i+=1
                j-=1
                
    #TODO: Function to transppose the gridMatrix
    def transpose(self):
        self.gridCell = [list(t) for t in zip(*self.gridCell)]
        
    
    #TODO: Move non empty cell to the left
    
    def compressGrid (self):
        self.compress = False
        temp = [[0] * 4 for i in range(4)]
        for i in range(4):
            cnt  =0 
            for j in range(4):
                if self.gridCell[i][j]!=0:
                    temp[i][cnt] = self.gridCell[i][j]
                    
                    if cnt!=j:
                        self.compress = True
                        
                    cnt+=1
                    
        self.gridCell = temp
        
    #TODO: function to add the two same adjacent cell
    def mergeGrid(self):
        self.merge = False
        for i in range(4):
            for j in range(4-1):
                if self.gridCell[i][j] == self.gridCell[i][j+1] and self.gridCell[i][j] !=0:
                    self.gridCell[i][j] *=2
                    self.gridCell[i][j+1] = 0
                    self.score += self.gridCell[i][j]
                    self.merge = True
                        
        
        #TODO: randomly make a gridCell from 0 to value 2
    def randomCell(self):
        cells=[]
            
        #make all cells 0
        for i in range(4):
            for j in range(4):
                if self.gridCell[i][j]==0:
                    cells.append((i,j))
             
             # assign value to 2           
        curr = random.choice(cells)
        i = curr[0]
        j = curr[1]
        self.gridCell[i][j]=2
                
        
        #TODO: function to check either we merge two cell or not
    def canMerge(self):
        for i in range(4):
            for j in range(3):
                if self.gridCell[i][j] == self.gridCell[i][j+1]:
                    return True
                    
        for i in range(3):
            for j in range(4):
                if self.gridCell[i+1][j] == self.gridCell[i][j]:
                    return True
            
        return False
        
        
    #TODO: Assign color to each cell
    def colorGrid(self):
        for i in range(4):
            for j in range(4):
                if self.gridCell[i][j] ==0:
                    self.board[i][j].config(text='', bg = 'azure4')
                else:
                    self.board[i][j].config(text=str(self.gridCell[i][j]), 
                                            bg = self.bgColor.get(str(self.gridCell[i][j])),
                                            fg = self.color.get(str(self.gridCell[i][j])))

        
        
    
    
    
class Game:
    def __init__(self, gamepanel):
        self.gamepanel = gamepanel
        self.end = False
        self.won = False
        
        
    #TODO: Function to use at start of the game
        
    def start(self):
       self.gamepanel.randomCell()
       self.gamepanel.randomCell()
       self.gamepanel.colorGrid()
       self.gamepanel.window.bind('<Key>', self.linkKeys)
       self.gamepanel.window.mainloop()
       
       
        
    
    #TODO: check for game won or not
    def linkKeys(self, event):
        
        #if game is won or end then simply return
        if self.end or self.won:
            return
        
        #else
        pressedKey = event.keysym
        
        if pressedKey == 'Up':
            self.gamepanel.transpose()
            self.gamepanel.compressGrid()
            self.gamepanel.mergeGrid()
            self.gamepanel.moved = self.gamepanel.compress or self.gamepanel.merge
            self.gamepanel.compressGrid()
            self.gamepanel.transpose()
            
            
        elif pressedKey == 'Down':
            self.gamepanel.transpose()
            self.gamepanel.reverse()
            self.gamepanel.compressGrid()
            self.gamepanel.mergeGrid()
            self.gamepanel.moved = self.gamepanel.compress or self.gamepanel.merge
            self.gamepanel.compressGrid()
            self.gamepanel.reverse()
            self.gamepanel.transpose()
            
        elif pressedKey == 'Left':
            self.gamepanel.compressGrid()
            self.gamepanel.mergeGrid()
            self.gamepanel.moved = self.gamepanel.compress or self.gamepanel.merge
            self.gamepanel.compressGrid()

        elif pressedKey == 'Right':
            self.gamepanel.reverse()
            self.gamepanel.compressGrid()
            self.gamepanel.mergeGrid()
            self.gamepanel.moved = self.gamepanel.compress or self.gamepanel.merge
            self.gamepanel.compressGrid()
            self.gamepanel.reverse()
    
        else: 
            pass
        
        self.gamepanel.colorGrid()
        print(self.gamepanel.score)
        
        flag = 0
        
        for i in range(4):
            for j in range(4):
                if(self.gamepanel.gridCell[i][j] == 2048):
                    flag =1
                    break
                
        if (flag==1):     #Game won
            self.won = True
            messagebox.showinfo('2048', message="Congo! You WOn The Game!!!")
            print("won")
            return
        
        for i in range(4):
            for j in range(4):
                if self.gamepanel.gridCell[i][j]==0:
                    flag=1
                    break
                
        if not (flag or self.gamepanel.canMerge()):
            self.end = True
            messagebox.showinfo('2048', 'OOPS!! GAME OVER!')
            print('over')
            
        if self.gamepanel.moved:
            self.gamepanel.randomCell()
            
            
        self.gamepanel.colorGrid()                        
        
    
    

gamepanel = Board()
game2048 = Game(gamepanel)
game2048.start()