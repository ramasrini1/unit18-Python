# def compact(lst):
#     """Return a copy of lst with non-true elements removed.

#         >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
#         [1, 2, 'All done']
#     """
#     count = len(lst)
#     index = 0
#     print(count)
#     lst1 = []
#     for item in lst:
#         if item:
#             lst1.append(item)
#     return lst1

def compact(lst):
#     """Return a copy of lst with non-true elements removed.

#         >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
#         [1, 2, 'All done']
#     """
    return [val for val in lst if val ]
   

print(compact([0, 1, 2, '', [], False, (), None, 'All done']))