# It's a combination of two things: [merging and sorting]!
# Exploits the fact that arrays of 0 or 1 element are always sorted
# Works by decomposing an array into smaller arrays of 0 or 1 elements, 
# then building up a newly sorted array

# STEPS 
# 1. Divide the array, e.j [1, 2, 4, 3] => [1, 2], [4, 3]
# 2. Divde the new array again: [1, 2] => [1], [2] &&  [4, 3] => [4], [3]
# 3. Join and sort the single items: [1], [2] => [1, 2] && [4], [3] => [3, 4]
# 4. join and sort the arrays again [1, 2] && [3, 4] => [1, 2, 3, 4]

# Best time complexity: O(n log n)
# Time complexity average: O(n log n)
# Time complexity worst: O(n log n)
# Space complexity: O(n)

# Notes: For this algorithm does not care if the data is sorted 
# or the data length also there is not edge cases

def merge(arrA, arrB):
    i = 0
    j = 0
    result = []

    while(i <= len(arrA) and j <= len(arrB)):
        arrAIsLooped = (i >= len(arrA))
        arrAValue = arrA[i] if not arrAIsLooped else -1
        
        arrBIsLooped = (j >= len(arrB))
        arrBValue = arrB[j] if not arrBIsLooped else -1

        if arrAIsLooped and arrBIsLooped:
            break

        if (arrAValue < arrBValue) and not arrAIsLooped:
            i += 1
            result.append(arrAValue) 
            continue

        if (arrBValue < arrAValue) and not arrBIsLooped:
            j += 1
            result.append(arrBValue)
            continue

        if not arrAIsLooped  and  arrBIsLooped:
            nextLoop = i + 1
            nextItem = arrA[nextLoop] if (nextLoop + 1) <= len(arrA) else None
            i += 1

            if nextItem:
                result.append(arrAValue if arrAValue < nextItem else nextItem)
            else:
                result.append(arrAValue)   
        
        if not arrBIsLooped and arrAIsLooped:
            nextLoop = j + 1
            nextItem = arrB[nextLoop] if nextLoop + 1 <= len(arrB) else None
            j += 1

            if (nextItem):
                result.append(arrBValue if arrBValue < nextItem else nextItem)
            else:
                result.append(arrBValue)           
    
    return result



def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    middle = len(arr) // 2
    left_arr = merge_sort(arr[:middle])
    rigth_arr = merge_sort(arr[middle:])

    return merge(left_arr, rigth_arr)


print(merge_sort([10,24,76,73, 199]))
