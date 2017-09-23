import random, string


def random_word(length):
    return ''.join(random.choice(string.ascii_letters or string.ascii_lowercase) for i in range(length))
