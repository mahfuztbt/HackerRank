# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

def find_substrings(input_string):
    vowel = "[aeiou]"
    consonant = "[qwrtypsdfghjklzxcbnm]"
    return re.findall(r"{consonant}({vowel}{{2,}})(?={consonant})".format(vowel=vowel,consonant=consonant),input_string,re.IGNORECASE)

def main():
    input_string = input()
    substrings = find_substrings(input_string)
    if substrings:
        print(*substrings, sep="\n")
    else:
        print(-1)
        
if __name__ == "__main__":
    main()