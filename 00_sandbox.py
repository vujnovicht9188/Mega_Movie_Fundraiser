import random 

answer_list = ["ofc", "no you're dumb", "dude just stop talking", "maybe", "good question", "i don't really know", "lol"]

while 1 == 1:  
    question = input("Hurry up, ask me a question ----> ")

    if question != "xxx":
        print(random.choice(answer_list))
    else:
        break
