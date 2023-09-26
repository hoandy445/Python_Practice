combat = 0
magic = 0
stealth = 0


try:
    print("On a clear day you chance upon a strange animal, its leg trapped in a hunter's clawsnare. Judging from the bleeding it will not survive long.\n", 
        
        "1. Draw your dagger, mercifully ending its life with a single thrust.\n",
        "2. Use herbs from your pack to put it to sleep.\n",
        "3. Do not interfere in the natural evolution of events, but rather take the opportunity to learn more about a strange animal you have never seen before."
    )

    user_input = int(input("> "))
    if user_input < 1 or user_input > 3:
        quit()

    if user_input == 1: 
        combat += 1
    if user_input == 2:
        magic += 1
    if user_input == 3:  
        stealth += 1




    print("One Summer afternoon your father gives you a choice of chores.\n",
        
        "1. Work in the forge with him casting iron for a new plow.\n",
        "2. Gather herbs for your mother who is preparing dinner.\n",
        "3. Go catch fish at the stream using a net and line."
    )

    user_input = int(input("> "))

    if user_input == 1: 
        combat += 1
    if user_input == 2:
        magic += 1
    if user_input == 3:
        stealth += 1


    print("Your cousin has given you a very embarrassing nickname and, even worse, likes to call you it in front of your friends. You asked him to stop, but he finds it very amusing to watch you blush.\n",
        
        "1. Beat up your cousin, then tell him that if he ever calls you that nickname again, you will bloody him worse than this time.\n",
        "2. Gather herbs for your mother who is preparing dinner.\n",
        "3. Make up a story that makes your nickname a badge of honor instead of something humiliating."
    )

    user_input = int(input("> "))

    if user_input == 1: 
        combat += 1
    if user_input == 2:
        magic += 1
    if user_input == 3:
        stealth += 1


    print("There is a lot of heated discussion at the local tavern over a group of people called 'Telepaths'. They have been hired by certain City-State kings. Rumor has it these Telepaths read a person's mind and tell their lord whether a follower is telling the truth or not.\n",
        
        "1. This is a terrible practice. A person's thoughts are his own and no one, not even a king, has the right to make such an invasion into another human's mind.\n",
        "2. Loyal followers to the king have nothing to fear from a Telepath. It is important to have a method of finding assassins and spies before it is too late.\n",
        "3. In these times, it is a necessary evil. Although you do not necessarily like the idea, a Telepath could have certain advantages during a time of war or in finding someone innocent of a crime."
    )

    user_input = int(input("> "))

    if user_input == 1: 
        combat += 1
    if user_input == 2:
        magic += 1
    if user_input == 3:
        stealth += 1


    print("Your mother sends you to the market with a list of goods to buy. After you finish you find that by mistake a shopkeeper has given you too much money back in exchange for one of the items.\n",
        
        "1. Return to the store and give the shopkeeper his hard-earned money, explaining to him the mistake.\n",
        "2.  Decide to put the extra money to good use and purchase items that would help your family.\n",
        "3. Pocket the extra money, knowing that shopkeepers in general tend to overcharge customers anyway."
    )

    user_input = int(input("> "))

    if user_input == 1: 
        combat += 1
    if user_input == 2:
        magic += 1
    if user_input == 3:
        stealth += 1


    print("While in the market place you witness a thief cut a purse from a noble. Even as he does so, the noble notices and calls for the city guards. In his haste to get away, the thief drops the purse near you. Surprisingly no one seems to notice the bag of coins at your feet.\n",
        
        "1. Pick up the bag and signal to the guard, knowing that the only honorable thing to do is return the money to its rightful owner.\n",
        "2. Leave the bag there, knowing that it is better not to get involved.\n",
        "3. Pick up the bag and pocket it, knowing that the extra windfall will help your family in times of trouble."
    )

    user_input = int(input("> "))

    if user_input == 1: 
        combat += 1
    if user_input == 2:
        magic += 1
    if user_input == 3:
        stealth += 1


    print("Your father sends you on a task which you loathe, cleaning the stables. On the way there, pitchfork in hand, you run into your friend from the homestead near your own. He offers to do it for you, in return for a future favor of his choosing.\n",
        
        "1. Decline his offer, knowing that your father expects you to do the work, and it is better not to be in debt.\n",
        "2. Ask him to help you, knowing that two people can do the job faster than one, and agree to help him with one task of his choosing in the future.\n",
        "3. Accept his offer, reasoning that as long as the stables are cleaned, it matters not who does the cleaning."
    )

    user_input = int(input("> "))

    if user_input == 1: 
        combat += 1
    if user_input == 2:
        magic += 1
    if user_input == 3:
        stealth += 1


    print("Your mother asks you to help fix the stove. While you are working, a very hot pipe slips its mooring and falls towards her.\n",
        
        "1. Position yourself between the pipe and your mother.\n",
        "2. Grab the hot pipe and try to push it away.\n",
        "3. Push your mother out of the way."
    )

    user_input = int(input("> "))

    if user_input == 1: 
        combat += 1
    if user_input == 2:
        magic += 1
    if user_input == 3:
        stealth += 1


    print("While in town the baker gives you a sweetroll. Delighted, you take it into an alley to enjoy only to be intercepted by a gang of three other kids your age. The leader demands the sweetroll, or else he and his friends will beat you and take it.\n",
        
        "1. Drop the sweetroll and step on it, then get ready for the fight.\n",
        "2. Give him the sweetroll now without argument, knowing that later this afternoon you will have all your friends with you and can come and take whatever he owes you.\n",
        "3. Act like you're going to give him the sweetroll, but at the last minute throw it in the air, hoping that they'll pay attention to it long enough for you to get a shot in on the leader."
    )

    user_input = int(input("> "))

    if user_input == 1: 
        combat += 1
    if user_input == 2:
        magic += 1
    if user_input == 3:
        stealth += 1



    print("Entering town you find that you are witness to a very well-dressed man running from a crowd. He screams to you for help. The crowd behind him seem very angry.\n",
        
        "1. Rush to the town's aid immediately, despite your lack of knowledge of the circumstances.\n",
        "2. Stand aside and allow the man and the mob to pass, realizing it is probably best not to get involved.\n",
        "3. Rush to the man's aid immediately, despite your lack of knowledge of the circumstances."
    )

    user_input = int(input("> "))

    if user_input == 1: 
        combat += 1
    if user_input == 2:
        magic += 1
    if user_input == 3:
        stealth += 1

