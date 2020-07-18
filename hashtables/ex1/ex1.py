# def test_ex1_3(self):
#     weights_3 = [4, 6, 10, 15, 16]
#     answer_3 = get_indices_of_item_weights(weights_3, 5, 21)
#     self.assertTrue(answer_3[0] == 3)
#     self.assertTrue(answer_3[1] == 1)

def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    storage = {}

    for i in range(length):
        storage[weights[i]] = i

    for i in range(length):
        result = limit - weights[i]
        if result in storage:
            return (max(i, storage[result]), min(i, storage[result]))

    return None
