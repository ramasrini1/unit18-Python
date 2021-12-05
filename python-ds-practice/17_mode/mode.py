def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    count_dict = {}
    for num in nums:
        freq = count_dict.get(num, 0) + 1
        count_dict[num] = freq
    
    frequencies = count_dict.values()
    max_value = max(frequencies)
    
    for( item, freq ) in count_dict.items():
        if freq == max_value:
            return item
    
print(mode([1, 2, 1]))
print(mode([2, 2, 3, 3, 2]))