except:
    print("Invalid answer.")
    quit()





if combat >= 7:
    print("You are a Warrior. Warriors are the professional men-at-arms, soldiers, mercenaries, and adventurers of the Empire, trained with various weapons and armor styles, conditioned by long marches, and hardened by ambush, skirmish, and battle. ")
if combat == 3 and magic == 3 and stealth == 4:
    print("You are a Warrior. Warriors are the professional men-at-arms, soldiers, mercenaries, and adventurers of the Empire, trained with various weapons and armor styles, conditioned by long marches, and hardened by ambush, skirmish, and battle.")
if magic >= 7:
    print('You are a Mage. Most mages claim to study magic for its intellectual rewards, but they also often profit from its practical applications. Varying widely in temperament and motivation, mages share but one thing in common - an avid love of spellcasting.')
if stealth >= 7:
    print("You are a Thief. Thieves are pickpockets and pilferers. Unlike robbers, who kill and loot, thieves typically choose stealth and subterfuge over violence, and often entertain romantic notions of their charm and cleverness in their acquisitive activities.")
if combat == 6 and magic == 4 and stealth == 0:
    print("You are a Knight. Of noble birth, or distinguished in battle or tourney, knights are civilized warriors, schooled in letters and courtesy, governed by the codes of chivalry. In addition to the arts of war, knights study the lore of healing and enchantment.")
