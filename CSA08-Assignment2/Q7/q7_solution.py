"""
Q7 - Day-4 Design Challenge: Diagnose, Redesign and Validate
Target System: Q6 Temple Step Climbing Counter (Recursive vs. Iterative Space-Optimized DP)
"""
import sys
import time
import tracemalloc
from functools import lru_cache

# ORIGINAL DESIGN: Top-Down Memoised Recursion
@lru_cache(maxsize=None)
def original_ways_memo(n: int) -> int:
    if n <= 1:
        return 1
    return original_ways_memo(n - 1) + original_ways_memo(n - 2)

# REDESIGNED SOLUTION: Bottom-Up Rolling-Variable Iteration (O(n) Time, O(1) Auxiliary Space)
def redesigned_ways_iter(n: int) -> int:
    if n <= 1:
        return 1
    prev2, prev1 = 1, 1
    for _ in range(2, n + 1):
        prev2, prev1 = prev1, prev1 + prev2
    return prev1

def benchmark_comparison(test_sizes: list[int]):
    print(f"{'n':<8} | {'Orig Status':<16} | {'Orig Time (s)':<14} | {'Orig Peak Mem':<14} | {'Redesign Time (s)':<17} | {'Redesign Peak Mem'}")
    print("-" * 98)
    for n in test_sizes:
        # Measure Original
        original_ways_memo.cache_clear()
        tracemalloc.start()
        t0 = time.perf_counter()
        try:
            res_orig = original_ways_memo(n)
            orig_time = f"{time.perf_counter() - t0:.6f}"
            _, orig_peak = tracemalloc.get_traced_memory()
            orig_status = "OK"
            orig_mem_str = f"{orig_peak:,} B"
        except RecursionError:
            res_orig = None
            orig_time = "N/A (Crash)"
            _, orig_peak = tracemalloc.get_traced_memory()
            orig_status = "RecursionError"
            orig_mem_str = f"{orig_peak:,} B"
        tracemalloc.stop()

        # Measure Redesign
        tracemalloc.start()
        t0 = time.perf_counter()
        res_new = redesigned_ways_iter(n)
        new_time = f"{time.perf_counter() - t0:.6f}"
        _, new_peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        if res_orig is not None:
            assert res_orig == res_new

        print(f"{n:<8} | {orig_status:<16} | {orig_time:<14} | {orig_mem_str:<14} | {new_time:<17} | {new_peak:,} B")

if __name__ == "__main__":
    print(f"Python Recursion Limit: {sys.getrecursionlimit()}")
    benchmark_comparison([100, 500, 950, 1000, 5000])
