from puzzleInput import list

sequence = [int(line.strip().replace("R", "").replace("L", "-")) for line in list.splitlines() if line.strip()]

counter = 0
start= 50
current = start


for _ in sequence:
    
    prev = current
    
    if _ < 0 :
        quot, reminder = divmod(_ , -100)
        counter += quot
        if current != 0 and prev + reminder < 0:
            counter += 1

    if _ > 0 :
        quot, reminder = divmod(_, 100)
        counter += quot
        if current + reminder > 100:
            counter += 1
            
    current = (prev + _) % 100
    if current == 0:
        counter += 1

    print(f"{prev} -> {current}, quot = {quot} , reminder = {reminder}")

print(f"counter = {counter}")