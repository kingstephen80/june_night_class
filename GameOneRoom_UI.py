#imports
import random

#global variables
ISMONSTER = False
MONSTERNAME = ''
DOORCHOICE = ''

#classes
class Room():
    def __init__(self):
        global MONSTERNAME
        global ISMONSTER
        findmonster()
        self.n_door = dooropen()
        self.s_door = dooropen()
        self.e_door = dooropen()
        self.w_door = dooropen()
        if self.n_door is False and self.s_door is False and self.e_door is False and self.w_door is False:
            self.n_door = True
            self.doorstatement()
        else:
            self.doorstatement()
        if ISMONSTER is True:
            MONSTERNAME = namemonster()

    # list with the four directions
    direction = ['North', 'South', 'East', 'West']

    #list of different room descriptions
    description = ['The %s wall is covered in moss.',
                   'The %s wall is covered in slime.',
                   'The %s wall is made of brick.',
                   'The %s wall is solid stone.',
                   'The %s wall has crumbled.',
                   'The %s wall is normal looking.',
                   'The %s wall, its just a forrest.',
                   'The %s wall looks like it is dense fog.',
                   'The %s wall is made of old hard cheese.',
                   'The %s wall is a decaying dragon, and no you cant loot him.'
                   ]
    #list of if there is a door open or not to go with the descriptions
    dooropen = ['No', 'Yes']

    #load the 4 directions
    def north(self):
        rnd = rnd09()
        self.desc = self.description[rnd] % self.direction[0]
        return self.desc

    def south(self):
        rnd = rnd09()
        self.desc = self.description[rnd] % self.direction[1]
        return self.desc

    def east(self):
        rnd = rnd09()
        self.desc = self.description[rnd] % self.direction[2]
        return self.desc

    def west(self):
        rnd = rnd09()
        self.desc = self.description[rnd] % self.direction[3]
        return self.desc

    #generate the door open messages
    def doorstatement(self):
        global DOORCHOICE
        if self.n_door is True and self.s_door is True and self.e_door is True and self.w_door is True:
            ds = "There are open doors to the North, South, East and West."
            DOORCHOICE = "You can go North, South, East or West: "
        elif self.n_door is False and self.s_door is True and self.e_door is True and self.w_door is True:
            ds = "There are open doors to the South, East and West."
            DOORCHOICE = "You can go South, East or West: "
        elif self.n_door is False and self.s_door is False and self.e_door is True and self.w_door is True:
            ds = "There are open doors to the East and West."
            DOORCHOICE = "You can go East or West: "
        elif self.n_door is False and self.s_door is False and self.e_door is False and self.w_door is True:
            ds = "There is an open door to the West."
            DOORCHOICE = "You can go West: "
        elif self.n_door is True and self.s_door is False and self.e_door is False and self.w_door is True:
            ds = "There are open doors to the North and West."
            DOORCHOICE = "You can go North or West: "
        elif self.n_door is True and self.s_door is True and self.e_door is False and self.w_door is True:
            ds = "There are open doors to the North, South and West."
            DOORCHOICE = "You can go North, South or West: "
        elif self.n_door is True and self.s_door is True and self.e_door is True and self.w_door is False:
            ds = "There are open doors to the North, South, and East."
            DOORCHOICE = "You can go North, South or East: "
        elif self.n_door is True and self.s_door is True and self.e_door is False and self.w_door is False:
            ds = "There are open doors to the North and South."
            DOORCHOICE = "You can go North or South: "
        elif self.n_door is False and self.s_door is False and self.e_door is True and self.w_door is False:
            ds = "There is an open door to the East."
            DOORCHOICE = "You can go East: "
        elif self.n_door is False and self.s_door is True and self.e_door is False and self.w_door is False:
            ds = "There is an open door to the South."
            DOORCHOICE = "You can go South: "
        elif self.n_door is True and self.s_door is False and self.e_door is False and self.w_door is False:
            ds = "There is an open door to the North."
            DOORCHOICE = "You can go North: "
        elif self.n_door is True and self.s_door is True and self.e_door is False and self.w_door is True:
            ds = "There are open doors to the North, South and West."
            DOORCHOICE = "You can go North, South or West: "
        elif self.n_door is False and self.s_door is True and self.e_door is False and self.w_door is True:
            ds = "There are open doors to the South and West."
            DOORCHOICE = "You can go South or West: "
        elif self.n_door is True and self.s_door is False and self.e_door is True and self.w_door is True:
            ds = "There are open doors to the North, East and West."
            DOORCHOICE = "You can go North, East or West: "
        elif self.n_door is False and self.s_door is True and self.e_door is True and self.w_door is False:
            ds = "There are open doors to the South and East."
            DOORCHOICE = "You can go South or East: "
        elif self.n_door is True and self.s_door is False and self.e_door is True and self.w_door is False:
            ds = "There are open doors to the North and West."
            DOORCHOICE = "You can go North or West: "
        return ds

