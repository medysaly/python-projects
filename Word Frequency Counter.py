split_words = {}
user_sentence = input('Please enter a sentece: ').lower()
words = user_sentence.split()
for i in words:
    if i in split_words:
        split_words[i] += 1
    else:
        split_words[i] = 1

print(split_words)