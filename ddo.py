import random

class Puzzle:
    """
    The Puzzle object is what handles the main game. It is in charge of initializing and storing the Button objects, taking input from the user, flipping the neighboring buttons' 
    states and checking for completion

    attributes:
        gameBoard: stores Button objects
        gameDifficulty: stores the difficulty specified by the user
    """

    def __init__(self):
        self.buttonList = [
        Button(1, (2,4)),
        Button(2, (1,5,3)),
        Button(3, (2,6)),
        Button(4, (1,5,7)),
        Button(5, (2,4,6,8)),
        Button(6, (3,5,9)),
        Button(7, (4,8)),
        Button(8, (7,5,9)),
        Button(9, (6,8))
        ]                                                               
        self.gameDifficulty = int(input("Available difficulties\nEasy\t[1]\nMedium\t[2]\nHard\t[3]\nExpert\t[4]\nPlease select a difficulty: "))
        self.puzzleGameplay()

    def displayBoard(self):
        """
        Displays the buttons in a 3x3 grid, note that True is printed as an "X" and False is printed as an "O"
        """
        for boardRow in range(3):
            for boardColumn in range(3):
                print("X" if self.buttonList[boardRow + boardColumn].isEnabled else "O", end=" ")
            print("")

    def isIncomplete(self):
        """
        Checks if the puzzle is incomplete
        Return True if incomplete then return value will be used inside the for loop
        """
        for currentButton in self.buttonList:
            if currentButton.isEnabled:
                return False
            return True 

    def puzzleGameplay(self):
        """
        Main game loop;
            1. ask the user for the number of the button they wish to flip
            2. flip said button and all its neighbors
            3. check if all buttons are the same, if not, return to step 1
        """
        while self.isIncomplete():
            self.displayBoard()

            # You can access all of the board's contents here
            #_gameBoard = self.gameBoard.buttonList
            # This is where we get which button the user would like to select
            inputButton = int(input("Enter button number: "))
            
            '''
            Task 1
            Requirement:
            Buttons adjacent to the inputButton should have their values flipped e.g. True -> False; False -> True
            '''

            '''
            Task 2
            Requirement:
            Buttons to the diagonals of the inputButton should have their values flipped
            '''

            '''
            Task 3
            Requirement:
            Should make the flipping neighbors alternate between adjacent and diagonal 
            '''

class Button:
    """
    The Button object stores its number/index, its state (True/False) and its neighbors. Through the changeState method it can have 
    its isEnabled value flipped
    """

    def __init__(self, number, neighbors1):
        self.isEnabled = random.choice([True,False])
        self.buttonNumber = number
        self.cardinalNeighbors = neighbors1
    
    def changeState(self):
        self.isEnabled ^= 1

game = Puzzle()
