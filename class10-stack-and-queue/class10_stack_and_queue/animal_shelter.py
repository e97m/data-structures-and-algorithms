
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
    A class to creat two queues, one fir dogs and the other for cats
    '''
    def __init__(self):
        self.cats_queue = AnimalQueue()
        self.dogs_queue = AnimalQueue()
        # self.all_animals_queue = AnimalQueue()


    def add_animal(self, new_animal):
        '''
        A method to deside where to enqueue the new animal (dog queue or cat queue)
        Input: new animal
        '''
        if new_animal == 'cat':
            self.cats_queue.enqueue(new_animal)
            # self.all_animals_queue.enqueue(new_animal)
        elif new_animal == 'dog':
            self.dogs_queue.enqueue(new_animal)
            # self.all_animals_queue.enqueue(new_animal)
        else:
            return 'We only receive dogs and cats'


    def request_animal(self, pref = None):
        '''
        A method to deside from where to dequeue the recuested anomal (dog queue or cat queue)
        Input: preference
        '''
        if pref == None:
            # return self.all_animals_queue.dequeue()
            return 'Please enter the animal type as a value (string)'
        elif pref == 'cat':
            return self.cats_queue.dequeue()
        elif pref == 'dog':
            return self.dogs_queue.dequeue()
        else:
            return 'We only have dogs and cats'



class AnimalQueue:
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
            return 'We only receive dogs and cats'
        else:
            if type(new_animal) is Node:
                return 'Please enter the animal type as a value (string) and it will converted to Node automaticly'
            else:
                new_node = Node(new_animal)

            if  self.front is None:
                    self.front = new_node
                    self.rear = new_node
            else:
                    self.rear.next = new_node
                    self.rear = new_node
            

    def dequeue(self):
        '''
        A method to remove the oldest anomal in the queue
        '''
        if self.front is None:
            return 'The shelter queue for this animal type is empty'
        else: 
            current = self.front
            self.front = self.front.next
            current.next = None
            return current.value
            

    def __str__(self):
        '''
        A method to print the animal shelter queue
        Input: nothing
        Output: string
        '''
        output = ''
        if self.front is None:
            return 'The shelter queue for this animal type is empty'
        else:
            current = self.front
            while current is not None:
                output += '{ ' f'{current.value}' ' } -> '
                current = current.next
            output += 'Null'
        return  output

    


if __name__ == '__main__':
    shelter = AnimalShelter()
    shelter.add_animal('dog')
    shelter.add_animal('cat')
    shelter.add_animal('dog')
    shelter.add_animal('dog')
    shelter.add_animal('cat')
    print(shelter.dogs_queue)
    print(shelter.cats_queue)
    # print(shelter.all_animals_queue)

    print(shelter.request_animal('cat'))
    print(shelter.dogs_queue)
    print(shelter.cats_queue)
    # print(shelter.all_animals_queue)
    print(shelter.request_animal('dog'))
    print(shelter.dogs_queue)
    print(shelter.cats_queue)
    # print(shelter.all_animals_queue)
    print(shelter.request_animal())
    print(shelter.dogs_queue)
    print(shelter.cats_queue)
    # print(shelter.all_animals_queue)

    shelter.request_animal('cat')
    print(shelter.request_animal('cat'))

    print(shelter.add_animal('rabit'))
    print(shelter.request_animal('rabit'))


