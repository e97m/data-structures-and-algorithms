from class10_stack_and_queue.brackets import validate_brackets

def test_brackets_1():
    assert validate_brackets('()') == True

def test_brackets_2():
    assert validate_brackets('()[]{}') == True

def test_brackets_3():
    assert validate_brackets('(]') == False

def test_brackets_4():
    assert validate_brackets('([)]') == False

def test_brackets_5():
    assert validate_brackets('(){}[[]]') == True

def test_brackets_6():
    assert validate_brackets('{[()]}') == True

def test_brackets_7():
    assert validate_brackets('{}{Code}[Fellows](())') == True

def test_brackets_8():
    assert validate_brackets('{') == False

def test_brackets_9():
    assert validate_brackets(')') == False