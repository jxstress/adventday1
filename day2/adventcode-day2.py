def processGame(game,rule):
    gameRounds = games[1].split(';')
    
    for game in gameRounds:
        gameElement = game.strip().split(',')
        for element in gameElement:
            cube = element.strip().split(' ')
            if (cube[1] in cubesAllowed):
                if int(cube[0]) <= rule[cube[1]]:
                    continue
                else:
                    return False
    return True


cubesAllowed  = {'red':12, 'green':13, 'blue':14}
sumNumbers = 0

with open("puzzle-input-day2.txt", "r") as file:
    # Read the contents of the file
    for line in file:
        
        games = line.strip().split(':')
        gameNum = int(games[0].split(' ')[1])
        if processGame (games, cubesAllowed):
            sumNumbers += gameNum    

print (sumNumbers)
    
#Answer 2317