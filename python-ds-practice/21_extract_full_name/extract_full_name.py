def extract_full_names(people):
    """Return list of names, extracting from first+last keys in people dicts.

    - people: list of dictionaries, each with 'first' and 'last' keys for
              first and last names

    Returns list of space-separated first and last names.

        >>> names = [
        ...     {'first': 'Ada', 'last': 'Lovelace'},
        ...     {'first': 'Grace', 'last': 'Hopper'},
        ... ]

        >>> extract_full_names(names)
        ['Ada Lovelace', 'Grace Hopper']
    """

    return [f"{person['first']} {person['last']}" for person in people]
    # name_list = []
    # for person in people:
    #     fname = person['first']
    #     lname = person['last']
    #     name = f'{fname} {lname}'
    #     name_list.append(name)
    
    # return name_list


    # name_list = []
    # for name_set in people:
    #     full_name = ""
    #     for (name) in name_set.values():
    #         full_name = f'{full_name} {name}'
    #         full_name = full_name.strip()
    #     name_list.append(full_name)
    
    # return name_list