# get sentence from user

originalSentence = input("Please enter a sentence! ").strip().lower()

# split sentence into words

words = originalSentence.split()

# loop through words and convert into pig latin

new_words = []

for word in words:
    if word[0] in 'aeiou':
        new_word = word + 'yay'
        new_words.append(new_word)
    else:
        if word[1] not in 'aeiou':
            new_word = word[2:] + word[0:2] + 'ay'
            new_words.append(new_word)
        else:
            new_word = word[1:] + word[0] + 'ay'
            new_words.append(new_word)
        
print('Modified words: ')
print(new_words)

#if it starts with a vowel add yay

#otherwise move consonant to end and add ay

# stick words back together

newSentence = " ".join(new_words)

# output the final string

print(newSentence)
