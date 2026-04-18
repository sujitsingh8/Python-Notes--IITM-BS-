# Find the length of the longest word from the set of words entered

word = input('Enter the word: ')
maxLen = 0
while word != '-1':
    count= 0
    for letter in word:
        count = count +1
    if (count>maxLen):
        maxLen = count
    word = input('Enter a word: ')
print('Length of the longest word is', maxLen)