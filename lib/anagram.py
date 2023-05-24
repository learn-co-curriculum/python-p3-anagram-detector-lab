# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word

    def matching_word(self, words):
        return [word for word in words if sorted(self.word) == sorted(word)]


listen = Anagram('listen')
print(listen.matching_word(['enlist', 'google', 'inlets', 'banana']))
