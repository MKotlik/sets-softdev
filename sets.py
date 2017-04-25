# List Comprehensions
# Misha Kotlik

# SETS ARE RESTRICTED TO ONLY HAVE UNIQUE ELEMENTS

def union(A, B):
    unionized = [i for i in A]
    unionized += [i for i in B if i not in A]
    return unionized


def intersection(A, B):
    intersected = [i for i in B if i in A]
    return intersected


def set_difference(U, A):
    difference_set = [i for i in U if i not in A]
    return difference_set


def symmetric_difference(A, B):
    unionized = [i for i in A]
    unionized += [i for i in B if i not in A]
    intersected = [i for i in B if i in A]
    return [i for i in unionized if i not in intersected]


def cartesian_product(A, B):
    product = [(x, y) for x in A for y in B]
    return product
