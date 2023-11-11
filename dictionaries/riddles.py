Q1 = "What has to be broken before you can use it?"
Q2 = "I'm tall when I'm young, and I'm short when I'm old. What am I?"
Q3 = "What month of the year has 28 days?"

riddles = {}
riddles[Q1] = "egg"
riddles[Q2] = "candle"
riddles[Q3] = "all of them"

import random
rlist = list(riddles.keys())
random.shuffle(rlist)

for i in rlist:
    print(i)
    useranswer = input("> ")
    if useranswer == riddles[i]:
        print("correct answer!")
    else:
        print("wrong answer!")
