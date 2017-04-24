# List Comprehensions
# Misha Kotlik

def union(A, B):
    unionized = [i for i in A]
    unionized += [i for i in B]
    return unionized
