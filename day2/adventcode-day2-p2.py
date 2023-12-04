def processGame(game,rule):
    gameRounds = games[1].split(';')
    
    for game in gameRounds:
        gameElement = game.strip().split(',')
        for element in gameElement:
            cube = element.strip().split(' ')
            if (cube[1] in rule):
                if int(cube[0]) > rule[cube[1]]:
                   rule[cube[1]] = int(cube[0])
    
    powerSum = 1
    for value in rule.values():
        powerSum *= value
        
    return powerSum

#cubesAllowed  = {'red':12, 'green':13, 'blue':14}
sumNumbers = 0

with open("puzzle-input-day2.txt", "r") as file:
    # Read the contents of the file
    for line in file:
        cubesAllowed  = {'red':0, 'green':0, 'blue':0}
        games = line.strip().split(':')
        gameNum = int(games[0].split(' ')[1])
        sumNumbers += processGame (games, cubesAllowed)

print (sumNumbers)
    
#Answer 74804