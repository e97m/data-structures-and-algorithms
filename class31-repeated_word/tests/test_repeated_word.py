from repeated_word.repeated_word import first_repeated_word_hash

def test_first_repeated_word_hash():
    text = "Once upon a time, there was a brave princess who..."
    assert first_repeated_word_hash(text) == 'a'

def test_first_repeated_word_hash_2():
    text = "It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only..."
    assert first_repeated_word_hash(text) == 'it'

def test_first_repeated_word_hash_3():
    text = "It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn't know what I was doing in New York..."
    assert first_repeated_word_hash(text) == 'summer'

def test_first_repeated_word_hash_empty():
    text = ""
    assert first_repeated_word_hash(text) == 'There are no repeated words.'

def test_first_repeated_word_hash_puctuation():
    text = "Hello, I am Emad. Hello again I am a student at ASAC."
    assert first_repeated_word_hash(text) == 'hello'