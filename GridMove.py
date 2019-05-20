import random
#----------------------------------------------------------
class cell (object):
    def __init__(self,ID):
        assert type(ID) == int
        self.ID = ID
    def celloptions(self,option):
        options = {
            1: '#', #wall cell
            2: 'O', #player cell
            3: '.', #trail cell
            4: 'X', #goal cell
        }
        return options.get(option, ' ')
    def __str__(self):
        return self.celloptions(self.ID)
    def destroy(self):
        self.ID = 0
#----------------------------------------------------------    
def PrintMap(position,X):
    X[position[0]][position[1]] = cell(2)#playercell
    text = ""
    for list in X:
        for string in list:
           text = text + str(string)
        print(text)
        text = ""
#----------------------------------------------------------
def CreateMap(x,y,grid,numwalls):
    Y = []
    Goal = []
    grid.clear()
    for i in range(0,y):
        Y.append(cell(0))#blankcell
    for i in range(0,x):
        grid.append(Y[:])
    for i in range(0,numwalls):
        grid[random.randint(0,x-1)][random.randint(0,y-1)] = cell(1)#wallcell
    Goal = [random.randint(0,x-1),random.randint(0,y-1)]
    grid[Goal[0]][Goal[1]] = cell(4)#goalcell
    return Goal
#----------------------------------------------------------
def move(grid,position,x,y):
    def moveoptions(option):
        options = {
            #[(0 = verticle 1 = horizontal), increment]
            "w": [0,-1], #Up
            "a": [1,-1], #Left
            "s": [0,1], #Down
            "d": [1,1], #Right
        }
        return options.get(option, " ")
    def detectcollision(position,destination):
        if destination[0] < 0\
        or destination[1] < 0\
        or destination[0] > x-1\
        or destination[1] > y-1:
            print("You cannot go that way")
        if grid[destination[0]][destination[1]].ID == 1:#wallcell
            print("You cannot go that way")
        else:
            position = destination[:]
        return position
    grid[position[0]][position[1]] = cell(3)#trailcell
    move = moveoptions(input("Up(w),Left(a), Down(s), or Right(d)?"))
    if move != " ":
        destination = position[:]
        destination[move[0]] += move[1]
        position = detectcollision(position,destination)
    else:
        print("invalid input")
    return position
#----------------------------------------------------------
def main():
    y = 10
    x = 10
    walls = 20
    grid = []
    i = 0
    position = [0,0]
    userinput = ""
    playagain = True

    while playagain:
        Goal = CreateMap(x,y,grid,walls)
        while position != Goal:
            PrintMap(position,grid)
        ## move input
            position = move(grid,position,x,y)
        ## win
        print("Success!")
        PrintMap(position,grid)
        while userinput != "Y" and userinput != "N":
            userinput = input("Play again? Y/N")
            if userinput == "Y":
                playagain = True
            elif userinput == "N":
                playagain = False
            else:
                print("Invalid Input.")
        userinput = ""   
#----------------------------------------------------------
main()

## end
print("Good bye <3")
