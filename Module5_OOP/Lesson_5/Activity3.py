class Reverse:
    def __init__(self, strings=""):
        """
        Constructor with a default value for the 'strings' attribute.
        """
        self.strings = strings
    
    def set_string(self, word):
        """
        Sets the value of the strings attribute to the input word.
        """
        self.strings = word
    
    def get_reversed(self):
        """
        Returns the reversed string.
        """
        return self.strings[::-1]

if __name__ == "__main__":
    reverse_instance = Reverse()
    user_input = input("Enter a word: ")
    reverse_instance.set_string(user_input)
    print("Reversed string:", reverse_instance.get_reversed())