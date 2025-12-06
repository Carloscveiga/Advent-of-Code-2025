from puzzleInput import puzzleInput

batteryStorage = []

puzzleInput = puzzleInput.split("\n")
initialValueA = 0
initialValueB = 0
index = 0

results = []

for battery in puzzleInput:

    for value in reversed(range(0, len(battery))):
        
        maxPos = len(battery) - 1
        currentValue = int(battery[value])
        maxValuePos = 0
        position = value
        
        if currentValue >= initialValueA and position != maxPos:
            initialValueA = currentValue
            index= value
            
    finalvalueA = initialValueA
    initialValueA = 0
    
    for value in reversed(range(index+1, len(battery))):
        
        currentValue = int(battery[value])
        position = value

        if currentValue > initialValueB and position != maxPos:
            initialValueB = currentValue
            
        if value == maxPos:
            if initialValueB < int(battery[maxPos]):
                initialValueB = int(battery[maxPos])
                
    finalvalueB =  initialValueB
    initialValueB = 0

    finalValue = int(str(finalvalueA) + str(finalvalueB))    
    results.append(finalValue)

print(sum(results)) 