
# text1 = []
with open("text1-1.txt", "r") as t:
    text = t.readlines()
    text1 = [int(line) for line in text]
    # print(text1)

with open("text2-1.txt", "r") as t:
    text = t.readlines()
    text2 = [int(line) for line in text]
    # print(text2)


result = [numbers for numbers in text1 if numbers in text2]
print(result)
