#quick sort in recursive way
# Time complxity: O(n*log(n))

class QuickSort(object):
    def __init__(self, arr):
        self.arr = arr
        self.quick_sort(0, len(self.arr)-1)
        print(self.arr)

    def quick_sort(self, start, end):
        if start >= end:
            return

        left = start
        right = end
        piv = self.arr[(start+end)//2]
        while left <= right:
            while self.arr[left] < piv:
                left += 1
            while self.arr[right] > piv:
                right -= 1
            if left <= right:
                self.arr[left], self.arr[right] = self.arr[right], self.arr[left]
                left += 1
                right -= 1
        self.quick_sort(start, right)
        self.quick_sort(left, end)


if __name__ == '__main__':
    arr = [1, 3, 5, 2, 4, 6]
    QuickSort(arr)
