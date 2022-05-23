# from collections import Counter
import string



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
    text = text.lower() 
    text = text.translate(str.maketrans('', '', string.punctuation))   # remove punctuation
    text = text.split(' ') 
    ht = HashTable()
    for word in text:
        if ht.get(word):
            return word
        else:
            ht.set(word, 1)
    for word in text:
         ht.set(word, 1)
    return 'There are no repeated words.'


# Not compleated
def all_repeated_words_hash(text):
    '''
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
    text = text.lower() 
    text = text.translate(str.maketrans('', '', string.punctuation))   # remove punctuation
    text = text.split(' ') # split into words
    text_counted = Counter(text) 
    for word in text_counted: 
        if text_counted[word] > 1: # return the first word appears more than once
            return word
    return 'There are no repeated words.'





if __name__ == '__main__':
    print(first_repeated_word_hash('Enter a string: this is an example. an apple a day'))