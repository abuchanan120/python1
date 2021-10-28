# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


#Converts a given string to pig latin
def pigLatin(str):
    str = str.lower()
    words = str.split()
    for i, word in enumerate(words):
        if word[0] in 'aeiou':                  #if the first letter is a vowel
            words[i] = words[i] + "yay"         #add yay to the end
        else:
            has_vowel = False
            for j, letter in enumerate(word):
                if letter in 'aeiou':            #if first letter is a consonant, look for next vowel
                    words[i] = word[j:] + word[:j] + "ay"       #then move the consonant(s) to the end and add ay
                    has_vowel = True
                    break

            if(has_vowel == False):             #if there are no vowels, just append "ay"
                words[i] = words[i] + "ay"
    newstr = ' '.join(words)
    print("Pig Latin:", newstr)

# Main code execution
if __name__ == '__main__':
    string=input("Enter a string:")
    pigLatin(string)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
