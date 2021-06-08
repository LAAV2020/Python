""" Homework assignment for week 3 """


# Adam Vickter


def words_containing(sentence, letter):
    """ Given a sentence, returns list of words that contain the letter.
        Letter given is lowercase. Sentence can be mixed case, and the
        case should be ignored for searching.
    """
    result = []
    words = sentence.split(" ")
    for item in words:
        if letter.lower() in item.lower():
            result.append(item)
    return result


def len_safe(object):
    """Return length of object or -1 if object has no length."""
    try:
        return len(object)
    except:
        return -1


def unique(sequence):
    """Yield iterable elements in order, skipping duplicate values."""
    result = []
    for item in sequence:
        if item not in result:
            yield item
            result.append(item)
