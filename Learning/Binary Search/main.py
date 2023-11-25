def BinarySearch(orderedList, elementToSearch):
    start = 0
    end = len(orderedList)-1
    pos = BinarySearchRec(orderedList, elementToSearch, start, end)
    if pos >= 0:
        print(f'element found at index {pos+1}')
    else:
        print('element not found in the list')


def BinarySearchRec(orderedList, elementToSearch, start, end):
    if start > end:
        return -1
    mid = (int)((start+end)/2)
    if orderedList[mid] == elementToSearch:
        return mid
    elif orderedList[mid] > elementToSearch:
        return BinarySearchRec(orderedList, elementToSearch, start, mid-1)
    else:
        return BinarySearchRec(orderedList, elementToSearch, mid+1, end)


# This code will run because my_script.py is being executed directly.
if __name__ == '__main__':
    orderedList = [int(x)
                   for x in input('Enter list separated by spaces: ').split()]
    # [print(x) for x in orderedList]
    elementToSearch = int(input('enter element to search:'))
    BinarySearch(orderedList, elementToSearch)