#functions
#function to see if the door is open or not for each wall
def dooropen():
    if random.randint(1, 101) < 50:
        do = True
    else:
        do = False
    return do

#generate some random numbers between 0 and 9
def rnd09():
    rnd = random.randint(0, 9)
    return rnd

#moving through a door statements
def doormove(dir):
    if dir == "north" or dir == "n":
        direction = "North"
    elif dir == "south" or dir == "s":
        direction = "South"
    elif dir == "east" or dir == "e":
        direction = "East"
    elif dir == "west" or dir == "w":
        direction = "West"
    path = "   You walk through the door in the %s wall.\n\n" % direction
    return path

#is there a monster in this room?
def findmonster():
    global ISMONSTER
    if random.randint(1,101) < 50:
        ISMONSTER = True
    else:
        ISMONSTER = False
    return ISMONSTER

#name the monster
def namemonster():
    global MONSTERNAME
    names = [
        'Magneto',
        'Doctor Doom',
        'Venom',
        'Juggernaut',
        'Thanos'
    ]
    rnd = random.randint(0, 4)
    name = names[rnd]
    return name

#user interface
def userinterface():
    global MONSTERNAME
    global ISMONSTER
    global DOORCHOICE
    playmore = True
    while playmore == True:
        new = Room()

        print "You have entered a new room.\n  %s\n  %s\n  %s\n  %s\n" % (new.north(), new.south(), new.east(), new.west())

        if ISMONSTER is True:
            print "Look out! You see %s in the room!" % MONSTERNAME
          
          #(stephen: looking to add random monster attack upon entry.)

 


# Fight thought process def fight(p, m):
	def fight(monster, hero):
        m = monster
        h = hero
        while hero.hp and m.hp > 0:
            choice1 = raw_input("You now have a choice, run! Or fight %s! Enter 1 if you would like to run. \nEnter 2 if you want to fight\n>   " % MONSTERNAME)
    		p_attack = p.damage + random.randint(-2, 3)
            p_run  = p.damgage + random.randint(-2, 2)
            m_attack = m.damage + random.randint(2, 3)
            if choice1 == "1"
                p_run = p.damage + random.randint(-2, 2)
                #exit room to previous location.
            elif choice1 == "2"
                p_attack = p.damage + random.randint(-2, 3)
                m_attack = m.damage + random.randint(3, 9)




def UserName():
    global UserName = raw_input("Pick a name for your Hero:   ")



class Things():
    def __init__(self, name):
        self.hp = 90 + random.randint(5, 50)
        self.name = name
        self.ap = 5 + random.randint(3, 10)
        self.w  = 0 
        self.a  = 0 


def fight(p, m):
    while m.hp or p.hp > 0:
        choice1 = raw_input("Enter 1 to attack the monster.\n Enter 2 to run away. \n> ")
        p_attack = p.damage + random.randint(-2, 3)
        m_attack = m.damage + random.randint(-2, 3)
        if choice1 == "1":
            p_attack = p.damage + random.randint(-2, 3)
            m_attack = m.damage + random.randint(3, 9)
        elif choice1 == "2":
                 # code to exit room
        choice2 = raw_input("You have survived the first fight, Enter 1 to attack %s again.\n Enter 2 to play dead\n" % MONSTERNAME)
        p_attack = p.damage + random.randint(-2, 3)
        m_attack = m.damage + random.randint(-2, 3)
        if choice2 == "1":
            p_attack = p.damage + random.randint(-2, 3)
            m_attack = m.damage + random.randint(3, 9)
        elif choice2 == "2":
        choice3 = raw_input("The fight continues to the death... ")
            p_attack = p.damage + random.randint(-2, 3)
        m_attack = m.damage + random.randint(-2, 3)
        if choice3 == "1":
            p_attack = p.damage + random.randint(-2, 3)
            m_attack = m.damage + random.randint(3, 9)
        elif choice3 == "2":

        print ''




        #elif hero.hp == 0:
		#	print "You have lost this time! Thanks for playing."

	# if hero.hp and m.hp > 0:
	# 		!" % MONSTERNAME
	# 		random_m.attack1 = hero.damage + random.randint(-2, 3)

	# if hero.hp and m.hp > 0:

 #            print "%s looks at you and says,So you have survived the fight so far lets see how you do with this
 #        choice2 == raw_input("You are still kicking, great! ")




		#return rnd = random.randint(0,1)

        #     print "Fight sequence here!"
        # else:
        #     print "You do not see any monsters!"
        #fight() #fight class here

        #Continue playing options:
        choice = raw_input("Do you want to continue?\nPlease Enter Yes or No: ")
        choice = str.lower(choice)
        if choice == "yes" or choice == "y":
            print new.doorstatement()
            print DOORCHOICE
            dchoice = str.lower(raw_input("Which way do you want to go?"))
            print doormove(dchoice)
            playmore = True
        elif choice == "no" or choice == "n":
            print "Thank you for playing!"
            playmore = False


userinterface()




Things ()
