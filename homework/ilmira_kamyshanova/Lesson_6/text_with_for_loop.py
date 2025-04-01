text = ('Etiam tincidunt neque erat, quis molestie enim imperdiet vel. '
        'Integer urna nisl, facilisis vitae semper at, dignissim vitae libero')
new_words = []

for word in text.split(' '):
    if ',' in word or '.' in word:
        new_words.append(word[:-1] + 'ing' + word[-1])
    else:
        new_words.append(word + 'ing')

print(' '.join(new_words))
