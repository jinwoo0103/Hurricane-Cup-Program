### Import two data files
Player_data = open('Player_data.csv', 'r', encoding = 'utf-8')
Match_data = open('Match_data.csv', 'r', encoding = 'utf-8')

### Define function sort: list sort with Player's count
def sort(li):
    list_length = len(li)
    for i in range(list_length-1):
        for j in range(list_length-i-1):
            if li[j].count > li[j+1].count:
                li[j], li[j+1] = li[j+1], li[j]

### Define function count_included: count how much the Player is included in
def count_included(player):
    result = 0
    for i in m:
        if player in i.main_ref:
            result += 1
        if player in i.assi_ref:
            result += 1
        if player in i.wait_ref:
            result += 1
        if player in i.video:
            result += 1
    return resul

### Define function find_delete: find where the player is included and delete all
def find_delete(player):
    for i in m:
        if player in i.main_ref[32]:
            i.main_ref[32].remove(player)
        if player in i.assi_ref[33]:
            i.assi_ref[33].remove(player)
        if player in i.assi_ref[32]:
            i.assi_ref[32].remove(player)
        if player in i.wait_ref[34]:
            i.wait_ref[34].remove(player)
        if player in i.wait_ref[33]:
            i.wait_ref[33].remove(player)
        if player in i.video[34]:
            i.video[34].remove(player)

### Make class Player
class Player:
    def __init__(self):
        self.name = ""
        self.team = ""
        self.th = 0
        self.train_dept = False
        self._8_9 = True
        self._9_10 = True
        self.count = 0
        self.injury = False

### Read data from Player_data

p = []

Player_data.readline()
for line in Player_data:
    player = Player()
    temp = line.split(',')
    player.name = temp[0]
    player.team = temp[1]
    player.th = int(temp[2])
    if temp[3] == 'O':
        player.train_dept = True
    if temp[4] == 'X':
        player._8_9 = False
    if temp[5] == 'X':
        player._9_10 = False
    player.count = int(temp[6])
    if temp[7].strip('\n') == 'O':
        player.injury = True
    p.append(player)

### Make class Match
class Match:
    def __init__(self):
        self.team = []
        self.time = ()
        self.place = ""
        self.main_ref = {"Final": [], 32: []}
        self.assi_ref = {"Final": [], 33: [], 32: []}
        self.wait_ref = {"Final": [], 34: [], 33: []}
        self.video = {"Final": [], 34: []}
        self.carry = {"Final": [], 34: []}

### Read data from Match_data
m1 = Match()
m2 = Match()
m3 = Match()
m4 = Match()

m = [m1, m2, m3, m4]

round = int(input("Please Enter Round: "))
for i in range(round):
    Match_data.readline()
temp = Match_data.readline().split(',')
m1.team.append(temp[1])
m1.team.append(temp[2])
m2.team.append(temp[3])
m2.team.append(temp[4])
m3.team.append(temp[5])
m3.team.append(temp[6])
m4.team.append(temp[7])
m4.team.append(temp[8].strip('\n'))

m1.time = (8,9)
m1.place = "B"
m2.time = (9,10)
m2.place = "B"
m3.time = (8,9)
m3.place = "N"
m4.time = (9,10)
m4.place = "N"

####################################################################################

### Remember Time of 허리케인 Team
for i in m:
    if "허리케인A" in i.team:
        time_A = i.time
    if "허리케인B" in i.team:
        time_B = i.time


### Add players to match considering (th, _8_9, _9_10, team_schedule)
for i in m:
    for j in p:
        if True or (not j.injury):  ## Do not consider injuries yet
            if j.th == 32:
                if ((i.time == (8,9) and j._8_9) or (i.time == (9,10) and j._9_10)): ## If time is okay
                    if (j.team == "허리케인A" and i.time != time_A) or (j.team == "허리케인B" and i.time != time_B): ## If team schedule is okay
                        i.main_ref[32].append(j)
                        i.assi_ref[32].append(j)
            elif j.th == 33:
                if ((i.time == (8,9) and j._8_9) or (i.time == (9,10) and j._9_10)):
                    if (j.team == "허리케인A" and i.time != time_A) or (j.team == "허리케인B" and i.time != time_B):
                        i.assi_ref[33].append(j)
                        i.wait_ref[33].append(j)
            else:
                if ((i.time == (8,9) and j._8_9) or (i.time == (9,10) and j._9_10)):
                    if (j.team == "허리케인A" and i.time != time_A) or (j.team == "허리케인B" and i.time != time_B):
                        if j.train_dept: ## only train_dept do those two.
                            i.wait_ref[34].append(j)
                            if ("허리케인A" in i.team) or ("허리케인B" in i.team):
                                i.video[34].append(j)

