# Add your clarifying questions here

def rotate_list(list_of_stuff, rotator):  # O(n) time complexity, O(n) space complexity
    list_len = len(list_of_stuff)
    temp_list = [None] * list_len
    for i in list_of_stuff:
        new_index = (list_of_stuff.index(i) + rotator) % list_len
        if new_index >= list_len:
            new_index = new_index - list_len
        temp_list[new_index] = i
    return temp_list

def rotate_list_slicing(list_of_stuff: list, rotator): # O(1) time complexity, O(n) space complexity
    rotator = -(rotator % len(list_of_stuff))
    list_of_stuff = list_of_stuff[rotator:] + list_of_stuff[:rotator]
    return list_of_stuff

def rotate_list_in_place(list_of_stuff: list, rotator): # O(n) time complexity, O(1) space complexity
    rotator = rotator % len(list_of_stuff)
    for _ in range(rotator):
        item = list_of_stuff.pop()
        list_of_stuff.insert(0, item)
    return list_of_stuff

# print(rotate_list(["a", "b", "c"], 1))
# print(rotate_list_slicing(["a", "b", "c"], 1))
# print(rotate_list_in_place(["a", "b", "c"], 1))
print(f"{rotate_list([1, 2, 3, 4, 5, 6, 7, 8, 9], 13) = }")
print(f"{rotate_list_slicing([1, 2, 3, 4, 5, 6, 7, 8, 9], 13) = }")
print(f"{rotate_list_in_place([1, 2, 3, 4, 5, 6, 7, 8, 9], 13) = }")
