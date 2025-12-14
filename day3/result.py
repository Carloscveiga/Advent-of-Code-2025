from puzzleInput import puzzleInput

puzzleInput2 = """987654321111111
811111111111119
234234234234278
818181911112111"""

batteryStorage = []

puzzleInput = puzzleInput.split("\n")
initialValueA = 0
initialValueB = 0
index = 0

results = []

"""

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
            
        if position == maxPos:
            if initialValueB < int(battery[maxPos]):
                initialValueB = int(battery[maxPos])
                
    finalvalueB =  initialValueB
    initialValueB = 0

    finalValue = int(str(finalvalueA) + str(finalvalueB))    
    results.append(finalValue)

print(sum(results)) 

"""

#Part 2

maxBatInitialValue = 0
maxBatteryValue = ""


for battery in puzzleInput:

    for value in range(0, 89):
        
        if int(battery[value]) > maxBatInitialValue:
            maxBatInitialValue = int(battery[value])
            position = value
    
    maxInitialvalue = maxBatInitialValue
    maxBatteryValue = maxBatteryValue + str(maxBatInitialValue)
    battery = battery[position+1:]
    maxBatInitialValue = 0
    
    while len(str(maxBatteryValue)) < 12:
        
        currentMaxValue = 0
        
        for i in range (len(battery)):
            if int(battery[i]) > currentMaxValue and ((len(battery) - (i +1))) + (len(str(maxBatteryValue))+1) >=12 :
                currentMaxValue = int(battery[i])
                position = i
                                
        maxBatteryValue += str(currentMaxValue) 
        battery = battery[position+1:]
        
    results.append(int(maxBatteryValue))
    maxBatteryValue =""
print(sum(results))
    
