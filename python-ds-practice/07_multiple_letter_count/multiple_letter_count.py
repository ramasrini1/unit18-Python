def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    my_dict = {}
    for  l in phrase :
        count = phrase.count(l)
        my_dict[l] = count
    
    #print dict
    # for (key, value) in my_dict.items():
    #     print (key, "appears ", value, " times")

    return my_dict

multiple_letter_count('yay')
multiple_letter_count('Yay')