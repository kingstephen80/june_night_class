import random

class Player():
    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.mana = 100
        self.damage = 3


class Monster(Player):
    def __init__(self, name, hp, mana):
        Player.__init__(self, name)
        self.hp = hp
        self.mana = mana



def fight(p, m):
    while (m.hp >= 0 or p.hp >= 0):

        choice1 = raw_input("Enter 1 to attack the monster.\n Enter 2 to run away. \n> ")
      
        if choice1 == "1":
            m.hp -=(p.damage + p.a + random.randint(-2, 3))
            p.hp -=(m.damage - p.w + random.randint(-2, 3))
            print "your hp is %s" % p.hp
            print "The monster has %s " % m.hp
        elif choice1 == "2":
            print ("Your health is now at %s" % str(p.hp))
        if m.hp <= 0:
            print "You have killed the monster"
            print ("The monster has left some loot, you pick up the %s" % loot)

            break
        elif p.hp <= 0:
            print "You have died. "
            break


    def loot(p):
        ran= random.randint(0, 100)
        if ran < 50:
            p.a += 1
        else:
            p.w += 1
        



        # if m.hp <= 0:
        #     print "The mo"

                   # code to exit room
        # choice2 = raw_input("You have survived the first fight, Enter 1 to attack %s again.\n Enter 2 to play dead\n" % MONSTERNAME)
        #     p_attack = p.damage + random.randint(-2, 3)
        #     m_attack = m.damage + random.randint(-2, 3)
        #     if choice2 == "1":
        #         p_attack = p.damage + random.randint(-2, 3)
        #         m_attack = m.damage + random.randint(3, 9)
        #     elif choice2 == "2":

        # choice3 = raw_input("The fight continues to the death... ")
        #     p_attack = p.damage + random.randint(-2, 3)
        #     m_attack = m.damage + random.randint(-2, 3)
        #     if choice3 == "1":
        #         p_attack = p.damage + random.randint(-2, 3)
        #         m_attack = m.damage + random.randint(3, 9)
        #     elif choice3 == "2":



player = Player("Stephen")
trogdor = Monster("Trogdor the burninator", 75, 20)

fight(player, trogdor)