if combat == 6 and magic == 2 and stealth == 2:
    print("You are a Knight.. Of noble birth, or distinguished in battle or tourney, knights are civilized warriors, schooled in letters and courtesy, governed by the codes of chivalry. In addition to the arts of war, knights study the lore of healing and enchantment.")
if combat == 6 and magic == 0 and stealth == 4:
    print("You are a Knight. Of noble birth, or distinguished in battle or tourney, knights are civilized warriors, schooled in letters and courtesy, governed by the codes of chivalry. In addition to the arts of war, knights study the lore of healing and enchantment.")
if combat == 6 and magic == 3 and stealth == 1:
    print("You are a Barbarian. Barbarians are the proud, savage warrior elite of the plains nomads, mountain tribes, and sea reavers. They tend to be brutal and direct, lacking civilized graces, but they glory in heroic feats, and excel in fierce, frenzied single combat.")
if combat == 6 and magic == 1 and stealth == 3:
    print("You are a Crusader. Any heavily armored warrior with spellcasting powers and a good cause may call himself a Crusader. Crusaders do well by doing good. They hunt monsters and villains, making themselves rich by plunder as they rid the world of evil.")
if combat == 5 and magic == 5 and stealth == 0:
    print("You are an Archer. Archers are fighters specializing in long-range combat and rapid movement. Opponents are kept at distance by ranged weapons and swift maneuver, and engaged in melee with sword and shield after the enemy is wounded and weary.")
if combat == 5 and magic == 4 and stealth == 1:
    print("You are an Archer. Archers are fighters specializing in long-range combat and rapid movement. Opponents are kept at distance by ranged weapons and swift maneuver, and engaged in melee with sword and shield after the enemy is wounded and weary.")
if combat == 5 and magic == 3 and stealth == 2:
    print("You are an Archer. Archers are fighters specializing in long-range combat and rapid movement. Opponents are kept at distance by ranged weapons and swift maneuver, and engaged in melee with sword and shield after the enemy is wounded and weary.")
if combat == 5 and magic == 1 and stealth == 4:
    print("You are an Archer. Archers are fighters specializing in long-range combat and rapid movement. Opponents are kept at distance by ranged weapons and swift maneuver, and engaged in melee with sword and shield after the enemy is wounded and weary.")
if combat == 5 and magic == 0 and stealth == 5:
    print("You are an Archer. Archers are fighters specializing in long-range combat and rapid movement. Opponents are kept at distance by ranged weapons and swift maneuver, and engaged in melee with sword and shield after the enemy is wounded and weary.")
if combat == 5 and magic == 2 and stealth == 3:
    print("You are a Scout. Scouts rely on stealth to survey routes and opponents, using ranged weapons and skirmish tactics when forced to fight. By contrast with barbarians, in combat scouts tend to be cautious and methodical, rather than impulsive.")
if combat == 4:
    print("You are a Rogue. Rogues are adventurers and opportunists with a gift for getting in and out of trouble. Relying variously on charm and dash, blades and business sense, they thrive on conflict and misfortune, trusting to their luck and cunning to survive.")
if combat == 3 and magic == 6 and stealth == 1:
    print("You are a Healer. Healers are spellcasters who swear solemn oaths to heal the afflicted and cure the diseased. When threatened, they defend themselves with reason and disabling attacks and magic, relying on deadly force only in extremity.")
if combat == 3 and magic == 5 and stealth == 2:
    print("You are a Witchhunter. Witchhunters are dedicated to rooting out and destroying the perverted practices of dark cults and profane sorcery. They train for martial, magical, and stealthy war against vampires, witches, warlocks, and necromancers.")
if combat == 2 and magic == 5 and stealth == 3:
    print("You are a Witchhunter. Witchhunters are dedicated to rooting out and destroying the perverted practices of dark cults and profane sorcery. They train for martial, magical, and stealthy war against vampires, witches, warlocks, and necromancers.")
