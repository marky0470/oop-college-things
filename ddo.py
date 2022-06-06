import random

class Puzzle:
    
    def __init__(self):
        self.buttonList = [
        Button(1, (2,4),     [5]),
        Button(2, (1,5,3),   (4,6)),
        Button(3, (2,6),     [5]),
        Button(4, (1,5,7),   (2,8)),
        Button(5, (2,4,6,8), (1,3,7,9)),
        Button(6, (3,5,9),   (2,8)),
        Button(7, (4,8),     [5]),
        Button(8, (7,5,9),   (4,6)),
        Button(9, (6,8),     [5])
        ]

        self.gameDifficulty = int(input("Available difficulties\nEasy\t[1]\nMedium\t[2]\nHard\t[3]\nExpert\t[4]\nPlease select a difficulty: "))
        if self.gameDifficulty == 1:
            self.isCardinal = True
        else:
            self.isCardinal = False
        self.puzzleGameplay()

    def displayBoard(self):

        currentColumn = 0
        for eachButton in self.buttonList:
            print("X" if eachButton.isEnabled else "O", end = " ")
            currentColumn += 1
            if currentColumn == 3:
                print("")
                currentColumn = 0

    def isIncomplete(self):

        for currentButton in self.buttonList:
            if currentButton.isEnabled == False:
                return True
        return False

    def puzzleGameplay(self):

        while self.isIncomplete():
            self.displayBoard()

            inputButton = int(input("Enter button number: "))

            for eachButton in self.buttonList:
                if eachButton.buttonNumber == inputButton:
                    eachButton.changeState()
                    if self.isCardinal == True:
                        inputNeighbors = eachButton.cardinalNeighbors
                    else:
                        inputNeighbors = eachButton.diagonalNeighbors
            
            for eachButton in self.buttonList:
                if eachButton.buttonNumber in inputNeighbors:
                    eachButton.changeState()

            if self.gameDifficulty == 3:
                self.isCardinal = not(self.isCardinal)
            elif self.gameDifficulty == 4:
                self.isCardinal = random.choice([True, False])
        
        print("Puzzle Complete")

class Button:

    def __init__(self, number, neighbors1, neighbors2):
        self.isEnabled = random.choice([True,False])
        self.buttonNumber = number
        self.cardinalNeighbors = neighbors1
        self.diagonalNeighbors = neighbors2
    
    def changeState(self):
        self.isEnabled ^= 1

game = Puzzle()
