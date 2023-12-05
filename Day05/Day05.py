

#destination / source / range
#seed to soul -> soil / seed / range
def GetRawMaps(lines:list[str],start:int) -> list[tuple[int, int, int]]:
    maps = [ ]
    
    while start+1 < len(lines) and lines[start+1].strip() != '':
        start+=1
        items = lines[start].split(' ')
        maps.append( ( int(items[0]),int(items[1]),int(items[2]) ) )

    return maps

def GetAllMaps(lines:list[str]) -> dict[int,list[tuple[int, int, int]]]:
    seedMaps = { }

    for x  in range(1,len(lines)):
        if 'to-soil' in lines[x]:
            #seedToSoil = GetRawMaps(lines, x)
            seedMaps[0] = GetRawMaps(lines, x)
        elif 'to-fertilizer' in lines[x]:
            soilToFertilizer = GetRawMaps(lines, x)
            seedMaps[1] = GetRawMaps(lines, x)
        elif 'to-water' in lines[x]:
            fertilizerToWater = GetRawMaps(lines, x)
            seedMaps[2] = GetRawMaps(lines, x)
        elif 'to-light' in lines[x]:
            waterToLight = GetRawMaps(lines, x)
            seedMaps[3] = GetRawMaps(lines, x)
        elif 'to-temperature' in lines[x]:
            lightToTemp = GetRawMaps(lines, x)
            seedMaps[4] = GetRawMaps(lines, x)
        elif 'to-humidity' in lines[x]:
            tempToHumidity = GetRawMaps(lines, x)
            seedMaps[5] = GetRawMaps(lines, x)
        elif 'to-location' in lines[x]:
            humidityToLoc = GetRawMaps(lines, x)
            seedMaps[6] = GetRawMaps(lines, x)
    
    return seedMaps


def GetSeeds(line:str) -> list[int]:
    return [ int(x) for x in line.split(':')[1].strip().split(' ')]

def GetNewPosition(currentLoc:int, seedMap:list[tuple[int, int, int]]) -> int:

    for dest, source, num in seedMap:
        if currentLoc >= source and currentLoc < source+num:
            return dest + (currentLoc-source)

    return currentLoc

def Part1(filename: str):
    with open(filename) as f:
        lines = [x for x in f.readlines()]
        f.close()

    #get seeds
    seeds = GetSeeds(lines[0])
    
    seedMaps = { }

    seedMaps = GetAllMaps(lines)
    #check seed locations next
    loc = [ ]
    for s in seeds:
        currentLoc = s
        for k in seedMaps.keys():
            currentLoc = GetNewPosition(currentLoc, seedMaps[k])

        loc.append(currentLoc)

    print( min(loc) )
    return False


def ConvertSeedToRanges(seeds:list[int]) -> list[tuple[int,int]]:
    seedRanges = []
    for x in range(0,len(seeds),2):
        seedRanges.append( (seeds[x], seeds[x+1]) )
    
    return seedRanges

def GetOverlappingRanges(seedRange:tuple[int,int], seedMaps:tuple[int,int,int]) -> list[tuple[int,int]]:
    newRanges = [ ]
    for dest, source, range in seedMaps:
        if seedRange[0] >= source or seedRange[0]<(source+range):
            #we overlap

    return newRanges

def Part2(filename: str):
    with open(filename) as f:
        lines = [x for x in f.readlines()]
        f.close()


    #get seeds
    seeds = GetSeeds(lines[0]) #change this to ranges
    seedRanges = ConvertSeedToRanges(seeds)
    
    seedMaps = { }
    seedMaps = GetAllMaps(lines)

    for k in seedMaps.keys():
        loc = [ ]
        for s in seedRanges:
            #change this to take the seed range and get a set of ranges back that in the new seedMap
            currentLoc = GetNewPosition(currentLoc, seedMaps[k]) 
            loc.extend(currentLoc)

        seedRanges = loc #replace the starting seed ranges with the new ranges


    print( min(loc) )
    return False


if __name__ == '__main__':    
    
    #filename = './Day05/test_input.txt'    
    filename = './Day05/input.txt'    
    
    Part1(filename)
    Part2(filename)