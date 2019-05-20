import random
trailcell = "."
blankcell = " "
playercell = "O"
wallcell = "#"
goalcell = "X"
y = 10
x = 10
walls = 20

Y =[]
X= []
i = 0
position = [0,0]
destination = [0,0]
move = ""
playagain = True
userinput = ""

class cell (object):
    def __init__(self,ID):
        assert type(ID) == int
        self.ID = ID
    def __str__(self):
        if self.ID == 0:
            return " " #blank cell
        elif self.ID == 1:
            return "#" #wall cell
        elif self.ID == 2:
            return "O" #player cell
        elif self.ID == 3:
            return "." #trail cell
        elif self.ID == 4:
            return "X" #goal cell
        else:
            
            return " "
    def destroy(self):
        self.x = -1
        self.y = -1
        
    
def PrintMap(position,X,playercell):
    X[position[0]][position[1]] = cell(2)
    text = ""
    for list in X:
        for string in list:
           text = text + str(string)
        print(text)
        text = ""
def CreateMap(x,y):
    global X
    global Y
    global Goal
    X.clear()
    Y.clear()
    for i in range(0,y):
        Y.append(cell(0))
    for i in range(0,x):
        X.append(Y[:])
    for i in range(0,walls):
        X[random.randint(0,x-1)][random.randint(0,y-1)] = cell(1)
    Goal = [random.randint(0,x-1),random.randint(0,y-1)]
    X[Goal[0]][Goal[1]] = cell(4)

##Main Loop
while playagain:
    CreateMap(x,y)
    while position != Goal:
        PrintMap(position,X,playercell)
    ## move input
        X[position[0]][position[1]] = cell(3)
        destination = position[:]
        move = input("Up(w),Left(a), Down(s), or Right(d)?")
        if move == "a":
            destination[1] -= 1
        elif move == "d":
            destination[1] += 1
        elif move == "w":
            destination[0] -= 1
        elif move == "s":
            destination[0] += 1
        else:
            print("invalid Input")
    ##Detect boundary/collision
        if destination[0] < 0\
        or destination[1] < 0\
        or destination[0] > x-1\
        or destination[1] > y-1:
            print("You cannot go that way")
            destination = position[:]
        if X[destination[0]][destination[1]].ID == 1:
            print("You cannot go that way")
        else:
            position = destination[:]
    ## win
    print("Success!")
    PrintMap(position,X,playercell)
    while userinput != "Y" and userinput != "N":
        userinput = input("Play again? Y/N")
        if userinput == "Y":
            playagain = True
        elif userinput == "N":
            playagain = False
        else:
            print("Invalid Input.")
    userinput = ""
## end
print("Good bye <3")
