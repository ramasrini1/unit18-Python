def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    phrase1 = phrase.lower()
    vowels = "aeiou"
    count_dict = {}
    for letter in phrase1:
        if not vowels.find(letter) == -1:
            freq = count_dict.get(letter, 0) + 1
            count_dict[letter] = freq
    
    return count_dict
