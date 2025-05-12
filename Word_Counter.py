sentence = input('Please enter a phrase : ')

words = sentence.split()
word_count = len(words)
char_count = len(sentence.replace(" ", ""))


print(f'Words: {word_count}')
print(f'Characters: {char_count}')