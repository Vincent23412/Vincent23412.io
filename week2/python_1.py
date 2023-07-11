# We have example messages from 6 persons in JSON format. There are at least 3 persons
# who are older than 17. Using a loop to find out those who are most probably older than 17
# years old based on example messages. Print their names in the console
import re

def find_and_print(messages):
    # write down your judgment rules in comments
    # your code here, based on your own rules

    old = []
    for name,describe in messages.items() :
        numbers = re.findall(r'\d+', describe)
        if numbers :
            if int(numbers[0]) > 17 :
                old.append(name)
        if 'vote' in describe or 'legal' in describe :
            old.append(name)
        
    print(old)
    return name
            


find_and_print({
    "Bob":"My name is Bob. I'm 18 years old.",
    "Mary":"Hello, glad to meet you.",
    "Copper":"I'm a college student. Nice to meet you.",
    "Leslie":"I am of legal age in Taiwan.",
    "Vivian":"I will vote for Donald Trump next week",
    "Jenny":"Good morning."
})