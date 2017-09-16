#!/usr/bin/env python

def get_number_of_value_crossings(signal, value):
    """ Determine the number of times a signal (numeric array) crosses a value.
        signal == value is not counted as a crossing """
    # sign is defined as +1 if signal > value, -1 if signal < value,
    # and 0 if signal == value
    old_sign = 0
    new_sign = 0
    n = 0 # Number of times a crossing occurs.
    for i in range(len(signal)):
        # Store the sign of the previous signal value if non-zero
        if new_sign != 0:
            old_sign = new_sign

        # Set the current sign
        if signal[i] > value:
            new_sign = 1
        elif signal[i] < value:
            new_sign = -1
        else:
            new_sign = 0

        # If the sign is non-zero and has changed, a crossing occured
        if i != 0 and new_sign != 0 and new_sign != old_sign:
            n += 1

    return n

def test_func():
    """ Simple test for get_number_of_value_crossings function """
    value = 5
    signal = [1, 2, 3, 4, 5, 5, 5, 4, 3, 4, 5, 5, 6, 7, 4, 6, 5, 5, 7]
    result = get_number_of_value_crossings(signal, value)
    if result == 3:
        print 'Test passed, result = ' + str(result)
    else:
       print 'Test failed, result = ' + str(result)

if __name__ == '__main__':
    test_func()
