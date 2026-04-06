# 🚀 Searching & Sorting Roadmap (Interview Prep)

This roadmap is designed to build strong foundations in:

- 🔍 Searching Techniques
- 🔢 Sorting Algorithms
- 🧠 Problem-solving patterns

---

# 🔹 PHASE 1: Linear Search (Build fundamentals)

### 1. Search an element in an array

Given an array of integers and a target value, return the index of the first occurrence of the target. If the element is not present, return -1.

👉 Edge cases:

- Empty array
- Target at first or last position
- Multiple occurrences
- Negative numbers

---

### 2. Check if an element exists in an array

Return `true` if the element exists, otherwise `false`.

👉 Focus: Early exit once found.

---

### 3. Count occurrences of a number

Count how many times a given number appears in the array.

👉 Edge cases:

- Element appears multiple times
- Element not present → return 0

---

### 4. Find the first occurrence of an element

Return the first index where the element appears.

👉 Important when duplicates exist.

---

### 5. Find the last occurrence of an element

Return the last index where the element appears.

👉 Builds intuition for binary search variants.

---

# 🔹 PHASE 2: Binary Search (Only for sorted arrays)

### 6. Standard Binary Search

Given a sorted array, return the index of a target element. If not found, return -1.

👉 Edge cases:

- Empty array
- Single element
- Target not present
- Only works on sorted arrays

---

### 7. Find the first occurrence using binary search

Return the first index of the target even if duplicates exist.

👉 Key idea: Continue searching left after finding a match.

---

### 8. Find the last occurrence using binary search

Return the last index of the target.

👉 Key idea: Continue searching right after finding a match.

---

### 9. Count occurrences using binary search

Use binary search to count occurrences.

👉 Formula: count = last_occurrence - first_occurrence + 1

---

### 10. Find insertion position (lower bound)

Return the index where an element should be inserted to maintain sorted order.

👉 Edge cases:

- Insert at beginning
- Insert at end
- Insert in middle

---

# 🔹 PHASE 3: Bubble Sort (Start sorting)

### 11. Perform one pass of Bubble Sort

Perform a single pass and observe the largest element moving to the end.

---

### 12. Count swaps in Bubble Sort

Run bubble sort and count total swaps.

👉 Helps understand efficiency.

---

### 13. Fully implement Bubble Sort

Sort array in ascending order.

👉 Edge cases:

- Already sorted
- Reverse sorted
- Duplicates
- Empty array

---

### 14. Optimized Bubble Sort

Stop early if no swaps occur in a pass.

👉 Reduces unnecessary iterations.

---

# 🔹 PHASE 4: Selection Sort

### 15. One iteration of Selection Sort

Find the smallest element and place it at the correct position.

---

### 16. Fully implement Selection Sort

Sort by repeatedly selecting the smallest remaining element.

---

# 🔹 PHASE 5: Insertion Sort

### 17. Insert into sorted array

Insert a number into its correct position in a sorted array.

👉 Core idea behind insertion sort.

---

### 18. Fully implement Insertion Sort

Build the sorted array step by step.

👉 Edge cases:

- Already sorted
- Reverse sorted
- Small arrays

---

# 🔹 PHASE 6: Merge Sort (Divide & Conquer)

### 19. Merge two sorted arrays

Combine two sorted arrays into one sorted array.

👉 Edge cases:

- One array empty
- Different sizes
- Duplicates

---

### 20. Implement Merge Sort

Sort using recursion.

👉 Must:

- Divide array
- Merge sorted halves

👉 Focus: recursion + merging logic.

---

# 🔹 PHASE 7: Quick Sort

### 21. Partition an array

Rearrange elements:

- Smaller than pivot → left
- Greater than pivot → right

👉 Core of quick sort.

---

### 22. Implement Quick Sort

Sort using quick sort.

👉 Edge cases:

- Already sorted
- Reverse sorted
- Many duplicates
- Worst pivot selection

---

# 🔹 PHASE 8: Heap Concepts (Introduction)

### 23. Build a heap (max or min)

Convert array into a heap structure.

👉 Understand parent-child relationships.

---

### 24. Heap Sort

Sort using heap structure.

👉 Steps:

- Build heap
- Extract max/min repeatedly

---

# 🔹 PHASE 9: Bucket Sort

### 25. Bucket Sort (basic version)

Sort numbers using buckets (range: 0–100).

👉 Steps:

- Distribute elements into buckets
- Sort each bucket
- Combine results

👉 Edge cases:

- Skewed data
- Many duplicates

---

# 🎯 Final Goal

By completing this roadmap, you will:

- Master searching techniques
- Understand all major sorting algorithms
- Develop strong problem-solving skills
- Be well-prepared for coding interviews

---

🔥 _Practice each problem by writing code, testing edge cases, and optimizing your solutions._