### Sort every match's list
for i in m:
    sort(i.main_ref[32])
    sort(i.assi_ref[33])
    sort(i.assi_ref[32])
    sort(i.wait_ref[34])
    sort(i.wait_ref[33])
    sort(i.video[34])

### Choose main_ref
for i in m:
    if not "허리케인A" in i.team:
        if i.main_ref[32]:
            i.main_ref["Final"].append(i.main_ref[32][0])
            find_delete(i.main_ref[32][0])
        if len(i.main_ref["Final"]) == 1:
            print("Successfully choosed main_ref of %s :D" % (i.place + " " + str(i.time)))
        elif len(i.main_ref["Final"]) == 0:
            print("There's no player who can be the main_ref of %s T_T" % (i.place + " " + str(i.time)))
        else:
            print("It's a program error when choose the main_ref of %s T_T" % (i.place + " " + str(i.time)))

### Choose assi_ref:
for i in m:
    if not "허리케인A" in i.team:
        for j in range(2):
            if i.assi_ref[33]:
                i.assi_ref["Final"].append(i.assi_ref[33][0])
                find_delete(i.assi_ref[33][0])
            elif i.assi_ref[32]:
                i.assi_ref["Final"].append(i.assi_ref[32][0])
                find_delete(i.assi_ref[32][0])
        if len(i.assi_ref["Final"]) == 2:
            print("Successfully choosed assi_ref of %s :D" % (i.place + " " + str(i.time)))
        elif len(i.assi_ref["Final"]) < 2:
            print("There's no player who can be the assi_ref of %s T_T" % (i.place + " " + str(i.time)))
        else:
            print("It's a program error when choose the assi_ref of %s T_T" % (i.place + " " + str(i.time)))

### Choose wait_ref:
for i in m:
    if i.wait_ref[34]:
        i.wait_ref["Final"].append(i.wait_ref[34][0])
        find_delete(i.wait_ref[34][0])
    elif i.wait_ref[33]:
        i.wait_ref["Final"].append(i.wait_ref[33][0])
        find_delete(i.wait_ref[33][0])
    if len(i.wait_ref["Final"]) == 1:
        print("Successfully choosed assi_ref of %s :D" % (i.place + " " + str(i.time)))
    elif len(i.wait_ref["Final"]) == 0:
        print("There's no player who can be the assi_ref of %s T_T" % (i.place + " " + str(i.time)))
    else:
        print("It's a program error when choose the assi_ref of %s T_T" % (i.place + " " + str(i.time)))

### Choose video:
for i in m:
    if i.video[34]:
        i.video["Final"].append(i.video[34][0])
        find_delete(i.video[34][0])
    if len(i.video["Final"]) == 1:
        print("Successfully choosed assi_ref of %s :D" % (i.place + " " + str(i.time)))
    elif len(i.video["Final"]) == 0:
        print("There's no player who can be the assi_ref of %s T_T" % (i.place + " " + str(i.time)))
    else:
        print("It's a program error when choose the assi_ref of %s T_T" % (i.place + " " + str(i.time)))

### Print for test
print ("")
for i in m:
    print("========================================")
    print (i.place, i.time)
    print ("주심")
    if i.main_ref["Final"]:
        for j in i.main_ref["Final"]:
            print (j.name, j.team)
    else:
        print ("### Out of Stock!! Use OB!!")
    print ("")
    print ("부심")
    if len(i.assi_ref["Final"]) == 2:
        for j in i.assi_ref["Final"]:
            print (j.name, j.team)
    elif len(i.assi_ref["Final"]) == 1:
        for j in i.assi_ref["Final"]:
            print (j.name, j.team)
            print ("### Out of Stock!! Use OB!!")
    else:
        for j in range(2):
             print ("### Out of Stock!! Use OB!!")
             
    print ("")
    print ("대기심")
    if i.wait_ref["Final"]:
        for j in i.wait_ref["Final"]:
            print (j.name, j.team)
    else:
        print("### Out of Stock!! Use OB!!")
    print ("")
    if ("허리케인A" in i.team) or ("허리케인B" in i.team):
        print ("촬영")
        if i.video["Final"]:
            for j in i.video["Final"]:
                print (j.name, j.team)
        else:
             print ("### Out of Stock!! Use Other 34th guys not in train_dept!!")
        print ("")
print("========================================")
