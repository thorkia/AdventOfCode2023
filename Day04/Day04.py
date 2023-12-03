

def Part1(filename: str):
    with open(filename) as f:
        lines = [x for x in f.readlines()]
        f.close()

    return False


def Part2(filename: str):
    with open(filename) as f:
        lines = [x for x in f.readlines()]
        f.close()

    return False


if __name__ == '__main__':    
    
    filename = './Day04/test_input.txt'    
    #filename = './Day04/input.txt'    
    
    Part1(filename)
    Part2(filename)