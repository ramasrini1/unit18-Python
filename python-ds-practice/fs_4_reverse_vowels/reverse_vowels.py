def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which re not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """
    lst = list(s)
    vowels = set('aeiou')
    j = len(lst)-1
    i = 0
    while i < j:
      
        if lst[i].lower() not in vowels:
            i = i + 1
        else:
            if lst[j].lower() not in vowels:
                j = j - 1
            else:
                #print("i ", i, "j ", j)
                lst[i], lst[j] = lst[j], lst[i]
                i = i + 1
                j = j - 1
    
    #str1 = ''.join([str(item) for item in lst])
    str1 = ''.join(lst)
    return str1

#print(reverse_vowels("Tomatoes"))  
#print(reverse_vowels("Reverse Vowels In A String"))
#print(reverse_vowels("aeiou"))
#print(reverse_vowels("why try, shy fly?"))
