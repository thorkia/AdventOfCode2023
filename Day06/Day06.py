
def GetGames(time: str, dist: str) -> list[tuple[int,int]]:
    times = time.split(':')[1].strip()
    dists = dist.split(':')[1].strip()

    timelist = [ int(t) for t in times.split() if t !='' ]
    distlist = [ int(d) for d in dists.split() if d !='' ]

    return [ (timelist[x], distlist[x]) for x in range(len(timelist)) ]

#a win is recorded as the length held
def GetGameWins(game: tuple[int,int]) -> list[int]:
    wins = [ ]
    for h in range(game[0]+1):
        distance = h*(game[0]-h)
        if distance > game[1]:
            wins.append( (h,distance) )

    return wins

def Part1(filename: str):
    with open(filename) as f:
        lines = [x for x in f.readlines()]
        f.close()

    games = GetGames(lines[0], lines[1])
    
    score = 1
    for game in games:
        wins = GetGameWins(game)
        score *= len(wins)

    print(score)

    return False

def GetGame(time: str, dist: str) -> tuple[int,int]:
    times = time.split(':')[1].strip()
    dists = dist.split(':')[1].strip()

    time = int(times.replace(' ',''))
    dist = int(dists.replace(' ',''))
    
    return (time, dist)

def Part2(filename: str):
    with open(filename) as f:
        lines = [x for x in f.readlines()]
        f.close()

    game = GetGame(lines[0], lines[1])
    wins = GetGameWins(game)

    print(len(wins))
    return False


if __name__ == '__main__':    
    
    #filename = './Day06/test_input.txt'    
    filename = './Day06/input.txt'    
    
    Part1(filename)
    Part2(filename)