def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
    #return phrase.title()
    
    # lst = phrase.split(' ')
    # s = " "
    # new_list = []
    # for word in lst:
    #     word = word.capitalize()
    #     new_list.append(word)
    # s = s.join(new_list)
   
    # return s
    
    lst = [word.capitalize() for word in phrase.split(' ')]
    return ' '.join(lst)

    #return ' '.join([s.capitalize() for s in phrase.split(' ')])