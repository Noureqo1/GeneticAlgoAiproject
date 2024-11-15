import numpy as np
import pygame
import operator  
import time

class Puzzel ():

    def __init__(self):
        self.width = 800                    
        self.height = 800                   
        self.numRows = 20                     
        self.numColumns = 20
        self.wallRatio = 0.3
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.maze = np.zeros((self.numRows, self.numColumns))

        for i in range(self.numRows):
            for j in range(self.numColumns):
                if np.random.rand() < self.wallRatio:
                    self.maze[i][j] = 1
                else:
                    self.maze[i][j] = 0

        for i in range(min(3, self.numRows)):
            for j in range(min(3, self.numColumns)):
                self.maze[i][j] = 0                   


    def drawMaze(self):
        cellWidth = self.width / self.numColumns
        cellHeight = self.height / self.numRows
        
        self.screen.fill((0,0,0))
        
        for i in range(self.numRows):
            for j in range(self.numColumns):
                if self.maze[i][j] == 1:
                    pygame.draw.rect(self.screen, (255,255,255), (j*cellWidth, i*cellHeight, cellWidth, cellHeight))
            
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

puzz = Puzzel()

while True:
    puzz.drawMaze()
       
