import random

"""
In this program, we open a text file (story.txt), and check for the words it contains
We define a word as that word in the story that we need to replace with user input.
Normally, the words to be replaced are in "<>" brackets.
We take user input for each word ro be replaced and replace the words to be replaced
with the corresponding user input.
The uodated user story is afterwards printed out.
"""

with open("story.txt", "r") as file:
    story = file.read()

words = set()
start_of_word = -1
target_start = "<"
target_end = ">"
for i, char in enumerate(story):
    if char == target_start:
        start_of_word = i

    if char == target_end and start_of_word != -1:
        word = story[start_of_word: i+1]
        words.add(word)
        start_of_word = -1

answers = {}

for word in words:
    answer = input("Enter a word for " + word + ": ")
    answers[word] = answer


for word in words:
    story = story.replace(word, answers[word])

print(story)