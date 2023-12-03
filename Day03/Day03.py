

def GetNeighbours(locY: int, locX: int, maxY: int, maxX: int) -> list[tuple[int, int]]:
    coords = [ ]
    
    coords.append( (locY-1, locX-1) )#al
    coords.append( (locY-1, locX) )#a
    coords.append( (locY-1, locX+1) )#ar

    coords.append( (locY, locX-1) )#l
    coords.append( (locY, locX+1) )#r
    
    coords.append( (locY+1, locX-1) )#bl
    coords.append( (locY+1, locX) )#b
    coords.append( (locY+1, locX+1) )#br

    return [ c for c in coords if c[0]>=0 and c[0]<maxY and c[1]>=0 and c[1]<maxX ]


def IsPartNumber(lines:list[str], neighbours: list[tuple[int, int]]) -> bool:
    for n in neighbours:
        if lines[n[0]][n[1]] != '.' and lines[n[0]][n[1]].isdigit() == False:
            return True

    return False


def Part1(filename: str):
    with open(filename) as f:
        lines = [x.strip() for x in f.readlines()]
        f.close()

    maxY = len(lines)
    maxX = len(lines[0])

    sumPart = 0
    for y in range(0, maxY):
        number = ''
        isPart = False
        for x in range(0, maxX):            
            if lines[y][x].isnumeric():
                number = number + lines[y][x]                
                if IsPartNumber(lines, GetNeighbours(y,x,maxY,maxX)):
                    isPart = True
            else:
                if isPart:                    
                    sumPart+=int(number)                
                isPart=False
                number = ''
        if isPart: #if the line ends - need to check if its a part and include it
            sumPart+=int(number)
        
    
    print(sumPart)    


def IsGear(lines:list[str], neighbours: list[tuple[int, int]]) -> bool:
    for n in neighbours:
        if lines[n[0]][n[1]] == '*':
            return True

    return False

def GetStarLoc(lines:list[str], neighbours: list[tuple[int, int]]) -> tuple[int,int]:
    for n in neighbours:
        if lines[n[0]][n[1]] == '*':
            return n

    return (-1,-1)

def Part2(filename: str):
    with open(filename) as f:
        lines = [x.strip() for x in f.readlines()]
        f.close()
    
    maxY = len(lines)
    maxX = len(lines[0])

    stars = { }
    #Get stars
    for y in range(0, maxY):                
        for x in range(0, maxX):
            if lines[y][x] == '*':
                if (y,x) not in stars:
                    stars[(y,x)] = [ ]

    #like part 1 - find a number - but only count it if its beside a star
    for y in range(0, maxY):
        number = ''
        isGear = False
        starloc = (-1,-1)
        for x in range(0, maxX):            
            if lines[y][x].isnumeric():
                number = number + lines[y][x]
                neigh = GetNeighbours(y,x,maxY,maxX)           
                if IsGear(lines, neigh):
                    isGear = True
                    starloc = GetStarLoc(lines, neigh)
            else:
                if isGear:
                    stars[starloc].append(int(number))
                isGear=False
                number = ''
                starloc = (-1,-1)
        if isGear: #if the line ends - need to check if its a gear and include it            
            stars[starloc].append(int(number))

    validGears = [ g for g in stars.values() if len(g) == 2]
    print(sum( [ g[0]*g[1] for g in validGears ]))
    
    
    return False

if __name__ == '__main__':    
    
    #filename = './Day03/test_input.txt'    
    filename = './Day03/input.txt'

    Part1(filename)
    Part2(filename)