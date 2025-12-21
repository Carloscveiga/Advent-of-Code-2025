from puzzleInput import puzzleInput, puzzleInput2

#Part 1

puzzle = puzzleInput2
sequence = [[0 if c == '.' else 1 if c == 'S' else '^' for c in line.strip()] for line in puzzle.splitlines() if line.strip()]
height, width = len(sequence), len(sequence[0])
rollingArray = [0]*width
paths = 0 
for i in range(height):
    for j in range(width):
        if i == 0 and sequence[i][j] == 1 :
            rollingArray[j] = 1
        elif sequence[i][j] == '^':
            if rollingArray[j] > 0:
                paths +=1
            rollingArray[j-1] += rollingArray[j]
            rollingArray[j+1] += rollingArray[j]
            rollingArray[j] = 0

print(paths)

#Part 2

print(sum(rollingArray))