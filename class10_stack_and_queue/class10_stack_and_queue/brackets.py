from class10_stack_and_queue.stack_and_queue import Stack

def validate_brackets(my_str):
    '''
    A function to validate the brackets in a string
    Input: string
    Output: boolean
    '''
    stack = Stack()
    for char in my_str:
        if char == '(' or char == '[' or char == '{':
            stack.push(char)
        elif char == ')' or char == ']' or char == '}':
            if stack.is_empty():
                return False
            else:
                if char == ')' and stack.peek() == '(':
                    stack.pop()
                elif char == ']' and stack.peek() == '[':
                    stack.pop()
                elif char == '}' and stack.peek() == '{':
                    stack.pop()
                else:
                    return False
    if stack.is_empty():
        return True
    else:
        return False


if __name__ == '__main__':
    print(validate_brackets('()[]{}'))
    print(validate_brackets('(]'))
    print(validate_brackets('([)]'))
    print(validate_brackets('(){}[[]]'))
    print(validate_brackets('{[()]}'))
    print(validate_brackets('{}{Code}[Fellows](())'))
    print(validate_brackets('{'))
    print(validate_brackets(')'))