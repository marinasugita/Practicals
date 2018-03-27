words = input("Text: ").split()
word_count = {}
for word in words:
    word_count[word] = word_count.get(word,0) + 1

for word, value in sorted(word_count.items()):
    print("{} : {}".format(word, value))
