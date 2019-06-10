import random
import PathfinderCharacterMaker
import BitMapWriter


#----------------------------------------------------------


class grid (list):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def return_list(self):
        gridlist = []
        for row in self:
            gridlist.append(row)
        print(gridlist)
        print("hi")
        return gridlist

    def create_blank(self):
        print("Map created")
        for i in range (0,self.height):
            row = []
            for j in range(0,self.width):
                row.append(cell(0))#Blank cell
            self.append(row)

    def create_random(self, num_walls):
        self.create_blank()
        print("Map randomized")
        for i in range(0, num_walls):
            self.editcell(random.randint(0, self.height-1),
            random.randint(0,self.width-1), cell(1))#wall cell

    def create_custom(self, mapstring):
        pass
            
    def print(self, playerlist):
        print("Printing Map")
        ##Place players
        for i in range(0,len(playerlist)):
            try:
                self.editcell(playerlist[i].position[0],
                              playerlist[i].position[1],
                              str(" "+str(playerlist[i].name[:1])+"  "))

            except:
                print("cannot place player " + playerlist[i].name)
        #Print map
        text = "" 
        for row in self:
            text = ":"
            for cell in row:
                text = text + str(cell)
            print(text)
            text = ""

        #Create Bitmap
        BitMapWriter.CreateNewTwentyFourBit(self)
        
        #Clear trails
        for i in self:
            for j in i:
                try:
                    if j.ID == 3:#triailcell
                        j.ID = 0#blank cell
                except:
                    pass

    def editcell(self, x, y, newvalue):
        try:
            self[x][y] = newvalue
        except:
            print("Out of range")
#------------------------------------------------------------


class cell (object):
    def __init__(self,ID):
        assert type(ID) == int
        self.ID = ID

    def __repr__(self):
        returntext = self.celloptions(self.ID)
        return returntext

    def __str__(self):
        returntext = self.celloptions(self.ID)
        return returntext

    def celloptions(self,option):
        options = {
            0: '██',
            1: '▒▒', #wall cell
            2: 'O', #player cell
            3: '▓▓', #trail cell
            4: 'X', #goal cell
        }
        return options.get(option, ' ')
    
    def destroy(self):
        self.ID = 0
#----------------------------------------------------------


class Unit (object):
    def __init__(self, name, position, movement):
        self.name = name
        self.position = position
        self.movement = movement

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name

    def Move(self, grid, directionstring, x, y):
        for j in directionstring:
            grid[int(self.position[0])][int(self.position[1])] = cell(3)#trailcell
            self.position = ObstacleCheck(grid,self.position,j,x,y)
        return grid
                    

#-----------------------------------------------------------
class Player(Unit):
    pass


#----------------------------------------------------------
class NPC(Unit):
    pass


#----------------------------------------------------------
class Monster(Unit):
    pass


#-------------------------------------------------------------
def CreatePlayer(name, position, movement, playerlist):
    print("Created player " + str(name) + " at coordinates " + str(position))
    player = Player(name,position,movement)
    playerlist.append(player)
    return playerlist


#----------------------------------------------------------
def ObstacleCheck(grid, position, direction, x, y):
    def moveoptions(option):
        options = {
            #[(0 = verticle 1 = horizontal), increment]
            "w": [-1, 0], #Up
            "a": [0, -1], #Left
            "s": [1, 0], #Down
            "d": [0, 1], #Right
        }
        return options.get(option, " ")

    def detectcollision(position, destination):
        if destination[0] < 0\
        or destination[1] < 0\
        or destination[0] > x-1\
        or destination[1] > y-1\
        or grid[destination[0]][destination[1]].ID == 1:#wallcell
            print("Bump")
        else:
            position = destination[:]
        return position
    move = moveoptions(direction)
    if move != " ":
        destination = position[:]
        destination[0] += move[0]
        destination[1] += move[1]
        position = detectcollision(position,destination)
        
    else:
        print("invalid input")
    return position
#----------------------------------------------------------

##----------------------------------------------------------


NewMap = grid(20, 20)
NewMap.create_random(80)
NewMap.print([])




