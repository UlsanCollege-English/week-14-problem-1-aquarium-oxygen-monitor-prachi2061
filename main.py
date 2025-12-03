
## main.py
```python
"""
HW01 — Aquarium Oxygen Monitor (Sliding Window)

Implement max_window_sum(readings, k) to return the maximum sum of any
contiguous subarray of length k.

See README.md for full problem description and constraints.
"""


def max_window_sum(readings, k):
    """
    Return the maximum sum of any contiguous subarray of length k.

    :param readings: list of integers (may be positive, zero, or negative)
    :param k: length of the sliding window (int)
    :return: maximum sum over all windows of size k (int)
    :raises ValueError: if k <= 0, k > len(readings), or readings is empty
    """
    # TODO (8 Steps of Coding):
    # 1. Re-read the problem and examples.
    # 2. Re-phrase the task in your own words (in comments or on paper).
    # 3. Identify inputs, outputs, and any helper variables you will need.
    # 4. Break down the logic for initializing the first window and sliding it.
    # 5. Write pseudocode to guide your implementation.
    # 6. Translate your pseudocode into Python here.
    # 7. Test and debug with small examples, including negatives and edge cases.
    # 8. Check that your solution is O(N) time and O(1) extra space.
    raise NotImplementedError("Implement max_window_sum in main.py")


if __name__ == "__main__":
    # Optional manual testing
    sample_readings = [3, 1, 2, 7, 4, 2]
    sample_k = 3
    print(max_window_sum(sample_readings, sample_k))
