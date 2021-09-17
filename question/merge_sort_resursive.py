


def merge_sort_recursive(array):
    if len(array) <= 1:
        return array
    mid = len(array) // 2
    left = merge_sort_recursive(array[:mid])
    right = merge_sort_recursive(array[mid:])
    return merge(left, right)


def merge(left, right):
    result = []
    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    if len(left) > 0:
        result.extend(left)
    if len(right) > 0:
        result.extend(right)
    return result


if __name__ == '__main__':
    array = [1, 3, 5, 7, 2, 4, 6, 8]
    print(merge_sort_recursive(array))




