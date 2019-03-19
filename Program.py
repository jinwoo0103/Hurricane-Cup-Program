### Import CS Data files
Player_data = open('Player_data.csv', 'r')
Match_data = open('Match_data.csv', 'r')

### Read data from Player_data
name = []
team = []
th = []
train = []
no8_9 = []
no9_10 = []
count = []
injury = []

Player_data.readline()
for line in Player_data:
    temp = line.split(',')
    name.append(temp[0])
    team.append(temp[1])
    th.append(temp[2])
    train.append(temp[3])
    no8_9.append(temp[4])
    no9_10.append(temp[5])
    count.append(int(temp[6]))
    injury.append(temp[7])

### Read data from Match_data
b8_9 = []
b9_10 = []
n8_9 = []
n9_10 = []

round = input("Please enter Round: ")
if type(round) != int:
    print("Wrong Input.")
else:
    for i in range(round):
        Match_data.readline()
    temp = Match_data.readline().split(',')
    b8_9.append(temp[1])
    b8_9.append(temp[2])
    b9_10.append(temp[3])
    b9_10.append(temp[4])
    n8_9.append(temp[5])
    n8_9.append(temp[6])
    n9_10.append(temp[7])
    n9_10.append(temp[8])

print (name, team, th, train, no8_9, no9_10, count, injury)
print (b8_9, b9_10, n8_9, n9_10)
