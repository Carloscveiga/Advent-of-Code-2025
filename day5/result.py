from puzzleInput import puzzleInput, puzzleInput2

ranges = [list(map(int, line.split('-'))) for line in puzzleInput2.splitlines() if '-' in line]
values = []
ranges.sort()
counter = 0

for i in range(len(ranges) - 1):

    if ranges[i][1] < ranges[i + 1][0]:
        values.append(ranges[i])
        
    else:
        ranges[i+1][0] = ranges[i][0]
        ranges[i+1][1] = max(ranges[i][1], ranges[i + 1][1])

values.append(ranges[-1])   

for value in values:
    counter += (value[1] - value[0]) +1
               
print(counter)



