# It's a combination of two things: [merging and sorting]!
# Exploits the fact that arrays of 0 or 1 element are always sorted
# Works by decomposing an array into smaller arrays of 0 or 1 elements, 
# then building up a newly sorted array

# STEPS 
# 1. Divide the array, e.j [1, 2, 4, 3] => [1, 2], [4, 3]
# 2. Divde the new array again: [1, 2] => [1], [2] &&  [4, 3] => [4], [3]
# 3. Join and sort the single items: [1], [2] => [1, 2] && [4], [3] => [3, 4]
# 4. join and sort the arrays again [1, 2] && [3, 4] => [1, 2, 3, 4]

# Complexity: O(n + m)
# Time: O(n + m)

def merge_sort(arrA, arrB):
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
            nextItem = arrB[nextLoop] if j + 1 <= len(arrB) else None
            j += 1

            if (nextItem):
                result.append(arrBValue if arrBValue < nextItem else nextItem)
            else:
                result.append(arrBValue)           
    
    return result


print(merge_sort([100,200, 400, 500, 600, 700], [1,2,3,5,6]))
