from collections import Counter
import string, re



class HashTable(object):
    def __init__(self, size=1024):
        self.size = size
        self.table = [None] * size

    def hash(self, key):
        """
        A method to hash the key according to ASCII size
        Input: key
        Output: hash value
        """
        sum_of_ascii = 0
        for ch in key:
            ch_ascii = ord(ch)  # 86
            sum_of_ascii += ch_ascii
        hashed_key = (sum_of_ascii * 19) % self.size
        return hashed_key

    def set(self, key, value):
        """
        A method to hash the key, then set the key and value pair in the table, handling collisions as needed
        Input: key, value
        Output: othing
        """
        idx = self.hash(key)
        if not self.table[idx]:
            self.table[idx] = [[key, value]]  # LinkedList().add({key, value})
        else:
            self.table[idx].append([key, value])

    def get(self, key):
        """
        A method to retrieve the vlaue of a key
        Input: key
        Output: value
        """
        return self.table[self.hash(key)]

    def contains(self, key):
        """
        A method to check if the key is already in the hash table
        Input: key
        Output: boolean
        """
        if self.get(key) is not None:
            return True
        else:
            return False

    def keys(self):
        """
        A method to retrieve the keys of a hash table
        Input: nothing
        Output: list of keys
        """
        # return [key[0][0] for key in self.table if key is not None]
        keys = []
        for bucket in self.table:
            if bucket is not None:
                keys.append(bucket[0][0])
        return keys


    def most_common_key(self):
        '''Finds the most common key in the table'''
        most_common = []
        for bucket in self.table:
            if bucket is not None:
                if len(bucket) > len(most_common):
                    most_common = bucket
        return most_common[0][0]


    def max_count(self):
        '''Finds the how many times the most common key appears in the table'''
        max_count = 0
        for bucket in self.table:
            if bucket is not None:
                if len(bucket) > max_count:
                    max_count = len(bucket)
        return max_count


    def __str__(self):
            output = ""
            for bucket in self.table:
                if bucket is not None:
                    output += f"{bucket} \n"
            return output


def first_repeated_word_hash(text):
    '''
    Finds the first repeated word in a string.
    Input: string
    Output: string
    '''
    if text == '': raise Exception('Text is empty')

    # lower case all letters
    text = text.lower() 

    # remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    # or  
    re.sub(pattern = "[^\w\s]", repl = "", string = text)

    text = text.split(' ') 

    ht = HashTable()
    for word in text:
        if ht.contains(word):
            return word
        else:
            ht.set(word, 1)
    for word in text:
         ht.set(word, 1)
    return 'There are no repeated words.'


# Not compleated
def all_repeated_words_hash(text):
    '''
    if text == '': raise Exception('Text is empty')
    Finds all repeated words in a string.
    Input: string
    Output: string
    '''
    text = text.lower() 
    text = text.translate(str.maketrans('', '', string.punctuation))  
    text = text.split(' ')
    ht = HashTable()
    for word in text:
        ht.set(word, 1)
    


def all_repeated_words(text):
    '''
    Finds all repeated words in a string.
    Input: string
    Output: string
    '''
    if text == '': raise Exception('Text is empty')
    repeated = []
    text = text.lower() 
    text = text.translate(str.maketrans('', '', string.punctuation))   # remove punctuation
    text = text.split(' ') # split into words
    text_counted = Counter(text) 
    for word in text_counted: 
        if text_counted[word] > 1: # words appears more than once
            repeated.append(word) 
    if len(repeated) <1:
        return 'There are no repeated words.'
    return repeated


def most_common_word_hash(text):
    '''
    Finds the most common word in a string.
    Input: string
    Output: string
    '''
    if text == '': raise Exception('Text is empty')
    text = text.lower() 
    re.sub(pattern = "[^\w\s]", repl = "", string = text)
    text = text.split(' ')
    ht = HashTable()
    counter = 1
    for word in text:
        ht.set(word, counter)
        counter += 1
    return ht.most_common_key()


def most_common_word(text):
    if text == '': raise Exception('Text is empty')
    text = text.lower()
    re.sub(pattern = "[^\w\s]", repl = "", string = text)
    text = text.split(' ')

    ht = HashTable()
    counter = 1
    temp_max = ''
    temp_max_num = 0
    for word in text:
        if ht.contains(word):
            ht.set(word, int(ht.get(word)[0][1])+1)
            if ht.get(word)[-1][1] > temp_max_num:
                temp_max = word
        else:
            ht.set(word, counter)

    return temp_max
        
            





if __name__ == '__main__':
    print(first_repeated_word_hash('Enter a string: this is an example. an apple a day'))
    print(most_common_word_hash('Enter a string: this is an example. an apple a day'))
    print(most_common_word('Enter a string: this is an example. an apple a day'))