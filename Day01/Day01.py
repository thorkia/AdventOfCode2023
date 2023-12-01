import types
import typing


def Part1(filename: str):
    with open(filename) as f:
        lines = [x.strip() for x in f.readlines()]
        f.close()
    
    total = 0
    for l in lines:
        nums = [int(x) for x in l if x.isnumeric()]
        total+= nums[0]*10 + nums[-1]

    print(total)
   

mapping = { "one" : "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}

def ReplaceFirstLast(line: str) -> str:
    newLine = line
    #Do First One
    foundItems = [ (line.find(k),k) for k,v in mapping.items() if line.find(k) != -1 ]
    if len(foundItems) > 0:
        first = min(foundItems, key = lambda t: t[0])
        #Only replace the first item found if a digit comes before it
        if len([x for x in line[:first[0]] if x.isnumeric()]) == 0:
            newLine = line.replace(first[1], mapping[first[1]], 1)
    
    #Do Last One
    foundItems = [ (line.rfind(k),k) for k,v in mapping.items() if line.find(k) != -1 ]
    if len(foundItems) > 0:
        last = max(foundItems, key = lambda t: t[0])

        #reverse the line and revers the find string.  replace first occurance, then reverse the string back
        newLine = newLine[::-1].replace(last[1][::-1], mapping[last[1]],1)[::-1]

    return newLine

def Part2(filename: str):
    with open(filename) as f:
        lines = [ReplaceFirstLast(x.strip()) for x in f.readlines()]
        f.close()

    total = 0
    for l in lines:
        nums = [int(x) for x in l if x.isnumeric()]
        print(str(nums[0]*10 + nums[-1]))
        total+= nums[0]*10 + nums[-1]

    print(total)


if __name__ == '__main__':    
    
    #filename = './Day01/test_input.txt'
    #filename = './Day01/test_input2.txt'
    filename = './Day01/input.txt'    
    
    Part1(filename)
    Part2(filename)