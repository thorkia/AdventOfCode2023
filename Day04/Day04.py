

def Part1(filename: str):
    with open(filename) as f:
        lines = [x.strip() for x in f.readlines()]
        f.close()
    
    totalPoints = 0
    for line in lines:
        line = line.split(':')
        game = line[1].split('|')

        winningNums = set([ int(x) for x in game[0].strip().split(' ') if x!=''])
        nums = set([ int(x) for x in game[1].strip().split(' ') if x!=''])

        matches = winningNums.intersection(nums)
        if len(matches) > 0:
            totalPoints += 2**(len(matches)-1)
    
    print(totalPoints)    


def Part2(filename: str):
    with open(filename) as f:
        lines = [x.strip()for x in f.readlines()]
        f.close()

    cardCounts = { }
    for x in range(len(lines)):
        cardCounts[x+1] = 1

    cardNum = 0
    for line in lines:
        cardNum+=1
        line = line.split(':')
        game = line[1].split('|')

        winningNums = set([ int(x) for x in game[0].strip().split(' ') if x!=''])
        nums = set([ int(x) for x in game[1].strip().split(' ') if x!=''])

        matches = winningNums.intersection(nums)
        for x in range(len(matches)):
            winCard = cardNum+x+1
            cardCounts[winCard] += cardCounts[cardNum]

    print(sum(cardCounts.values()))
    return False


if __name__ == '__main__':    
    
    #filename = './Day04/test_input.txt'    
    filename = './Day04/input.txt'    
    
    Part1(filename)
    Part2(filename)