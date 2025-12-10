def max_window_sum(readings, k):
    if not readings:
        raise ValueError("readings list is empty")
    if k <= 0:
        raise ValueError("k must be positive")
    if k > len(readings):
        raise ValueError("k cannot exceed number of readings")

    # initial window
    window_sum = sum(readings[:k])
    max_sum = window_sum

    # slide the window
    for i in range(k, len(readings)):
        window_sum += readings[i]          # add new element
        window_sum -= readings[i - k]      # remove old element
        if window_sum > max_sum:
            max_sum = window_sum

    return max_sum
