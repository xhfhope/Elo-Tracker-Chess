                #loading database
                #get result
                #access database variables
                #send variables to method
                # 0 indicates draw, 1 indicates first player won, 2 indicates second player won
                #change ratings in database based on return and result
                #end loop
                #print(calculateRating(2400, 2350, 2));
import pickle                

# ---- Start Functions and Classes ----#
class Player:
    def __init__ (self, name, fullname, rating):
        self.name = name
        self.fullname = fullname
        self.rating = rating
        
def calculateRatingChange(p1,p2,winner):
    chances = {0:0.5, 25:0.54, 50:0.57, 75:.61, 100:.65, 125:.67, 150:.7, 175:.73, 200:.76, 225:.78, 250:.81, 275:.83, 300:.85, 325:.87, 350:.88, 375:.9, 400:.91, 425:.92, 450:.93, 475:.95}
    temp = 0;
    #ensured that p1 represents better player (or they are equal)
    if(p1 < p2):
        temp=p1
        p1=p2
        p2 = temp
        if(winner != 0):
            if(winner == 1):
                winner=2
            else:
                winner=1

    #establishing modifier to make lower rated games have lower elo changes 
    if(p1>=2000):
        modifier=1
    elif (p1>=1800):
        modifier=0.93
    elif (p1>=1300):
        modifier=.87
    elif (p1>=800):
        modifier=.8
    else:
        modifier=.67

    diff = p1-p2
    diff = mround(diff, 25)


    if (p1 != p2):        
        #returning if diff is >=500
        if (diff >= 500):
            if(winner==2):
                return 150
            if(winner==1):
                return 1
            if(winner==0):
                return 75
            
        #returning math based on win chance * modifier        
        chance = chances[diff]
        if winner == 1:
            print(str(chance) + ', ' + str(modifier))
            return (int)((100- (100* (chance))) * modifier)
        elif winner == 2:
            return (int)(100* (chance * modifier))
        elif winner==0:
            return (int)(100* (0.5 * chance * modifier))
    else:
            return (int)(50 * modifier)

def mround(x, base):
    return int(base * round(float(x)/base))

def addResultsAndWriteFile():
    players = {}
    import pickle
    fopen = input('Input file: ')
    with open (fopen, 'rb') as handle:
        players = pickle.load(handle)
        
    while(True):
        pla1 = (input('Input player one\'s id: '))
        pla2 = (input('Input player two\'s id: '))
        result = int(input('Who won? (1,2, 0 for draw): '))
        change=calculateRatingChange(players[pla1].rating, players[pla2].rating, result)
        if(result==1):
            players[pla1].rating = players[pla1].rating + change
            players[pla2].rating = players[pla2].rating - change
        if(result==2):
            players[pla1].rating = players[pla1].rating - change
            players[pla2].rating = players[pla2].rating + change
        if(result==0):
            if(players[pla1].rating > players[pla2].rating): #p1 better
                players[pla1].rating = players[pla1].rating - change
                players[pla2].rating = players[pla2].rating + change
            elif(players[pla1].rating < players[pla2].rating):
                players[pla1].rating = players[pla1].rating + change
                players[pla2].rating = players[pla2].rating - change
            else:
                print('Draw of even-rated players. No rating change')
                
        b = int(input('Done with adding results? 1 for yes, 2 for no: '))
        if(b==1):
            break



    fout = input('New file ready to be made. New database filename: ')

    with open(fout, 'wb') as handle:
      pickle.dump(players, handle)

    print('Done.')

def displayRatings():
    players = {}
    import pickle
    fopen = input('Input file: ')
    with open (fopen, 'rb') as handle:
        players = pickle.load(handle)


    

    
    leftWidth = 25
    rightWidth= 7
    print('\n\n\n' + 'MAV CHESS RATINGS'.center(leftWidth + rightWidth, '-') + '\n')
    alreadyListed = []
    for j in players:
        highest = 400
        for i in players:
            if(players[i].rating>highest and players[i].fullname not in alreadyListed):
                highest = players[i].rating
                nameOfHighest = players[i].fullname
                rOfHighest = players[i].rating
        alreadyListed.append(nameOfHighest)
        #print(alreadyListed)
        print(nameOfHighest.ljust(leftWidth, '.') + str(rOfHighest).rjust(rightWidth))
    print()

def makeManualChange():
    players = {}

    import pickle
    fopen = input('Input file: ')
    with open (fopen, 'rb') as handle:
        players = pickle.load(handle)
    #vvvvvvvvv   MANUAL CHANGE SECTION    vvvvvvvvv




    #^^^^^^^^^   MANUAL CHANGE SECTION    ^^^^^^^^^

    fout = input('New file ready to be made. New database filename: ')

    with open(fout, 'wb') as handle:
          pickle.dump(players, handle)

# ---- End Functions and Classes ----#
#makeManualChange()
while True:
    choice = input('1. Input results and write to new file\n2.Display ratings\n3.Exit\n\n>>>')
    if choice == '1':
        addResultsAndWriteFile()
    if choice == '2':
        displayRatings()
    if choice == '3':
        break
