def convertPointState(point_value):
    if(point_value == 0):
        return "s"
    elif(point_value == 1):
        return "i"
    else:
        return "r"

def readUntilChar(file, stop_char):
    result = ""
    while True:
        char = file.read(1)
        if char == stop_char:
            break
        if not char: #To ostatnie sprawdzenie pewnie mozna ominac  
            print("koniec pliku")
            break
        result += char
    return result 


def readOneStep(file):
    result = []
    string = readUntilChar(file, "t")
    for char in string:
        result.append(char)
    return result 

def readOneline(file):
    readUntilChar(file, "\n")  

def count_character_occurrences(file_path, character):
    with open(file_path, 'r') as file:
        content = file.read()         
        count = content.count(character) 
    return count      
