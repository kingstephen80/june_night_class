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