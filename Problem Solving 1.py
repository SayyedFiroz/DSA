# Problem solving steps

# 1) State the problem clearly.identify the input and output

# eg alis have deck of card and and bob need to find queried card from that deck of card
# Deck of cards : [13,11,12,5,3,1] ,queried number = 5 ,position = [0,1,2,3,4,5] (To access card in list)

"""def locate_card(cards,query):
    pass"""

# 2)Come up with the some example inputs and outputs.Try to cover all edge cases

cards: [13, 11, 10, 7, 4, 3, 1, 0]
query = 7
output = 3

# we can pass the test case : result = locate_card(card,query) , print(result) , rsesult == output

# every test case will be represented in dictionary

test = {'input': {'cards': [13, 11, 10, 7, 4, 3, 1, 0], 'query': 7}, 'output': 3}

# how to check the test case :

"""locate_card(test['input']['cards'],test['input']['query']) == test['output']"""

# test cases(edge cases)

"""test = []

test.append({ 'input' : { 'cards' :  [9,7,5,2,-9] , 'query' : 4}, 'output':-1})

test.append({ 'input' : { 'cards' :  [] , 'query' : 7}, 'output':-1})

test.append({ 'input' : { 'cards' :  [8,8,8,6,6,6,3,2,2,2,0,0] , 'query' : 3}, 'output':6})

test.append({ 'input' : { 'cards' :  [8,8,6,6,6,3,2,2,2,0,0] , 'query' : 6}, 'output':2})"""


# 3) Come up with correct solution for the problem.State it in plain English.

# eg 1) Create variable position with the value 0
#    2) Check wheather the number in the index poaition in card equals.
#    3) if it does,position is answer and can be returned from the function
#    4) if not,increment the position  by 1.repeat till we reach the end
#    5) if the number is not found ,return -1


# algorithm : list of statement which can be converted into code and executed by a computer in different sets of inputs.

# linear search : searching through a list in linear fashion i.e. element after element

# 4)Implement the solution and test it using example inputs.Fix bugs,if any.

def locate_card(cards, query):
    position = 0

    while position < len(cards):

        if cards[position] == query:
            return position

        position += 1

    return -1


result = locate_card(test['input']['cards'], test['input']['query'])
print(result)

tests = []

tests.append({'input': {'cards': [9, 7, 5, 2, -9], 'query': 4}, 'output': -1})

tests.append({'input': {'cards': [], 'query': 7}, 'output': -1})

tests.append({'input': {'cards': [8, 8, 8, 6, 6, 6, 3, 2, 2, 2, 0, 0], 'query': 3}, 'output': 6})

tests.append({'input': {'cards': [8, 8, 6, 6, 6, 3, 2, 2, 2, 0, 0], 'query': 6}, 'output': 2})

from jovian.pythondsa import evaluate_test_cases

evaluate_test_cases(locate_card, tests)


#Complexity of linear search :Tc = O(n) and Sc = O(1)


# 5) Analyze the algorithm's complexity and identify inefficiencies,if any.