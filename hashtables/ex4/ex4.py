# def test_small(self):
#     result = has_negatives([1,2,3])
#     self.assertTrue(result == [])

#     result = has_negatives([1,2,3,-4])
#     self.assertTrue(result == [])

#     result = has_negatives([-1,-2,1,2,3,4,-4])
#     result.sort()
#     self.assertTrue(result == [1,2,4])]


def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    result = []
    storage = {}

    for num in a:
        storage[num] = 1
        if num != 0 and -num in storage:
            result.append(abs(num))
    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
