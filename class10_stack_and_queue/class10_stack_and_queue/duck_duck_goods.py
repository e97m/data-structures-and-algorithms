from stack_and_queue import Queue

def duck_duck_goods_queue(string,k):
    '''
    A function to play the game Duck Duck Goods
    input: string, k(int)
    output: the last character remaining in the string queue
    '''
    if type(k) is not int or k<1:
        return 'k must be an integer greater than 0'
    if len(string) == 1:
        return string

    queue= Queue()

    for char in string:
        queue.enqueue(char)

    for _ in range(len(string)-1):
        for _ in range(k-1):
            queue.enqueue(queue.dequeue())
        queue.dequeue()

    return queue.dequeue()


if __name__ == '__main__':
    print(duck_duck_goods_queue('abcdefghijklmnopqrstuvwxyz',3))
    print(duck_duck_goods_queue('a',3))
    print(duck_duck_goods_queue('abcdefghijklmnopqrstuvwxyz',1))
    print(duck_duck_goods_queue('abcdefghijklmnopqrstuvwxyz',0))
    print(duck_duck_goods_queue('abcdefghijklmnopqrstuvwxyz',-1))