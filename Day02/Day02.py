

def GetGameId(line:str) -> int:
    return int(line.split(':')[0].replace("Game", "").strip())
   
def IsValidPull(line:str, limits:dict[str,int]) -> bool:
    pulls = line.split(":")[1].split(';')
    for pull in pulls:
        cubes = [ (c.strip().split(" ")[1], int(c.strip().split(" ")[0]) ) for c in  pull.split(',')]
        for cube in cubes:
            if cube[1] > limits[cube[0]]:
                return False
            
    return True

def GetGamePower(line:str) -> int:
    colours = { }

    pulls = line.split(":")[1].split(';')
    for pull in pulls:
        cubes = [ (c.strip().split(" ")[1], int(c.strip().split(" ")[0]) ) for c in  pull.split(',')]
        for cube in cubes:
            if cube[0] in colours.keys():
                if  cube[1]>colours[cube[0]]:
                    colours[cube[0]] = cube[1]
            else:
                colours[cube[0]] = cube[1]
    
    prod = 1
    for v in colours.values():
        prod *= v
    
    return prod


def Part1(filename: str):
    limits = { "red": 12, "green": 13, "blue": 14}
    with open(filename) as f:
        lines = [x for x in f.readlines()]
        f.close()

    total = 0
    for line in lines:
        if IsValidPull(line, limits):
            total += GetGameId(line)

    print(total)


def Part2(filename: str):
    with open(filename) as f:
        lines = [x for x in f.readlines()]
        f.close()

    total = 0
    for line in lines:
        val = GetGamePower(line)        
        total+=val
    
    print(total)
    return False


if __name__ == '__main__':    
    
    #filename = './Day02/test_input.txt'    
    filename = './Day02/input.txt'    
    
    Part1(filename)
    Part2(filename)