import random, string


def random_word(length):
    return ''.join(random.choice(string.ascii_letters or string.ascii_lowercase) for i in range(length))


def generate_filename(original_filename):
    dots = original_filename.split('.')
    extension = dots[len(dots) - 1]
    new_name = random_word(6) + '.' + extension
    return new_name
