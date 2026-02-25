class Solution: 
    def selectionSort(self, arr):
        #code here
        n = len(arr)
        minimum = arr[0]
        minimum_index = 0
        for i in range(n):
            for j in range(i, n):
                if arr[j] < minimum:
                    minimum = arr[j]
                    minimum_index = j
                else:
                    continue
            current_num = arr[i]
            arr[i] = minimum
            arr[minimum_index] = current_num
            minimum = float("inf")
        return arr 
