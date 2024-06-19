#Reverse Text Reader

# text = input('Write any text: ')
# reverse_text = text[::-1].capitalize()
# print("Reverse version of text ->", reverse_text)

#PRACTICE TIME

text = input('Any text: ')
reverse = text.split()
word1 = reverse[0]
word2 = reverse[1]
temp = word1
word1 = word2
word2 = temp
print(word1.capitalize(), word2.casefold())