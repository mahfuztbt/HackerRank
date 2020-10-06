def minion_game(string):
    # your code goes here
    S=len(string)
    consonant,vowel=0,0

    for i in range(S):
        if string[i] in 'AIEOU':
            vowel=vowel+(S-i)
        else:
            consonant=consonant+(S-i)

    if consonant>vowel:
        print("Stuart {}".format(consonant))
    elif consonant == vowel:
        print("Draw")
    else:
        print("Kevin {}".format(vowel))

if __name__ == '__main__':
    s = input()
    minion_game(s)