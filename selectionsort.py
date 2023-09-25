def sort(data, first: int):
    """ Sorts a list of integers from smallest to largest
    bypassing the elements to the left of the first.

    Args:
        data (int): list of integers
        first (int): the list index at which the sort will begin.
    """   
    # initialize loop counter variable named i
    i = len(data) - first - 1

    # initialize loop counter variable named j to 0
    j = 0

    # initialize variable named big that will be used to store
    # index of the biggest value
    big = 0


    # initialize variable named temp that will be used
    # to swap list values
    temp = 0

    # loop through list as many times as specified by
    # len(data) and first
    # this loop represents the blue arrow
    while (i > 0):
        # set big equal to first
        big = first

        # set j equal to first + 1
        j = first + 1

        # loop through the list starting with the element at 
        # first + 1 and continue until reach first + i
        # this loop represents the yellow arrow
        while (j <= first + i):
            # if the value in data[big] is less than 
            # data[j]
            if(data[big] < data[j]):
                # set big equal to j
                big = j
            # increment j by 1
            j += 1
        
        # swap the data in first + i with the data in big
        # set temp to value in data[first + i]
        temp = data[first + i]

        # set data[first + i] to the value in data[big]
        data[first + i] = data[big]

        # set data[big] to the value in temp
        data[big] = temp

        # decrement i by 1
        i -= 1

