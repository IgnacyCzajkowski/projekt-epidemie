import utils
import matplotlib.pyplot as plt

Ilist = []
Rlist = []
Slist = []
SIMULATIONS = utils.count_character_occurrences("C:\\Users\\Ignacy\\Desktop\\python\\algorytmy_genetyczne_2\\epidemie\\magistrala2.txt", "b")
file = open("C:\\Users\\Ignacy\\Desktop\\python\\algorytmy_genetyczne_2\\epidemie\\magistrala2.txt", "r")


for j in range(SIMULATIONS):
    TIME = int(utils.readUntilChar(file, "b"))
    for i in range(TIME):
        if j == 0:
            Ilist.append(int(utils.readUntilChar(file, " ")))
            Rlist.append(int(utils.readUntilChar(file, " ")))
            Slist.append(int(utils.readUntilChar(file, "\n")))
        else:
            Ilist[i] += int(utils.readUntilChar(file, " "))
            Rlist[i] += int(utils.readUntilChar(file, " "))
            Slist[i] += int(utils.readUntilChar(file, "\n"))

for i in range(len(Ilist)):
    Ilist[i] = Ilist[i] / SIMULATIONS
    Rlist[i] = Rlist[i] / SIMULATIONS
    Slist[i] = Slist[i] / SIMULATIONS        


#print(SIMULATIONS)
#print(Ilist)
def plot(Slist, Ilist, Rlist): #To do innego pliku
    plt.plot(Slist, label = "S")
    plt.plot(Ilist, label = "I")
    plt.plot(Rlist, label = "R")
    plt.ylabel("Ilosc")
    plt.xlabel("Czas")
    plt.legend()
    plt.show()
def main():
    plot(Slist, Ilist, Rlist)    

    
    ##Ilist.append(int(str.split(" ")[0]))
    ##Rlist.append(int(str.split(" ")[1]))
    ##Slist.append(int(str.split(" ")[2]))

   