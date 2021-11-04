# Andrew Buchanan Python 1
# Programming Assignment 7
# November 4, 2021
# Using re and os modules to experiment with regex and os output

import re, os, platform   #the os.uname() appears to only work on UNIX systems,
                #but platform.uname() can be used on Windows

# Main code execution
if __name__ == '__main__':
    str1 = str(platform.uname())
    string = str(os.getcwd())
    #Regex searching
    result = re.search("Windows", str1)     #Matches because string contains Windows
    print(result)
    result = re.search("AMD64", str1)       #Matches because string contains AMD64
    print(result)
    result = re.match("uname_result", str1) #Matches because string starts with pattern
    print(result)
    result = re.match("version", str1)      #Won't match because string doesn't start with version
    print(result)
    result = re.search("Users", string)     #Matches because Users is in the string
    print(result)
