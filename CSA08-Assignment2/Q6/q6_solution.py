"""
Q6 - Recursion and Its Limits
Counting Ways to Climb Temple Steps
"""
import sys
import time
from functools import lru_cache

calls = 0

def ways_naive(n):
    """Ways to climb n temple steps taking 1 or 2 steps at a time."""
    global calls
    calls += 1
    if n <= 1:
        return 1
    return ways_naive(n - 1) + ways_naive(n - 2)

@lru_cache(maxsize=None)
def ways_memo(n):
    global calls
    calls += 1
    # TODO 1: Write the same base case and recursive case as ways_naive, calling
    # ways_memo
    if n <= 1:
        return 1
    return ways_memo(n - 1) + ways_memo(n - 2)

def ways_iterative(n: int) -> int:
    """Alternative Concept: O(n) time, O(1) space iterative DP loop."""
    if n <= 1:
        return 1
    prev2, prev1 = 1, 1
    for _ in range(2, n + 1):
        prev2, prev1 = prev1, prev1 + prev2
    return prev1

if __name__ == "__main__":
    print("--- Hand Verification (n = 1 to 6) ---")
    for step in range(1, 7):
        ways_memo.cache_clear()
        print(f"n={step}: ways={ways_memo(step)}")

    print("\n--- Complete the Code Output (n = 25) ---")
    calls = 0; print("naive:", ways_naive(25), "calls =", calls)
    ways_memo.cache_clear()
    calls = 0; print("memo :", ways_memo(25), "calls =", calls)

    print("\n--- Growth Investigation (n = 10, 20, 25, 30) ---")
    for n in [10, 20, 25, 30]:
        calls = 0
        t0 = time.perf_counter()
        ans_naive = ways_naive(n)
        t_naive = time.perf_counter() - t0
        c_naive = calls

        ways_memo.cache_clear()
        calls = 0
        t0 = time.perf_counter()
        ans_memo = ways_memo(n)
        t_memo = time.perf_counter() - t0
        c_memo = calls

        assert ans_naive == ans_memo == ways_iterative(n)
        print(f"n={n:<2} | Naive Calls: {c_naive:<8} ({t_naive:.5f}s) | Memo Calls: {c_memo:<4} ({t_memo:.6f}s)")

    print("\n--- Deployment Decision: Testing n = 1,000 ---")
    print("Current sys.getrecursionlimit():", sys.getrecursionlimit())
    ways_memo.cache_clear()
    try:
        res_1000 = ways_memo(1000)
        print("ways_memo(1000) succeeded (digits):", len(str(res_1000)))
    except RecursionError as err:
        print(f"ways_memo(1000) raised RecursionError: {err}")

    t0 = time.perf_counter()
    iter_1000 = ways_iterative(1000)
    t_iter = time.perf_counter() - t0
    print(f"ways_iterative(1000) succeeded in {t_iter:.6f}s | Number of digits: {len(str(iter_1000))}")
