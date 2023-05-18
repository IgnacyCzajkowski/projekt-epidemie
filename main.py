import numpy as np
import random as rnd
import matplotlib.pyplot as plt
import utils

state = {
  "S": 0,
  "I": 1,
  "R": 2
}

params = {
    "infection_prob": 0.1,
    "death_prob": 0.02,
    "Wymiar": 100,
    "Time_steps": 100
}

Ilist = [] #Tablice do innego pliku
Rlist = [] #
Slist = [] #


class Board:
    def __init__(self, d):
        self.d = d
        self.pola = np.zeros((params["Wymiar"], params["Wymiar"]))

    def getClosest(self, x, y):
        closest = self.pola[[(x-1) % params["Wymiar"],(x+1) % params["Wymiar"]],:][:,[(y-1) % params["Wymiar"],(y+1) % params["Wymiar"]]].flatten()
        closest = np.append(closest, self.pola[x, (y-1) % params["Wymiar"]])
        closest = np.append(closest, self.pola[x, (y+1) % params["Wymiar"]])
        closest = np.append(closest, self.pola[(x-1) % params["Wymiar"], y])
        closest = np.append(closest, self.pola[(x+1) % params["Wymiar"], y])
        return closest

    def interactWithClosest(self, x, y):
        if self.pola[x, y] == state["S"]:
            for i in range(np.count_nonzero(self.getClosest(x, y) == state["I"])):
                if rnd.random() < params["infection_prob"]:
                    return state["I"]
        elif self.pola[x, y] == state["I"]:
            if rnd.random() < params["death_prob"]:
                return state["R"] 
        return self.pola[x, y] 

    def returnNumbers(self):   # To trzeba poszukac i zoptymalizowac
        infected = 0
        retired = 0
        suspected = 0
        for row in self.pola:
            for cel in row:
                if cel == state["I"]:
                    infected += 1
                elif cel == state["R"]:
                    retired += 1
                else:
                    suspected += 1        
        return infected, retired, suspected



def initFirst(board):
    x = rnd.randint(0, params["Wymiar"]) 
    y = rnd.randint(0, params["Wymiar"])
    board.pola[x, y] = state["I"] 
    Ilist.append(board.returnNumbers()[0]) #te listy do innego pliku
    Rlist.append(board.returnNumbers()[1]) #
    Slist.append(board.returnNumbers()[2]) #
    #print(board.returnNumbers()[0], board.returnNumbers()[1], board.returnNumbers()[2]) #to do debugowania

def writeSnapshot(board, file):
    string = ""
    for x, y in np.ndindex(board.pola.shape):
        #string += str(board.pola[x, y])
        string += utils.convertPointState(board.pola[x, y])
    string += "t"    
    file.write(string)
    file.flush()

def writeForPlot(board, file2):
    file2.write(str(board.returnNumbers()[0]) + " ")
    file2.write(str(board.returnNumbers()[1]) + " ") 
    file2.write(str(board.returnNumbers()[2]) + "\n")  
    file2.flush()   


def timeStep(oldBoard, file, file2):
    newBoard = Board(params["Wymiar"])
    for x, y in np.ndindex(oldBoard.pola.shape):    
        newBoard.pola[x, y] = oldBoard.interactWithClosest(x, y)
    writeSnapshot(newBoard, file)
    writeForPlot(newBoard, file2)    
    Ilist.append(newBoard.returnNumbers()[0]) #te listy do innego pliku
    Rlist.append(newBoard.returnNumbers()[1]) #
    Slist.append(newBoard.returnNumbers()[2]) # 
    #print(newBoard.returnNumbers()[0], newBoard.returnNumbers()[1], newBoard.returnNumbers()[2]) #to do debugowania
    #print(newBoard.getClosest(5, 5)) #
    #print(newBoard.getClosest(0, 0)) #
    return newBoard


def algorithm(board, file, file2):
    for i in range(params["Time_steps"]):
        board = timeStep(board, file, file2)
       #print(board.getClosest(5, 5)) #
        #print(board.getClosest(0, 0)) #

def plot(Slist, Ilist, Rlist): #To do innego pliku
    plt.plot(Slist, label = "S")
    plt.plot(Ilist, label = "I")
    plt.plot(Rlist, label = "R")
    plt.ylabel("Ilosc")
    plt.xlabel("Czas")
    plt.legend()
    plt.show()                 #    
                                 
def main():
    magistrala = open("C:\\Users\Ignacy\\Desktop\python\\algorytmy_genetyczne_2\\epidemie\\magistrala.txt", "w")
    magistrala.write(str(params["Wymiar"]))
    magistrala.write("d")
    magistrala.flush() 

    magistrala2 = open("C:\\Users\\Ignacy\\Desktop\\python\\algorytmy_genetyczne_2\\epidemie\\magistrala2.txt", "a")
    #magistrala2 = open(".\\magistrala2.txt", "a")
    magistrala2.write(str(params["Time_steps"])+"b"+"\n")
    magistrala2.flush()  
    board = Board(params["Wymiar"])
    initFirst(board)
    algorithm(board, magistrala, magistrala2)
    magistrala.close()
    magistrala2.close()
    #plot(Slist, Ilist, Rlist)
    #print(board.getClosest(5, 5)) #
    
    

#if __name__ == "__main__":
main()                                     