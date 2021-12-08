"""Word Finder: finds random words from a dictionary."""
import random


class WordFinder:
    """Reads from a txt file and returns a random word  
    >>> wf = WordFinder("simple.txt")
    3 words read
    
    >>> wf.random() in ["cat", "dog", "porcupine"]
    True
    """
    def __init__(self, filename):
        """Returns number of words in a file."""
        file = open(filename)
        self.words = self.parse(file)
        file.close()
        print(f"{len(self.words)} words read")
       
    def parse(self, file ):
        return [w.strip() for w in file]
    
    def random(self):
        """Return random word."""
        return random.choice(self.words)

class SpecialRandomWord(WordFinder):
        """Specialized WordFinder that excludes blank lines/comments.
        >>> swf = SpecialRandomWord("complex.txt")
        3 words read

        >>> swf.random() in ["pear", "carrot", "kale"]
        True

        >>> swf.random() in ["pear", "carrot", "kale"]
        True

        >>> swf.random() in ["pear", "carrot", "kale"]
        True
        """
        def parse(self, file ):
            return [w.strip() for w in file 
                    if not len(w.strip())==0 and not w.startswith("#")]
            # lst = []
            # for w in file:
            #     if not len(w.strip()) == 0 and not w.startswith("#"):
            #         w = w.strip()
            #         lst.append(w)
            # return lst
    
# wf = WordFinder("simple.txt")
# print(wf.random())
# srw = SpecialRandomWord("complex.txt")
# print(srw.random())