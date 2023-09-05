"""QUESTION:Alice has some cards with numbers written on them. 
            She arranges the cards in decreasing order, and lays them out face down in a sequence on a table. 
            She challenges Bob to pick out the card containing a given number by turning over as few cards as possible. 
            Write a function to help Bob locate the card."""

def binarySearch(lo,hi,condition):
    while lo<=hi: #there should be atleast one element in cards
        mid=(lo+hi)//2
        result=condition(mid)
        if result=='found':
            return mid
        elif result=='left':
            hi=mid-1
        elif result=='right':
            lo=mid+1
    return -1    #if query is not there in cards

def locateCards(cards,query):
    def conditon(mid):
        if cards[mid]==query:
            if mid>=0 and cards[mid-1]==query: #if there is a repetition of queries take the first one 
                return 'left'
            else:
                return 'found'
        elif cards[mid]<query:
            return 'left'
        else:
            return 'right'
    return binarySearch(0,len(cards)-1,conditon)



testCases=[] #list for storing all test cases

#query occurs in middle
testCases.append({
    'input':{'cards':[14,9,7,6,3,1],
             'query':7
             },
    'output':2
})

#query is the first element
testCases.append({
    'input':{'cards':[14,9,7,6,3,1],
             'query':14
             },
    'output':0
})

#query is the last element
testCases.append({
    'input':{'cards':[14,9,7,6,3,1],
             'query':1
             },
    'output':5
})

#cards contains just one element,query
testCases.append({
    'input':{
        'cards':[6],
        'query':6
    },
    'output':-1
})

#cards does contain query
testCases.append({
    'input':{'cards':[14,9,7,6,3,1],
             'query':5
             },
    'output':-1
})

# cards is empty
testCases.append({
    'input': {
        'cards': [],
        'query': 7
    },
    'output': -1
})

# numbers can repeat in cards
testCases.append({
    'input': {
        'cards': [8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
        'query': 3
    },
    'output': 7
})

# query occurs multiple times
testCases.append({
    'input': {
        'cards': [8, 8, 6, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
        'query': 6
    },
    'output': 2
})

#prints all test cases
for testCase in testCases:
    print(testCase)
print()  # Print a newline character after all test cases


#checks whether this method is applicable for all test cases
for test_case in testCases:
    input_data = test_case['input']
    expected_output = test_case['output']

    result = locateCards(**input_data)

    if result == expected_output:
        print("Test passed.")
    else:
        print("Test failed.")
