import math
def is_a_triple(n):
    """Return True if n is a multiple of 3; False otherwise."""
    return n % 3 == 0

def last_prime(m):
    """Return the largest prime number p that is less than or equal to m.
    You might wish to define a helper function for this.
    You may assume m is a positive integer."""
    while (not is_prime(m)):
        m -= 1
    return m
    
def is_prime(m):
    n = m - 1
    while (n < 1):
        if (m % n == 0):
            return False
        n -= 1
    return True

def quadratic_roots(a, b, c):
    """Return the roots of a quadratic equation (real cases only).
    Return results in tuple-of-floats form, e.g., (-7.0, 3.0)
    Return "complex" if real roots do not exist."""
    if (((b*b) - (4*a*c)) < 0):
        return "complex"
    return ((-1*b + math.sqrt(b*b - 4*a*c))/(2*a), (-1*b - math.sqrt(b*b - 4*a*c))/(2*a))
    

def new_quadratic_function(a, b, c):
    """Create and return a new, anonymous function (for example
    using a lambda expression) that takes one argument x and 
    returns the value of ax^2 + bx + c."""
    return lambda x: a*x*x + b*x + c

def perfect_shuffle(even_list):
    """Assume even_list is a list of an even number of elements.
    Return a new list that is the perfect-shuffle of the input.
    Perfect shuffle means splitting a list into two halves and then interleaving
    them. For example, the perfect shuffle of [0, 1, 2, 3, 4, 5, 6, 7] is
    [0, 4, 1, 5, 2, 6, 3, 7]."""
    first_half = even_list[:even_list.len()/2]
    second_half = even_list[even_list.len()/2:]
    result = []
    for x in range (first_half.len()):
        result.append(first_half[x])
        result.append(second_half[x])
    return result

def list_of_3_times_elts_plus_1(input_list):
    """Assume a list of numbers is input. Using a list comprehension,
    return a new list in which each input element has been multiplied
    by 3 and had 1 added to it."""

def triple_vowels(text):
    """Return a new version of text, with all the vowels tripled.
    For example:  "The *BIG BAD* wolf!" => "Theee "BIIIG BAAAD* wooolf!".
    For this exercise assume the vowels are
    the characters A,E,I,O, and U (and a,e,i,o, and u).
    Maintain the case of the characters."""

def count_words(text):
    """Return a dictionary having the words in the text as keys,
    and the numbers of occurrences of the words as values.
    Assume a word is a substring of letters and digits and the characters
    '-', '+', *', '/', '@', '#', '%', and "'" separated by whitespace,
    newlines, and/or punctuation (characters like . , ; ! ? & ( ) [ ] { } | : ).
    Convert all the letters to lower-case before the counting."""

