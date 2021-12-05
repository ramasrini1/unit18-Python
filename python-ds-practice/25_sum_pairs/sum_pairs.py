# def sum_pairs(nums, goal):
#     """Return tuple of first pair of nums that sum to goal.

#     For example:

#         >>> sum_pairs([1, 2, 2, 10], 4)
#         (2, 2)

#     (4, 2) sum to 6, and come before (5, 1):

#         >>> sum_pairs([4, 2, 10, 5, 1], 6) # (4, 2)
#         (4, 2)

#     (4, 3) sum to 7, and finish before (5, 2):

#         >>> sum_pairs([5, 1, 4, 8, 3, 2], 7)
#         (4, 3)

#     No pairs sum to 100, so return empty tuple:

#         >>> sum_pairs([11, 20, 4, 2, 1, 5], 100)
#         ()
#     """
#     index1 = 0
#     index2 = 0
#     count = len(nums)
#     sum = 0
#     while index1 < count:
#         item1 = nums[index1]
#         while index2 < count:
#             if not index2 == index1:
#                 sum = nums[index1] + nums[index2]
#                 print("sum is ", sum)
#                 if sum == goal:
#                     t1 = (nums[index1], nums[index2])
#                     return t1
#             index2 += 1
#             print(f"index2 is {index2} and index1 is {index1}")
#         index1 += 1
    
#     return ()


def sum_pairs(nums, goal):
#     """Return tuple of first pair of nums that sum to goal.

#     For example:

#         >>> sum_pairs([1, 2, 2, 10], 4)
#         (2, 2)

#     (4, 2) sum to 6, and come before (5, 1):

#         >>> sum_pairs([4, 2, 10, 5, 1], 6) # (4, 2)
#         (4, 2)

#     (4, 3) sum to 7, and finish before (5, 2):

#         >>> sum_pairs([5, 1, 4, 8, 3, 2], 7)
#         (4, 3)

#     No pairs sum to 100, so return empty tuple:

#         >>> sum_pairs([11, 20, 4, 2, 1, 5], 100)
#         ()
#     """

    index1 = 0
    index2 = 0
    count = len(nums)
    sum = 0
    while index1 < count:
        index2 = 0
        while index2 < count:
            if not index2 == index1:
                sum = nums[index1] + nums[index2]
                if sum == goal:
                    return (nums[index1], nums[index2])
            #print(f"index1 is {index1} and index2 is {index2}")
            index2 += 1
        index1 += 1
    
    return ()

#print(sum_pairs([1, 2, 2, 10], 4))
# already_visited = set()

#     for i in nums:
#         difference = goal - i

#         if difference in already_visited:
#             return (difference, i)

#         already_visited.add(i)

#     return ()
