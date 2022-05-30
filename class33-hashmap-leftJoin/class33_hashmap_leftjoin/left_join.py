
def left_join(left_table, right_table):
    """
    Left join two hashmaps
    Input: two hashmaps
    Output: a list of tuples
    """
    new_table = {}
    for key, value in left_table.items():
        if key in right_table:
            new_table[key] = value + ',' + right_table[key]
        else:
            new_table[key] = value + ',' + 'NULL'
    return new_table


if __name__ == '__main__':
    left_table = {'a': '1', 'b': '2', 'c': '3'}
    right_table = {'a': '4', 'b': '5', 'd': '6'}

    print(left_join(left_table, right_table))