if combat == 1 and magic == 5 and stealth == 4:
    print("You are a Witchhunter. Witchhunters are dedicated to rooting out and destroying the perverted practices of dark cults and profane sorcery. They train for martial, magical, and stealthy war against vampires, witches, warlocks, and necromancers.")
if combat == 0 and magic == 5 and stealth == 5:
    print("You are a Witchhunter. Witchhunters are dedicated to rooting out and destroying the perverted practices of dark cults and profane sorcery. They train for martial, magical, and stealthy war against vampires, witches, warlocks, and necromancers.")
if combat == 3 and magic == 4 and stealth == 3:
    print("You are a Spellsword. Spellswords are spellcasting specialists trained to support Imperial troops in skirmish and in battle. Veteran spellswords are prized as mercenaries, and well-suited for careers as adventurers and soldiers-of-fortune.")
if combat == 2 and magic == 4 and stealth == 4:
    print("You are a Spellsword. Spellswords are spellcasting specialists trained to support Imperial troops in skirmish and in battle. Veteran spellswords are prized as mercenaries, and well-suited for careers as adventurers and soldiers-of-fortune.")
if combat == 1 and magic == 4 and stealth == 5:
    print("You are a Spellsword. Spellswords are spellcasting specialists trained to support Imperial troops in skirmish and in battle. Veteran spellswords are prized as mercenaries, and well-suited for careers as adventurers and soldiers-of-fortune.")
if combat == 0 and magic == 4 and stealth == 6:
    print("You are a Spellsword. Spellswords are spellcasting specialists trained to support Imperial troops in skirmish and in battle. Veteran spellswords are prized as mercenaries, and well-suited for careers as adventurers and soldiers-of-fortune.")
if combat == 3 and magic == 2 and stealth == 5:
    print("You are a Pilgrim. Pilgrims are travellers, seekers of truth and enlightenment. They fortify themselves for road and wilderness with arms, armor, and magic, and through wide experience of the world, they become shrewd in commerce and persuasion.")
if combat == 3 and magic == 1 and stealth == 6:
    print("You are an Agent. Agents are operatives skilled in deception and avoidance, but trained in self-defense and the use of deadly force. Self-reliant and independent, agents devote themselves to personal goals, or to various patrons or causes.")
if combat == 2 and magic == 6 and stealth == 2:
    print("You are a Sorcerer. Though spellcasters by vocation, sorcerers rely most on summonings and enchantments. They are greedy for magic scrolls, rings, armor and weapons, and commanding undead and Daedric servants gratifies their egos.")
if combat == 2 and magic == 3 and stealth == 5:
    print("You are a Monk. Monks are students of the ancient martial arts of hand-to-hand combat and unarmored self defense. Monks avoid detection by stealth, mobility, and agility, and are skilled with a variety of ranged and close-combat weapons.")
if combat == 2 and magic == 2 and stealth == 6:
    print("You are an Acrobat. Acrobat is a polite euphemism for agile burglars and second-story men. These thieves avoid detection by stealth, and rely on mobility and cunning to avoid capture.")
if combat == 1 and magic == 6 and stealth == 3:
    print("You are a Battlemage. Battlemages are wizard-warriors, trained in both lethal spellcasting and heavily armored combat. They sacrifice mobility and versatility for the ability to supplement melee and ranged attacks with elemental damage and summoned creatures.")
if combat == 0 and magic == 6 and stealth == 4:
    print("You are a Battlemage. Battlemages are wizard-warriors, trained in both lethal spellcasting and heavily armored combat. They sacrifice mobility and versatility for the ability to supplement melee and ranged attacks with elemental damage and summoned creatures.")
if combat == 1 and magic == 3 and stealth == 6:
    print("You are an Assassin. Assassins are killers who rely on stealth and mobility to approach victims undetected. Execution is with ranged weapons or with short blades for close work. Assassins include ruthless murderers and principled agents of noble causes.")



