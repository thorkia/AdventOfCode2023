from functools import cmp_to_key

cardValues = '23456789TJQKA'

def GetHandRank(hand: str):
    cards = { }
    for s in hand:
        if s in cards.keys():
            cards[s] = cards[s]+1
        else:
            cards[s] = 1
    
    if 5 in cards.values(): #five of a kind
        return 7
    elif 4 in cards.values(): #four of a kind
        return 6
    elif 3 in cards.values() and 2 in cards.values(): #full house
        return 5
    elif 3 in cards.values(): #three of a kind
        return 4
    elif len([ v for v in cards.values() if v==2]) == 2: #2 pairs
        return 3
    elif len([ v for v in cards.values() if v==2]) == 1: #1 pair
        return 2
    else:
        return 1

def CompareHandCards(hand1: str, hand2: str, cardVal: str):
    for x in range(len(hand1)):
        if cardVal.index(hand1[x]) < cardVal.index(hand2[x]):
            return -1
        if cardVal.index(hand1[x]) > cardVal.index(hand2[x]):
            return 1
    
    return 0

def CompareHands(hand1: tuple[str,int], hand2: tuple[str,int]):
    hand1Score = GetHandRank(hand1[0])
    hand2Score = GetHandRank(hand2[0])

    if hand1Score < hand2Score:
        return -1
    elif hand1Score == hand2Score:
        return CompareHandCards(hand1[0], hand2[0], cardValues)
    else:
        return 1

def Part1(filename: str):
    with open(filename) as f:
        lines = [x.strip() for x in f.readlines()]
        f.close()

    hands = [ (x.split(' ')[0],int(x.split(' ')[1])) for x in lines]
    hands.sort( key = cmp_to_key(CompareHands))    

    totalScore = 0
    for x in range(len(hands)):
        totalScore+= ( (x+1) * hands[x][1])
    
    print(totalScore)

    return False


cardValuesPart2 = 'J23456789TQKA'

def GetHandRankWithWildCard(hand: str):
    cards = { }
    for s in hand:
        if s in cards.keys():
            cards[s] = cards[s]+1
        else:
            cards[s] = 1

    #remove the J as that will impact the counts
    jCount = 0
    if 'J' in cards.keys():
        jCount = cards['J']
        cards.pop('J')
    
    if 5 in cards.values() or jCount == 5: #five of a kind
        return 7
    elif 4 in cards.values(): #four of a kind
        if jCount == 1: 
            return 7
        else:
            return 6
    elif 3 in cards.values() and 2 in cards.values(): #full house
        #we have 5 cards - it's impossible to have a J since I removed them
        return 5
    elif 3 in cards.values(): #three of a kind
        if jCount == 2: #3 of a kind becomes 5 of a kind
            return 7
        elif jCount == 1: #3 of a kind becomes 4 of a kind is higher than a full house
            return 6
        else:
            return 4
    elif len([ v for v in cards.values() if v==2]) == 2: #2 pairs
        if jCount == 1: #we can only have one J - which would make this a full house
            return 5
        else:
            return 3
    elif len([ v for v in cards.values() if v==2]) == 1: #1 pair
        if jCount == 3: #we have 5 of a kind
            return 7
        if jCount == 2: #we have 4 of a kind
            return 6
        if jCount == 1: #we have 3 of a kind
            return 4
        else:
            return 2
    else:
        if jCount == 4: #we have 5 of a kind
            return 7
        if jCount == 3: #we have 4 of a kind
            return 6
        if jCount == 2: #we have 3 of a kind - 3 is higher than 2 pair
            return 4
        if jCount == 1: #we have a pair
            return 2
        else:
            return 1

def CompareHandsWithWildcard(hand1: tuple[str,int], hand2: tuple[str,int]):
    hand1Score = GetHandRankWithWildCard(hand1[0])
    hand2Score = GetHandRankWithWildCard(hand2[0])

    if hand1Score < hand2Score:
        return -1
    elif hand1Score == hand2Score:
        return CompareHandCards(hand1[0], hand2[0], cardValuesPart2)
    else:
        return 1
    
def Part2(filename: str):
    with open(filename) as f:
        lines = [x for x in f.readlines()]
        f.close()

    hands = [ (x.split(' ')[0],int(x.split(' ')[1])) for x in lines]
    hands.sort( key = cmp_to_key(CompareHandsWithWildcard))    

    totalScore = 0
    for x in range(len(hands)):
        totalScore+= ( (x+1) * hands[x][1])

    print(totalScore)

    return False


if __name__ == '__main__':
    
    #filename = './Day07/test_input.txt'
    filename = './Day07/input.txt'
    
    Part1(filename)
    Part2(filename)