import GridMove
def LittleEndianToInt(Hex):
    byte = ""
    text = ""
    length = int(len(Hex))
    for i in range(int(length/2)):
        byte =  Hex[length-(i+1)*2:length-(i+1)*2+2]
        text = text + byte
    return(int(text,16))

def IntToLittleEndian(Integer):
    Hex = hex(Integer)
    Hex = Hex[2:] #trims off the "0x"
    length = len(Hex)
    string = ""
    if length % 2 == 1:
        Hex = "0" + Hex
        length = len(Hex) #adds a 0 to the last byte if length is odd number
    for i in range(int(length/2+1.5)):
        string = string + Hex[length - i*2:length - (i-1) * 2]
    return string
        

    
def CreateNewTwentyFourBit(grid):
    print("A file should be saved")
    NewBitmap = open("NewBitmap.bmp","wb")
    #Header
    cellwidth = 16
    fullhexstring = ""
    header = ""
    body = ""
    hexlist = []
    signature = "424d" #BM
    filesize =""
    reserved = "00000000"
    offbits = "32000000"
    headersize = "28000000"
    width = "" 
    height = "" 
    planes = "0100"
    bitcount = "1800"#24bit
    compression = "00000000"
    imagesize = ""
    Xpixelspermeter = "00000000"
    Ypixelspermeter = "00000000"
    clrused = "00000000"
    clrimportant = "00000000"

    width = IntToLittleEndian(grid.width*cellwidth)
    #could create a function for these
    for i in range(8- len(width)):
        width = width + "0" # fill in 0s
    height = IntToLittleEndian(grid.height*cellwidth)
    for i in range(8- len(height)):
        height = height + "0" # fill in 0s
    filesize = IntToLittleEndian((grid.width * grid.height)*cellwidth**2*3+54)
    for i in range(8- len(filesize)):
        filesize = filesize + "0" # fill in 0s
    imagesize = IntToLittleEndian((grid.width * grid.height)*cellwidth**2*3)
    for i in range(8- len(imagesize)):
        imagesize = imagesize + "0"
    
    header = signature+filesize+reserved+offbits+headersize+width+height+planes\
             +bitcount+compression+imagesize+Xpixelspermeter+Ypixelspermeter\
             +clrused+clrimportant 

    #Body
    for row in grid[::-1]:
        for cell in row:
            if cell.ID == 1:
                colorhex = "000000"
            else:
                colorhex = "ffffff"
            body = body + colorhex
##        body = body + "0000" #padding

    #Expand Body
    #Turns each cell into a cellwidth*cellwidth square
    expandedbody = ""
    for h in range(grid.height*cellwidth):
        for w in range(grid.width):
            expandedbody = expandedbody + body[(int(h/cellwidth)*grid.width)*6+w*6:\
                                        (int(h/cellwidth)*grid.width)*6+w*6+6]*cellwidth

    #Compile
    fullhexstring = header + expandedbody
    hexlist = [int(fullhexstring[i:i+2],16) for i in range(0, len(fullhexstring), 2)]
    array = bytearray(hexlist)
    NewBitmap.write(array)
    NewBitmap.close

grid = GridMove.grid(20,20)
grid.createrandom(400)
grid.print([])

CreateNewTwentyFourBit(grid)


#LittleEndianToInt(str(32000000))
