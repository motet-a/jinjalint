import collections


def flatten(iterable):
    """
    Deeply flattens an iterable.
    """
    for element in iterable:
        if (isinstance(element, collections.Iterable) and
                not isinstance(element, (str, bytes))):
            yield from flatten(element)
        else:
            yield element
