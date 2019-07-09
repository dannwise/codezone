def palindrome(string):
    
    # Variable to store edition count
    editions = 0
    
    # Making shure capitalized letters won't mess results up
    string = string.lower()

    # Spliting string in half or integer part of a odd string and comparing equidistant terms
    for i in range(len(string)//2):
        if not(string[i] == string[-(i+1)]):
            editions += 1
        continue
            
    return editions
