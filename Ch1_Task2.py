def square_number(number):

    return number*number

def test_square_number():
    assert square_number(2) == 4
    assert square_number(8) == 64
    assert square_number(10) == 100
    print('Your code is Correct')

test_square_number()