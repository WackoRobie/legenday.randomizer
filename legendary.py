import random
#
# Read card files into respective lists
#
with open('heros.txt') as tempFile:
    heros = [line.rstrip('\n') for line in tempFile]
with open('masterminds.txt') as tempFile:
    masterminds = [line.rstrip('\n') for line in tempFile]
with open('villains.txt') as tempFile:
    villains = [line.rstrip('\n') for line in tempFile]
with open('henchmen.txt') as tempFile:
    henchmen = [line.rstrip('\n') for line in tempFile]
with open('schemes.txt') as tempFile:
    schemes = [line.rstrip('\n') for line in tempFile]
#
# Get the number of players from user
#
print
players = None
while not players:
    try:
        players = int(raw_input('How many players?'))
    except:
        print 'Invalid entry'
print
#
# Determine Heros depending on the number of players without picking same hero more than once
#
sourceList = heros
heroList = []
if players<5:
    count=5
else:
    count=6
while count > 0:
    heroX = random.choice(sourceList)
    heroList.append(heroX)
    sourceList.remove(heroX)
    count = count - 1
#
# Print chosen heros
#
count = len(heroList)
while count>0:
    print "Hero #"+ (str(len(heroList)+1-count)) + ": " + heroList[(len(heroList)-count)]
    count = count - 1
#
# Pick and print Mastermind
#
mastermind = random.choice(masterminds)
print
print 'Mastermind: ' + mastermind
#
# Pick Villain groups
#
villainSource = villains
villainList = []
#if mastermind = "Dr Doom":
#    villianList.append(
if players < 3:
    count = 2
elif players > 4:
    count = 4
else:
    count = 2
while count > 0:
    villainX = random.choice(villainSource)
    villainList.append(villainX)
    villainSource.remove(villainX)
    count = count - 1
#
# Print villain groups
#
count = len(villainList)
while count>0:
    print "Villain Group #" + str(len(villainList)+1-count) + ": " + villainList[(len(villainList)-count)]
    count = count - 1
#
# Pick Henchman groups
#
henchSource = henchmen
henchList = []
if players < 4:
    count = 1
else:
    count = 2

while count > 0:
    henchX = random.choice(henchSource)
    henchList.append(henchX)
    henchSource.remove(henchX)
    count = count -1
#
# Print Henchmen groups
#
count = len(henchList)
while count>0:
    print "Henchmen Group #" + str(len(henchList)+1-count) + ": " + henchList[len(henchList)-count]
    count = count - 1
#
# Pick and print scheme
#
print
print "Scheme: " + random.choice(schemes)
print
