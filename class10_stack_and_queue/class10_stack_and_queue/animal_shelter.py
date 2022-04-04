
class Node:
    '''
    A class to create a node
    Input: the value of the data for the node.
    constructor: vlaue, next (pointer to the next)
    '''
    def __init__(self,value):
        self.value = value
        self.next = None

class AnimalShelter:
    '''
    A class to creat an animal queue for the animal shelter
    Input: no input
    constructor: front node, rear node
    '''

    def __init__(self):
        self.front = None
        self.rear = None
    

    def enqueue(self, new_animal):
        '''
        A method to add animal to the shelter queue (to the rear)
        Input: type of the new animal (cat/dog)
        '''
        if new_animal != 'cat' and new_animal != 'dog':
            if type(new_animal) is Node:
                # I can do: (new_node = new_value) or even loop thogh the nested Nodes till I reach to the str value, but I prefere to inform the user to do this manually
                return 'Please enter the animal type as a value (string) and it will converted to Node automaticly'
            return 'We only receive dogs and cats'
        else:
            new_node = Node(new_animal)
            if  self.front is None:
                    self.front = new_node
                    self.rear = new_node
            else:
                    self.rear.next = new_node
                    self.rear = new_node


    def dequeue(self, pref = None):
        '''
        A method to remove the input animal if it was at the peek (front) of the shelter queue
        Input: type of the animal you prefere (cat/dog)
        '''
        if self.front is None:
                return 'The shelter queue is empty'
        else: 
            if pref == None or (pref != 'dog' and pref != 'cat'):
                return self.dequeue(self.front.value)
            else: 
                previous = None
                current = self.front
                while current is not None:
                    if current.value == pref:
                        if previous is not None: # to handle dequeueing the first node
                            previous.next = current.next
                        else: # to handle dequeueing a node that is not the first
                            self.front = current.next
                        current.next = None
                        return current.value
                    previous = current
                    current = current.next
            

        # I recommend using linked list insted of queue if the middle Nodes needed to be accessed.
        # for the queue solution I recommend the following:
        # if self.front is None:
        #         return 'The shelter queue is empty'
        # else: 
        #     the_peek = self.front.value
        #     if the_peek == pref:
        #         current = self.front
        #         self.front = self.front.next
        #         current.next = None
        #         return current.value
        #     elif pref == None or (pref != 'dog' and pref != 'cat'):
        #         return self.dequeue(the_peek)
        #     else:
        #         return f'Sorry!! The available animal is not {the_peek}'
                

    def __str__(self):
        '''
        A method to print the animal shelter queue
        Input: nothing
        Output: string
        '''
        output = ''
        if self.front is None:
            return 'The shelter queue is empty'
        else:
            current = self.front
            while current is not None:
                output += '{ ' f'{current.value}' ' } -> '
                current = current.next
            output += 'Null'
        return  output

    


if __name__ == '__main__':
    shelter = AnimalShelter()
    shelter.enqueue('dog')
    shelter.enqueue('cat')
    shelter.enqueue('dog')
    shelter.enqueue('dog')
    print(shelter)

    print(shelter.dequeue('cat'))
    print(shelter)
    print(shelter.dequeue('dog'))
    print(shelter)
    print(shelter.dequeue())
    print(shelter)
    print(shelter.dequeue('rabit'))
    print(shelter)
    print(shelter.enqueue('rabit'))
