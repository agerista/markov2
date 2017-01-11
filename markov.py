from random import choice


def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """
    corpus = open(file_path).read()
    return corpus


def make_chains(text_string):
    """Takes input text as string; returns _dictionary_ of markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> make_chains("hi there mary hi there juanita")
        {('hi', 'there'): ['mary', 'juanita'], ('there', 'mary'): ['hi'], ('mary', 'hi': ['there']}
    """

    chains = {}
    n_words = ()
    words = text_string.split()

    for i in range(len(words) - 2):
        n_words = words[i], words[i + 1]
        new_value = words[i + 2]

        if n_words in chains:
            chains[(n_words)].append(new_value)
        else:
            chains[(n_words)] = [new_value]

    return chains


def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""

    text = ""

    random_key = choice(chains.keys())
    #print random_key
    words = random_key[0], random_key[1]
    text = text + random_key[0] + " " + random_key[1]
    next_word = choice(chains[random_key])
    #print next_word
    text = text + " " + next_word
    new_key = random_key[1], next_word
    #print new_key

    while new_key in chains:
        next_word = choice(chains[new_key])
        text = text + " " + next_word
        new_key = new_key[1], next_word

    return text


input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print random_text
