# your code goes here!
class Anagram():
    def __init__(self, word):
        self.word = word
    def match(self, text):
            return [word for word in text if sorted(word.lower()) == sorted(self.word.lower())]

listen = Anagram("listen")
listen.match(['enlists', 'google', 'inlets', 'banana'])
