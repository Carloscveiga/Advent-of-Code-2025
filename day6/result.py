from puzzleInput import puzzleInput, puzzleInput2

ranges = puzzleInput2.split("\n")
problems = ''

for j in range(len(ranges[0])-1, -1, -1):
    for i in range(0, len(ranges)):
        if ranges[i][j] in "+*":
            problems += ' ' + ranges[i][j]
        else:
            problems += ranges[i][j]
            
start = 0
seq=[]
for i in range(len(problems)):
    if problems[i] in "+*":
        chunk = problems[start:i+1]
        seq.append(chunk.split())
        start = i + 1
        
results=0

for problem in seq:
    results += eval(problem[-1].join(problem[:-1]))

print(results)

"""

Part 2

ranges = puzzleInput.split("\n")
height = len(ranges)
width = len(ranges[0])
problems = ''

for j in range(width-1, -1, -1):
    for i in range(0, height):
        if ranges[i][j] in "+*":
            problems += ' ' + ranges[i][j]
        else:
            problems += ranges[i][j]
            
start = 0
seq=[]
for i in range(len(problems)):
    if problems[i] in "+*":
        chunk = problems[start:i+1]
        seq.append(chunk.split())
        start = i + 1

newheight = len(seq)
problemsFinal = []

for i in range(0, newheight):
    values = []
    for j in range(0, len(seq[i])):
        print(seq[i][j])
        values.append(seq[i][j])
 
    if values[-1] == '+':
        result =  sum(map(int, values[:-1]))
        problemsFinal.append(result)
        
    if values[-1] == '*':
        product = 1
        for i in map(int, values[:-1]) :
            product *= i
            result = product
        problemsFinal.append(result)
    
print(sum(problemsFinal))         



Part 1

ranges = [list(line.split()) for line in puzzleInput2.splitlines()]
height = len(ranges)
width = len(ranges[-1])
problems = []

for i in range(0, width):
    values = []
    for j in range(0, height):
        values.append(ranges[j][i])
 
    if values[-1] == '+':
        result =  sum(map(int, values[:-1]))
        problems.append(result)
        
    if values[-1] == '*':
        product = 1
        for i in map(int, values[:-1]) :
            product *= i
            result = product
        problems.append(result)
    
print(sum(problems))

"""