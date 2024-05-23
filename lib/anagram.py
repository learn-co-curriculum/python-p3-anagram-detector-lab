# your code goes here!
class Anagram:
    def __init__(self,word):
        self.sorted_letters = sorted([letter for letter in word])
    
    def match(self, given_list):
        matching = []
        for i in given_list:
            if sorted([letter for letter in i]) == self.sorted_letters:
                matching.append(i)

        return matching