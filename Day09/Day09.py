


def GetOasisReportNextValue(line: str) -> int:
    report = [ int(l) for l in line.split(' ')]
    
    lastValues = [ ]

    #Get the last value from every line as we calculate the rows   
    allZero = False
    while allZero == False:
        lastValues.append(report[-1])
        
        newReport = []
        allZero = True
        for x in range(1,len(report)):
            diff = report[x] - report[x-1]
            newReport.append(diff)
            if diff != 0:
                allZero = False        
        report = newReport
    
    return sum(lastValues)    


def Part1(filename: str):
    with open(filename) as f:
        lines = [x.strip() for x in f.readlines()]
        f.close()

    oasisValue = [ ]
    for line in lines:
        oasisValue.append(GetOasisReportNextValue(line))

    print(sum(oasisValue))
    return False


def GetOasisReportPrevValue(line: str) -> int:
    report = [ int(l) for l in line.split(' ')]
    
    firstValues = [ ]
    firstValue = report[0]
    #Get the last value from every line as we calculate the rows   
    allZero = False
    while allZero == False:        
        
        newReport = []
        allZero = True
        for x in range(1,len(report)):
            diff = report[x] - report[x-1]
            newReport.append(diff)
            if diff != 0:
                allZero = False

        report = newReport
        firstValues.append(report[0])
    
    for x in range(len(firstValues)-2,-1, -1):
        firstValues[x] = firstValues[x] - firstValues[x+1]

    return firstValue - firstValues[0]
    return firstValue - sum(firstValues)    

def Part2(filename: str):
    with open(filename) as f:
        lines = [x for x in f.readlines()]
        f.close()

    oasisValue = [ ]
    for line in lines:
        oasisValue.append(GetOasisReportPrevValue(line))

    print(sum(oasisValue))
    return False    


if __name__ == '__main__':    
    
    #filename = './Day09/test_input.txt'        
    filename = './Day09/input.txt'    
    
    Part1(filename)
    Part2(filename)