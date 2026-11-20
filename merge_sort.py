# divide the list into list segments, compairing the segments for order recursively

def merge_sort(scores):
    if len(scores) <= 1:
        return scores
    
    mid = len(scores) // 2
    left = merge_sort(scores[:mid])
    right = merge_sort(scores[mid:])

    return merge(left, right) # writing this later


def merge(left, right):
    # combine the 2 sorted lists
    result = []
    if left[0] >= right[0]:
        result.append(left[0])
        result.append(right[0])
    else:
        result.append(right[0])
        result.append(left[0])
    return result


print(merge_sort([340, 820, 150, 999, 430, 275]))

