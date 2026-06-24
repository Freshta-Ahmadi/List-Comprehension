
sentence = ("should we create a method to pick a random card? No need. Python already has a function"
            " to get a random item from a sequence: random.choice.").split()
result = {word: len(word) for word in sentence}
print(result)
