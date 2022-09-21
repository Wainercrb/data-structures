// - Like merge sort, exploits the fact that arrays of 0 or 1 element
//   are always sorted
// - Works by selecting one element(called the "pivot") and finding the 
//   index where the pivot should end up in the sorted array
// - Once the pivot is positioned appropriately, quick sort can be applied 
//   on either side of the pivot

// STEPS 
// 1. Pick one element, e.j first item(idx=5): [5, 2, 1, 8, 4, 7, 6, 3] => 5
// 2. Move all the numbers that are less than 5 to the left and
//    move all the numbers that are greater than 5, e.j: 
//    [3, 2, 1, 4] + 5 + [7, 6, 8] => [2, 1, 4, 3, 5, 7, 6, 8]
// 3. Repeat the process with the left side(idx=3), e.j:
//    [3, 1, 4, 2] => [1, 2] + 3 + [4] => [1, 2, 3, 4]   
// 4. Repeat the process with the rest(idx=1), e.j:
//    [] + 1 + [2] = [1, 2] => [1, 2, 3, 4, 5, 7, 6, 8]
// 7. Repeat the process with the rith side(idx=7), e.j: 
//    [6] + 7 + [8] => [6, 7, 8]

// Best time complexity: O(n log n)
// Time complexity average: O(n log n)
// Time complexity worst: O(n^2)
// Space complexity: O(log n)

// Notes: If we have the sorted data the algorithm going to loop all the data

function pivot(arr, start = 0, end = arr.length - 1) {
  const swap = (arr, idx1, idx2) => {
    [arr[idx1], arr[idx2]] = [arr[idx2], arr[idx1]];
  };

  // We are assuming the pivot is always the first element
  let pivot = arr[start];
  let swapIdx = start;

  for (let i = start + 1; i <= end; i++) {
    if (pivot > arr[i]) {
      swapIdx++;
      swap(arr, swapIdx, i);
    }
  }

  // Swap the pivot from the start the swapPoint
  swap(arr, start, swapIdx);
  return swapIdx;
}


function quickSort(arr, left = 0, right = arr.length -1){
    if(left < right){
        let pivotIndex = pivot(arr, left, right) //3
        //left
        quickSort(arr,left,pivotIndex-1);
        //right
        quickSort(arr,pivotIndex+1,right);
      }
     return arr;
} 
           
quickSort([100,-3,2,4,6,9,1,2,5,3,23]);


