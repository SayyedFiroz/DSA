# Complexity :Complexity of an algorithm is a measure of the amount of time and/or space required by an algorithm for an input of a given size e.g. N.
# Unless otherwise stated, the term complexity always refers to the worst-case complexity (i.e. the highest possible time/space taken by the program/algorithm to process an input).

# Types of Complexity : 1)Time Complexity and Space Complexity

# Time Complexity:number of operations we perform in each iteration and the time taken to execute a statement on an n input.
# Time complexity is sometimes also called the running time of the algorithm.

# Space complexity:(for linear search) The space complexity is some constant c' (independent of N).
# since we just need a single variable position to iterate through the array, and it occupies a constant space in the computer's memory (RAM).


# Binary Search


tests = []

tests.append({'input': {'cards': [13, 11, 10, 7, 4, 3, 1, 0], 'query': 7},'output': 3})
tests.append({'input': {'cards': [4, 2, 1, -1], 'query': 4}, 'output': 0})
tests.append({'input': {'cards': [3, -1, -9, -127], 'query': -127}, 'output': 3})
tests.append({'input': {'cards': [6], 'query': 6}, 'output': 0})
tests.append({'input': {'cards': [9, 7, 5, 2, -9], 'query': 6}, 'output': -1})
tests.append({'input': {'cards': [8, 8, 6, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0], 'query': 6}, 'output': 2})


"""def locate_card(cards, query):
    lo = 0
    hi= len(cards) - 1

    while lo <=hi:
        mid = lo + hi // 2
        mid_number = cards[mid]
        if mid_number == query:
            return mid
        elif mid_number < query:
            hi = mid - 1
        elif mid_number > query:
            lo = mid + 1

    return -1"""


# test case 8 failed  the below one

cards = [8, 8, 6, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0]
query = 6

# to overcome the test case problem i solved by own

"""def locate_card(cards, query):
    lo = 0
    hi= len(cards) - 1

    while lo <=hi:
        mid = lo + hi // 2
        mid_number = cards[mid]
        if mid_number == query:
            for i in cards:
                if mid_number == query:
                    index = cards.index(query)
                    return index
            return mid
        elif mid_number < query:
            hi = mid - 1
        elif mid_number > query:
            lo = mid + 1

    return -1"""

# by intructor

# develop test function for the failed test and passed in main program

def testlocation(cards,query,mid):
    if cards[mid] == query:
        if mid-1 >= 0 and cards[mid-1]==query:
            return 'left'
        else:
            return 'found'
    elif cards[mid] > query:
        return 'right'
    else:
        return 'left'





def locate_card(cards,query):
    lo=0
    hi=len(cards)-1
    while lo<=hi:
        mid = (lo+hi)//2
        result = testlocation(cards,query,mid)
        if result == 'found':
            return mid
        elif result == 'left':
            hi = mid-1
        elif result == 'right':
            lo = mid+1
    return -1



result = (locate_card(cards,query))
print(result)





from jovian.pythondsa import evaluate_test_cases

evaluate_test_cases(locate_card,tests)

