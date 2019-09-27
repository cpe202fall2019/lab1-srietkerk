
def max_list_iter(int_list):  # must use iteration not recursion
    """finds the max of a list of numbers and returns the value (not the index)
    If int_list is empty, returns None. If list is None, raises ValueError"""
    pass
    if int_list == None: #error for None value
        raise ValueError
    elif len(int_list) == 0: #empty list return
        return None
    maxi = int_list[0] #the first num is the first max as only current element checked
    for num in int_list:
        if num > maxi:
            maxi = num
    return maxi


def reverse_rec(int_list):   # must use recursion
    """recursively reverses a list of numbers and returns the reversed list
    If list is None, raises ValueError"""
    if int_list == None: #error for None value
        raise ValueError
    if len(int_list) == 1 or len(int_list) == 0: #base case; only one element in list, have reached the end
        return int_list
    var = reverse_rec(int_list[1:]) #recursive call, slices list until one element in list
    var.append(int_list[0])
    return var


def bin_search(target, low, high, int_list):  # must use recursion
    """searches for target in int_list[low..high] and returns index if found
    If target is not found returns None. If list is None, raises ValueError """
    if int_list == None:
        raise ValueError
    if len(int_list) == 0:
        return None
    mid = (high + low) // 2
    if target == int_list[mid]:
        return mid
    if high == low: 
        return None
    if target > int_list[mid]:
        return bin_search(target, mid + 1, high, int_list)
    if target < int_list[mid]:
        return bin_search(target, low, mid - 1, int_list)

