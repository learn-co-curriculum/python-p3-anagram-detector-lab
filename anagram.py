# your code goes here!
class Anagram:

    
    def __init__(self, word):
        self.word = word.lower()

    def match(self, checkers):
        return [check for check in checkers if self.an_anagram(check)]
    
    def an_anagram(self,check):
        check_lower = check.lower()


        if check.lower() == self.word or len(check_lower) != len(self.word):
            return []
        
        return sorted(check_lower) == sorted(self.word)
    

# Creating an instance of Anagram class
listen = Anagram("Listen")
post = Anagram("Post")

#Find anagrams in alist
result = listen.match(['enlist','google','inlets', 'banana']) # Calling for an anagram
result1 =post.match(['grando','tops','pots', 'stop'])# Calling for an anagram

#Printing an anagram result
print(result) # Output ['enlist', 'inlets']
print(result1) # Output ['tops', 'pots', 'stop']