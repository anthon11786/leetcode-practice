"""
Write a function count_construct(target, wordbank) that accepts a target string and 
array of strings. 

The Function should return the number of ways that 'target' can be constructed by concatenating
the elements of the word_bank array.

You may reuse elements of word_bank as many times as needed. 
"""


def count_construct(target: str, word_bank: list[str], memo: dict = {}): 
    if target == '':
        return 1 
    if target in memo: 
        return memo[target] 
    
    total = 0 
    for word in word_bank:
        if target.startswith(word):
            remainder = target.removeprefix(word)
            total += count_construct(remainder, word_bank, memo) 
    
    memo[target] = total
    return total 


print(count_construct("abcdef", ["ab", "abc", "cd", "def", "abcd"])) # 1
print(count_construct("purple", ["purp", "p", "le", "purpl", "le"])) # 2
print(count_construct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"])) # 0 
print(count_construct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eeeee", "eeeeee"])) # 0 

"""
Time/Space complexity: 
m = target.length 
n = len(word_bank)


Brute force: 
Time: O(n^m * m )
Space: O(m^2) 

Memoized: 
Time: O(n * m^2)
Space: O(m^2) 

"""