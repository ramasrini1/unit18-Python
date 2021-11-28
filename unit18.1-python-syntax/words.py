def print_upper_words(words):
    """Print each word on sep line, uppercased.

        >>> print_upper_words(["Programming", "is", "pretty", "fun"])
        PROGRAMMING
        IS
        PRETTY
        FUN
    """

    for word in words:
        print(word.upper())

def print_words_e_upper(words):
    """Print words that start with e uppercase
      >>> print_word_e_upper(["egg", "yellow", "elephant"])
    """
    for word in words:
        if (word.startswith("e") or word.startswith("E")):
          print(word.upper())

def print_upper_words2(words, must_start_with):
  """Print words that start with words from the list must_start_with
      >>> print_upper_words2(["hello", "hey", "goodbye", "yo", "yes"],
                   must_start_with=["h", "y"])
  """
  for word in words:
    #print(f"word is {word}")
    for startWord in must_start_with:
      if word.startswith(startWord):
        print (f"{word.upper()}")

print_upper_words(["How", "are", "you!"])
print_words_e_upper(["egg", "yellow", "elephant"])
print_upper_words2(["hello", "hey", "goodbye", "yo", "yes"],
                   must_start_with=["h", "y"])