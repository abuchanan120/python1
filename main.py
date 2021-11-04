# Andrew Buchanan Python 1
# Programming Assignment 7
# November 4, 2021
# Using re and os (and platform) modules to experiment with regex and os output

import re, os, platform   #the os.uname() appears to only work on UNIX systems,
                #but platform.uname() can be used on Windows, so I imported that to use instead.

# Main code execution
if __name__ == '__main__':
    str1 = str(platform.uname())    #os.uname() doesn't work for Windows
    string = str(os.getcwd())       #os.getcwd() prints the current working directory

    #Regex searching
    result = re.search("Windows", str1)     #Matches because string contains Windows
    print("1.", result)
    result = re.search("Windows|Linux", str1)   #Matches because at least one of Windows/Linux were found
    print("2.", result)
    result = re.findall("AMD64|version|system|Intel", str1)       #Finds all patterns and stores in a list
    print("3.", result)
    result = re.match("uname_result", str1) #Matches because string starts with pattern
    print("4.", result)
    result = re.match("version", str1)      #Won't match because string doesn't start with version
    print("5.", result)
    result = re.search("Users", string)     #Matches because Users is in the string
    print("6.", result)
