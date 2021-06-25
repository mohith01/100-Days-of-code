def binary_search(list1, item):
    low = 0
    high = len(list1)-1
    while low<=high:
        mid = (low+high)//2
        guess = list1[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid -1
        else:
            low = mid +1
    return None

print(binary_search([1,3,4,5,6,9,11],4))
