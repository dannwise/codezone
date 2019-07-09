def possible_paths(ladder_size):

    result = [0] * (ladder_size + 1) 
    
    # No way to up a zero step ladder.
    result[0] = 0 
    
    # Only one way to up a one step ladder
    result[1] = 1 
    
    # Two ways to up a two steps ladder with one or two step sizes
    result[2] = 2 
    
    # Getting number of possible ways to up a Nth steps ladder with one or two step sizes.
    for i in range(3, ladder_size + 1): 
        result[i] = result[i - 1] + result[i - 2]

    return result[ladder_size] 
