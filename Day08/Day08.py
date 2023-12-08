import math

def GetNodes(lines: list[str]) -> dict[str,tuple[str,str]]:
    nodes = { }
    for line in lines:
        splitLine = line.split('=')
        node = splitLine[0].strip()
        lrInstruction = splitLine[1].strip().split(',')

        nodes[node] = (lrInstruction[0][1::].strip(), lrInstruction[1][:-1].strip())
    
    return nodes


def Part1(filename: str):
    with open(filename) as f:
        lines = [x for x in f.readlines()]
        f.close()

    instructions = lines[0].strip()
    nodes= GetNodes(lines[2:])
    sideToIndex = { 'L': 0, 'R': 1 }

    currentNode = 'AAA'
    steps = 0
    while currentNode != 'ZZZ':
        side = instructions[ steps % len(instructions) ]
        currentNode = nodes[currentNode][sideToIndex[side]]
        steps+=1

    print(steps)
    return False


def Part2(filename: str):
    with open(filename) as f:
        lines = [x for x in f.readlines()]
        f.close()    

    instructions = lines[0].strip()
    nodes= GetNodes(lines[2:])
    sideToIndex = { 'L': 0, 'R': 1 }

    startNodes = [n for n in nodes if n[-1]=='A'] #get all the items ending in A for start node
    nodesSteps = [ ]
    
    for start in startNodes:        
        steps = 0
        currentNode = start
        while currentNode[-1] != 'Z':
            side = instructions[ steps % len(instructions) ]
            currentNode = nodes[currentNode][sideToIndex[side]]
            steps+=1
        
        nodesSteps.append(steps)

    #getLCM
    print(math.lcm(*nodesSteps))

    return False


if __name__ == '__main__':    
    
    #filename = './Day08/test_input3.txt'    
    filename = './Day08/input.txt'    
    
    Part1(filename)
    Part2(filename)