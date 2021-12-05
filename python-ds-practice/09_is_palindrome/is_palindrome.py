def is_palindrome(phrase):
    """Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).

        >>> is_palindrome('tacocat')
        True

        >>> is_palindrome('noon')
        True

        >>> is_palindrome('robert')
        False

    Should ignore capitalization/spaces when deciding:

        >>> is_palindrome('taco cat')
        True

        >>> is_palindrome('Noon')
        True
    """
    word = phrase.lower().strip()
    word = word.replace(' ', '')
    return word == word[::-1]
    
    # lst = []
    
    # for letter in word:
    #     if letter != " ":
    #        lst.append(letter)
          
    # #print(lst)
    # length = len(lst)
    # count = 0
    # index = 0
    
    # if length % 2 == 0:
    #     count = length/2
    # else:
    #     count = (length -1 )/2

    # while index < count:
    #     if lst[index] != lst[length -1 - index]:
    #         return False
    #     index = index + 1
    # return True


print(is_palindrome('No on'))
print(is_palindrome('tacocat'))
print(is_palindrome('robert'))
print(is_palindrome('taco cat'))
print(is_palindrome('Noon'))
