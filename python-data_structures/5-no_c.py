def no_c(my_string):
    """Remove all characters 'c' and 'C' from a string."""
    return "".join(char for char in my_string if char not in ('c', 'C'))
