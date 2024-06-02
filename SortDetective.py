import random
import time

class MergeSort:
    def __init__(self, array):
        self.array = array

    def sort(self):
        self.array = self._merge_sort(self.array)
        return self.array

    def _merge_sort(self, array):
        if len(array) <= 1:
            return array

        mid = len(array) // 2
        left_half = self._merge_sort(array[:mid])
        right_half = self._merge_sort(array[mid:])

        return self._merge(left_half, right_half)

    def _merge(self, left, right):
        sorted_array = []
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                sorted_array.append(left[i])
                i += 1
            else:
                sorted_array.append(right[j])
                j += 1

        sorted_array.extend(left[i:])
        sorted_array.extend(right[j:])

        return sorted_array

class BubbleSort:
    def __init__(self, array):
        self.array = array

    def sort(self):
        n = len(self.array)
        for i in range(n):
            swapped = False
            for j in range(0, n - i - 1):
                if self.array[j] > self.array[j + 1]:
                    self.array[j], self.array[j + 1] = self.array[j + 1], self.array[j]
                    swapped = True
            if not swapped:
                break
        return self.array

class InsertionSort:
    def __init__(self, array):
        self.array = array

    def sort(self):
        for i in range(1, len(self.array)):
            key = self.array[i]
            j = i - 1
            while j >= 0 and key < self.array[j]:
                self.array[j + 1] = self.array[j]
                j -= 1
            self.array[j + 1] = key
        return self.array

class SelectionSort:
    def __init__(self, array):
        self.array = array

    def sort(self):
        n = len(self.array)
        for i in range(n):
            min_idx = i
            for j in range(i + 1, n):
                if self.array[j] < self.array[min_idx]:
                    min_idx = j
            self.array[i], self.array[min_idx] = self.array[min_idx], self.array[i]
        return self.array

class QuickSort:
    def __init__(self, array):
        self.array = array

    def sort(self):
        self._quick_sort(0, len(self.array) - 1)
        return self.array

    def _quick_sort(self, low, high):
        if low < high:
            pi = self._partition(low, high)
            self._quick_sort(low, pi - 1)
            self._quick_sort(pi + 1, high)

    def _partition(self, low, high):
        pivot = self.array[high]
        i = low - 1
        for j in range(low, high):
            if self.array[j] < pivot:
                i += 1
                self.array[i], self.array[j] = self.array[j], self.array[i]
        self.array[i + 1], self.array[high] = self.array[high], self.array[i + 1]
        return i + 1

class HeapSort:
    def __init__(self, array):
        self.array = array

    def sort(self):
        n = len(self.array)
        for i in range(n // 2 - 1, -1, -1):
            self._heapify(n, i)
        for i in range(n - 1, 0, -1):
            self.array[i], self.array[0] = self.array[0], self.array[i]
            self._heapify(i, 0)
        return self.array

    def _heapify(self, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        if left < n and self.array[i] < self.array[left]:
            largest = left
        if right < n and self.array[largest] < self.array[right]:
            largest = right
        if largest != i:
            self.array[i], self.array[largest] = self.array[largest], self.array[i]
            self._heapify(n, largest)

if __name__ == "__main__":
    size = int(input("Enter the size of the array: "))
    order = input("Enter the order of the array (ordered, reversed, random): ")

    if order == "ordered":
        array = list(range(size))
    elif order == "reversed":
        array = list(range(size, 0, -1))
    elif order == "random":
        array = [random.randint(1, size) for _ in range(size)]
    else:
        print("Invalid order specified.")
        exit()

    print("Array:", array)

    guess = input("Which sorting algorithm do you think will be most efficient? (bubble, insertion, selection, quick, heap, merge): ")

    algorithms = {
        "bubble": BubbleSort(array.copy()),
        "insertion": InsertionSort(array.copy()),
        "selection": SelectionSort(array.copy()),
        "quick": QuickSort(array.copy()),
        "heap": HeapSort(array.copy()),
        "merge": MergeSort(array.copy())
    }

    best_algo = {
        "ordered": "insertion",
        "reversed": "quick",
        "random": "quick"
    }

    start_time = time.time()
    if guess in algorithms:
        sorted_array = algorithms[guess].sort()
        elapsed_time = time.time() - start_time
        print(f"Sorted array using {guess} sort:", sorted_array)
        print(f"Time taken: {elapsed_time:.6f} seconds")
        if guess == best_algo[order]:
            print("Your guess was correct! This is generally the most efficient sort for this scenario.")
        else:
            print("Your guess was not the best choice for this scenario.")
            print(f"For an {order} array, {best_algo[order]} sort is typically more efficient.")
    else:
        print("Invalid sorting algorithm specified.")
        exit()