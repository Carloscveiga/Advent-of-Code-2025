
from puzzleInput import puzzleInput

ranges  = puzzleInput.split(",")
wrongIds = []


"""

#Part 1

for r in ranges:
    sequence = [int(x) for x in r.split("-")]
    
    for value in range(sequence[0], sequence[1] + 1):
        if len(str(value)) % 2 == 0 and int(str(value)[:len(str(value)) // 2]) == int(str(value)[len(str(value)) // 2:]): 
            wrongIds.append(value) 


print(wrongIds)
print("Final counter:", sum(wrongIds))

"""


#Part 2:


for r in ranges:
    sequence = [int(x) for x in r.split("-")]
    
    for value in range(sequence[0], sequence[1] + 1):      
        
        for i in range(1, len(str(value))+1):
            
            if len(str(value)) % i == 0 and i != 1:
                
                check = True
                div = i
                
                if div == len(str(value)):
                    for i in range(1, len(str(value))):
                        if str(value)[i] != str(value)[0] :
                            check = False
                    if check == True and value not in wrongIds:
                        wrongIds.append(value)
            
                if div < len(str(value)) and div > 1:
                    
                    for i in range(1, len(str(value)) // div):
                        if str(value)[i*div:(i+1)*div] != str(value)[:div]:
                            check = False
                    if check == True and value not in wrongIds:
                        wrongIds.append(value)         
        
    
print(wrongIds)
print("Final counter:", sum(wrongIds))