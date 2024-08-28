#parenthesis print count

def check_arrangement(input_string):
    open_count = 0
    close_count = 0
    arrangement = True
    for char in input_string:
        if char == '(':
            open_count += 1
        else:
            close_count += 1
        if open_count < close_count:
            arrangement = False
            break
    if arrangement and open_count == close_count:
        print('Valid Parenthesis Arrangement')
        print('Parenthesis count: ', open_count)
    else:
        print('Invalid Parenthesis Arrangement')


    