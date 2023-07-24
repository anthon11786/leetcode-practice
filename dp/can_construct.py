"""
write a funciton that takes in target string and array of strings 

the function should return a boolean indicating whether or not the 'target' can be 
constructed by concatenating elements of the wordBank array.

You may reuse elements of the wordBank array as many times as possible 
"""

# Base CASE 
def can_construct(target: str, word_bank: list[str]):
    """
    """
    # Base case - if empty string, you can construct it always by taking 0 word from wordbank 
    if target == "":
        return True 
    
    for word in word_bank: 
        if target.startswith(word): 
            remainder = target.removeprefix(word) # this constributes to time complexity, slices target string. And SPACE b/c create new string of m
            if (can_construct(remainder, word_bank)): 
                return True # early return true 

    return False 



    

print(can_construct("abcdef", ["ab", "abc", "cd", "def", "abcd"])) # True 
print(can_construct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"])) # False 
print(can_construct("eeeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eeeee", "eeeeee"])) 
# false -> simulate worse case, no early return because have to traverse whole tree 



"""
Time Complexity - Brute force
m = Length of target string 
n = length of word_bank array 

Time: O(n^m * m) - the second m multiplied is from the .removeprefix function which has to iterate through string arrays 
usually rule of thumb with recursion is the time complexity is the 
'branching' factor to the 'height' power, in this case, n is branching and m is height of recursive 
tree. 

Space: O(m^2)
Height of the tree - which is m (target.length) 
multiplied by 
the new string created in during the removeprefix() function return 

Time Complexity - Memoizied
m = Length of target string 
n = length of word_bank array 

Time: O(n*m  * m ) -> O(n * m^2)
Space: O(m^2)
"""


# Memoized version: 
def can_construct_memo(target: str, word_bank: list[str], memo: dict = {}):
    """
    """
    # Base case - if empty string, you can construct it always by taking 0 word from wordbank 
    if target == "":
        return True 
    if target in memo: 
        return memo[target]
    
    for word in word_bank: 
        if target.startswith(word): 
            remainder = target.removeprefix(word) # this constributes to time complexity, slices target string. And SPACE b/c create new string of m
            if (can_construct_memo(remainder, word_bank, memo)): 
                memo[target] = True # early return true 
                return memo[target]

    memo[target] = False 
    return memo[target]


print(can_construct_memo("abcdef", ["ab", "abc", "cd", "def", "abcd"])) # True 
print(can_construct_memo("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"])) # False 
print(can_construct_memo("eeeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eeeee", "eeeeee"])) 