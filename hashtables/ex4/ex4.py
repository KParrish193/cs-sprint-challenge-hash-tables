def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    
    # empty list
    result = []

    # empty dictionary
    positive_numbers = {}

    # loop through provided list 'a'
    for i in a:
        # look dupes among absolute values of numbers
        if abs(i) in positive_numbers:
            # add confirmed dupes to result list
            result.append(abs(i))
        else: 
            # make table of absolute value of numbers in 'a', key = number, value = 1
            positive_numbers[abs(i)] = 1

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))

# plan: 
#   1) loop through given list of numbers
#   2) determine a way of matching positive and negative numbers to find match - absolute value
#   3) search for dupes
#   4) return the matches of dupes