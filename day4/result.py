from puzzleInput import puzzleInput, puzzleInput2

sequence = [list(line.strip().replace("@", "1").replace(".", "0")) for line in puzzleInput2.splitlines() if line.strip()]
offsetRanges = [[-1, -1], [-1,  0], [-1,  1],[ 0, -1], [0,  1],[ 1, -1], [ 1,  0], [1,  1]]
finalCounter = []
height = len(sequence)
width  = len(sequence[0])
remainingStacks = True  

while remainingStacks == True:
    
    globalCounter = 0
    to_remove = [] 

    for row in range(height):
        for col in range(width):

            if sequence[row][col] == "1":

                localCounter = 0

                for offSetRow, offsetcol in offsetRanges:
                    newRow = row + offSetRow
                    newCol = col + offsetcol
                    
                    if 0 <= newRow < height and 0 <= newCol < width:
                        if sequence[newRow][newCol] == "1":
                            localCounter += 1

                if localCounter <= 3:
                    to_remove.append((row, col))

    for row, col in to_remove:
        sequence[row][col] = "0"
        globalCounter += 1
        
    finalCounter.append(globalCounter)
    if globalCounter <= 0:
        remainingStacks = False
            
print(sum(finalCounter))

"""

sequence = [list(line.strip().replace("@", "1").replace(".", "0")) for line in puzzleInput.splitlines() if line.strip()]
copySequence = [row[:] for row in sequence]
finalCounter =[]
globalCounter= 1
bottom= len(sequence)
left = 0
right = len(sequence[0])

while globalCounter > 0:
    
    globalCounter= 0
    top = 0
    
    while top < bottom:
        
        for i in range(left, right):
            
            localCounter = 0
            
            if sequence[top][i] == str(1):

                if top -1 >= 0:
                    if i == 0 :
                        if sequence[top-1][i] == str(1):
                            localCounter +=1
                        if sequence[top-1][i+1] == str(1):
                            localCounter +=1                           
                    elif i == len(sequence[0])-1:
                        if sequence[top-1][i-1] == str(1):
                            localCounter +=1
                        if sequence[top-1][i] == str(1):
                            localCounter +=1          
                    else:
                        if sequence[top-1][i-1] == str(1):
                            localCounter +=1
                        if sequence[top-1][i] == str(1):
                            localCounter +=1
                        if sequence[top-1][i+1] == str(1):
                            localCounter +=1              
                
                if i == 0:
                    if sequence[top][i+1] == str(1):
                        localCounter +=1
                elif i == len(sequence[0])-1:
                    if sequence[top][i-1] == str(1):
                        localCounter +=1 
                else:
                    if sequence[top][i-1] == str(1):
                        localCounter +=1        
                    if sequence[top][i+1] == str(1):
                        localCounter +=1
                
                if top + 1 < len(sequence):
                    if i == 0:
                        if sequence[top+1][i] == str(1):
                            localCounter +=1
                        if sequence[top+1][i+1] == str(1):
                            localCounter +=1
                    elif i == len(sequence[0])-1:
                        if sequence[top+1][i-1] == str(1):
                            localCounter +=1
                        if sequence[top+1][i] == str(1):
                            localCounter +=1    
                    else:
                        if sequence[top+1][i-1] == str(1):
                            localCounter +=1
                        if sequence[top+1][i] == str(1):
                            localCounter +=1             
                        if sequence[top+1][i+1] == str(1):
                            localCounter +=1 

                if localCounter <= 3 :
                    globalCounter += 1
                    copySequence[top][i] = '0'                        
                localCounter = 0
                
        top +=1 
                  
    finalCounter.append(globalCounter)
    sequence = [row[:] for row in copySequence]

print(sum(finalCounter))

"""