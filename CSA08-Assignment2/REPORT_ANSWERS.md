# Python Programming Assignment 2 (CO2) – Complete Analytical Report

## Q1 – Decisions with Many Boundaries (6 Marks)
### 1. Pre-Execution Predictions (8 Households)
| Household | Units | Ration Card | Age > 80 | Overlapping `if` Prediction | `if-elif-else` Prediction |
| :--- | :---: | :---: | :---: | :--- | :--- |
| H1 | 85 | Yes | No | Full Subsidy, Partial Subsidy | Full Subsidy |
| H2 (Boundary) | 100 | Yes | No | Full Subsidy, Partial Subsidy | Full Subsidy |
| H3 (Boundary) | 101 | Yes | No | Partial Subsidy | Partial Subsidy |
| H4 (Boundary) | 101 | No | No | No Subsidy | No Subsidy |
| H5 (Boundary) | 200 | Yes | No | Partial Subsidy | Partial Subsidy |
| H6 (Boundary) | 200 | No | Yes | No Subsidy | No Subsidy |
| H7 (Boundary) | 201 | No | Yes | Senior Citizen Special Subsidy | Senior Citizen Special Subsidy |
| H8 (Boundary) | 201 | Yes | No | No Subsidy | No Subsidy |

### 2. Why Separate `if` Statements Give Multiple Results vs `if-elif-else`
- **Separate `if` statements** are evaluated independently from top to bottom. If a developer writes `if units <= 100:` followed by `if units <= 200 and has_ration_card:`, a household with 100 units and a ration card satisfies both conditions and receives **two subsidies**.
- **`if-elif-else`** forms a single mutually exclusive decision chain: as soon as the first `True` branch executes, Python skips all remaining `elif` and `else` blocks, guaranteeing **at most one** outcome.

### 3. Design Decision: Combined Boolean Conditions (`and`/`or`) vs Nested `if`
- **Choice:** Flat `if-elif-else` with **combined Boolean conditions** (`101 <= units <= 200 and has_ration_card`) is superior to deeply nested `if` blocks.
- **Defence:** Each consumption slab maps 1-to-1 to a single `elif` branch, avoiding deep indentation ("arrow anti-pattern") and eliminating the risk of forgetting an inner `else` clause when a secondary condition (like `has_ration_card`) is `False`.

### 4. Alternative Concept & Complexity Analysis
- **`match-case` (Python 3.10+):** Evaluates structural patterns with guard clauses (`case (u, True, _) if 101 <= u <= 200:`). Like `if-elif-else`, it checks branches sequentially in $O(k)$ time for $k$ slabs and $O(1)$ auxiliary space.
- **Lookup List of `(upper_limit, condition_fn, decision)`:** Iterates over $k$ tuples in $O(k)$ time per decision and requires $O(k)$ memory to store the slab table, making slab thresholds data-driven and configurable without changing code logic.

---

## Q2 – Loops that Count Attempts (4 Marks)
### 1. Loop Design (`while` vs `for` with `range(3)`)
- **`while` loop:** Uses a separate `attempts` counter, so only nonblank OTP entries count toward the three allowed attempts. Blank entries are ignored with `pass` and `continue`.
- **`for` loop:** Uses `for attempt in range(1, 4)`. An inner `while` skips any blank entries before the next valid OTP is processed, so blank input does not consume one of the three attempts.
- **`break`:** Exits the verification loop immediately when the correct OTP is entered.
- **`continue`:** Skips blank entries without comparing them to the OTP or incrementing the valid-attempt counter.
- **`pass`:** Demonstrates a no-operation statement for an intentionally ignored blank entry in the `while` implementation.
- **Loop `else`:** Runs only when all three valid OTP attempts are incorrect and the loop finishes normally; it reports that the account is locked. A successful `break` skips the `else` block.
- **Input exhaustion:** Both loop versions return `NO_INPUT` if the provided entries end before verification or three failed attempts. They never report success merely because the input list ended.

### 2. Why `while` Is More Natural & Counter Placement
- **Why `while`:** A `while attempts < 3` loop directly represents a limit on valid attempts. The `for range(3)` version can also meet the blank-entry requirement, but it needs an inner loop to skip blanks before processing each counted attempt.
- **Counter placement:** The valid-attempt counter must be incremented only after checking that the entry is nonblank. Incrementing before the blank check would incorrectly charge the user for an empty submission.

### 3. Changed Condition (2 Extra Attempts via Security Question)
- The bonus implementation starts with three valid attempts. After the third incorrect OTP, a successful security-question check increases `max_attempts` by two exactly once. With the supplied test entries, the correct OTP is accepted on attempt 5.
- If the input entries run out before verification, the bonus implementation returns `NO_INPUT`; it does not treat missing input as success.

### 4. Alternative Concept & Complexity Analysis
- **Recursion:** The recursive alternative passes `attempts_left` and the current entry index (`idx`) to each call. Blank entries advance the index without reducing the remaining attempt count.
- **Time Complexity:** $O(a + b)$, where $a$ is the number of valid OTP attempts (at most 3, or 5 with the bonus) and $b$ is the number of blank entries skipped.
- **Space Complexity:** Iterative loops use $O(1)$ auxiliary space; the recursive version uses $O(a+b)$ call-stack space in the worst case because each recursive call advances through an entry.
- **Verified output:** Three incorrect OTPs produce `LOCKED`; a correct OTP after a blank produces `VERIFIED`; exhausted input produces `NO_INPUT`; the security-bonus test verifies on attempt 5; and the recursive test returns `VERIFIED`.

---

## Q3 – Vehicle Registration Number Validator (6 Marks)
### 1. Pre-Execution Predictions (6 Inputs)
1. `"tn 09 ab 1234"` $\rightarrow$ `"TN09AB1234"` $\rightarrow$ **Valid**
2. `"KA-01-M-0007"` $\rightarrow$ `"KA01M0007"` $\rightarrow$ **Valid**
3. `"  dl04caf9999  "` $\rightarrow$ `"DL04CAF9999"` $\rightarrow$ **Invalid** (11 chars; 3-letter series)
4. `"MH-12-Z-1001"` $\rightarrow$ `"MH12Z1001"` $\rightarrow$ **Valid**
5. `"TN9AB1234"` $\rightarrow$ `"TN9AB1234"` $\rightarrow$ **Invalid** (1-digit district code)
6. `"TN 22 1234 AB"` $\rightarrow$ `"TN221234AB"` $\rightarrow$ **Invalid** (digits in series position)

### 2. String Immutability & Slicing Inquiry
- **Immutability:** Python `str` objects cannot be modified in place after creation (enabling safe dictionary hashing, string interning, and memory safety). Therefore, `text.upper()` returns a *new* uppercase string rather than mutating `text`.
- **Slicing `s[-4:]` and `s[4:-4]`:**
  - For 9-char `"KA01M0007"`: `s[-4:]` returns `"0007"` (last 4 digits); `s[4:-4]` returns `"M"` (1-letter series).
  - For 10-char `"TN09AB1234"`: `s[-4:]` returns `"1234"` (last 4 digits); `s[4:-4]` returns `"AB"` (2-letter series).

### 3. Alternative Concept & Complexity Analysis
- **Regex (`re.fullmatch(r"[A-Z]{2}[0-9]{2}[A-Z]{1,2}[0-9]{4}", reg)`):**
  - **Time Complexity:** $O(L)$ where $L$ is string length for both slicing and regex matching.
  - **Readability & Maintainability:** Regex expresses the entire grammar in one compact pattern, whereas explicit slicing requires no `re` import and makes debugging individual segments straightforward for beginners.

---

## Q4 – Building Long Text: `+` or `join()`? (6 Marks)
### 1. Prediction & Measurement
- **Prediction:** `"".join()` is significantly faster than repeated `+=` because `join()` pre-calculates total output length in a single pass and allocates one buffer, whereas repeated `+=` risks allocating and copying growing strings on each iteration.
- **Measured Results (see `Q4/output.txt`):** Across 1,000, 10,000, and 200,000 lines, `"".join()` consistently outperforms `+=` and scales linearly.

### 2. String Immutability & CPython `+=` Optimization
- Because strings are immutable, `text += p + ";"` conceptually creates a new string object of length $k$ on step $k$, causing $1 + 2 + \dots + n = O(n^2)$ character copies.
- While CPython includes an in-place resize optimization when a string has a reference count of 1, this optimization is fragile (breaks if another variable references the string or on non-CPython interpreters like PyPy). `"".join()` guarantees $O(n)$ performance everywhere.

### 3. Alternative Concept & Complexity Analysis
- **`io.StringIO` / Direct File Streaming:** Writing line-by-line to `io.StringIO` runs in amortized $O(n)$ time with $O(n)$ buffer memory. Writing directly to disk (`file.write()`) achieves $O(n)$ time with $O(1)$ peak RAM, making direct file streaming ideal when statements exceed available memory.

---

## Q5 – Functions, Parameters and Scope (7 Marks)
### 1. Default Parameter Bug & `__defaults__`
- Default parameter expressions are evaluated **once at function definition time (`def`)**, not on each call. Thus `order=[]` binds a single shared `list` object inside `add_item_buggy.__defaults__`.
- After calling `add_item_buggy("Tea")` and `add_item_buggy("Vada")`, printing `add_item_buggy.__defaults__` outputs `(['Tea', 'Vada'],)`, proving the default tuple holds the mutated list.
- **Fix:** Use `order=None` and initialize `if order is None: order = []` inside the function body.

### 2. Parameters, Multiple Returns & LEGB Scope
- **Parameters:** Use **positional** arguments for mandatory core inputs (`item`), **default** parameters for standard configurations (`gst_rate=0.05`), and **keyword** arguments for clarity when overriding optional values (`discount=5.0`).
- **Multiple Returns:** Returning `return subtotal, gst, grand_total` packs values into a `tuple`, unpacked by the caller (`sub, gst, total = calculate_bill(...)`).
- **Scope (`local`, `nonlocal`, `global`):** `global` allows rebinding a module-level variable inside a function; `nonlocal` allows an inner function to rebind a variable in an enclosing function's scope. Mutating globals is generally avoided because it creates hidden coupling and makes functions non-reentrant and hard to test.

### 3. Alternative Concept & Complexity Analysis
- **Explicit Caller List vs. Closure:** Both run in $O(1)$ amortized time per `append()` and $O(m)$ space for $m$ items in an order. Passing an explicit list keeps functions stateless and transparent, whereas a closure encapsulates the list privately without exposing it to external mutation.

---

## Q6 – Recursion and Its Limits (8 Marks)
### 1. Recurrence & Hand Verification
- **Base Case:** `ways(0) = 1`, `ways(1) = 1` (1 way to stay at ground or take a single 1-step).
- **Recursive Case:** `ways(n) = ways(n - 1) + ways(n - 2)` for $n \ge 2$.
- **Hand Check ($n=1\dots6$):** $n=1 \rightarrow 1$, $n=2 \rightarrow 2$, $n=3 \rightarrow 3$, $n=4 \rightarrow 5$, $n=5 \rightarrow 8$, $n=6 \rightarrow 13$.

### 2. Call Tree for $n=5$ & Call Count Growth
```text
                  ways(5)
                 /       \
            ways(4)       ways(3)
           /      \       /      \
      ways(3)   ways(2) ways(2) ways(1)
      /     \
  ways(2) ways(1)
```
- Notice `ways(3)` is computed twice and `ways(2)` three times.
- At $n=25$, `ways_naive(25)` takes **242,785 calls** ($2 \times F_{26} - 1$), whereas `@lru_cache` memoisation takes only **26 calls** ($n + 1$).

### 3. Deployment Decision for $n = 1,000$
- Calling `ways_memo(1000)` on a cold cache triggers `RecursionError: maximum recursion depth exceeded` because Python's default `sys.getrecursionlimit()` is `1000` (and active interpreter frames already occupy ~3–5 frames).
- **Decision:** Rewrite with a bottom-up iterative loop (`ways_iterative`) rather than raising `sys.setrecursionlimit()`. Raising the recursion limit risks a C-level stack overflow crash for large $n$ and wastes $O(n)$ stack and cache memory, whereas an iterative loop runs in $O(n)$ time and $O(1)$ space safely for any $n$.

---

## Q7 – Day-4 Design Challenge: Diagnose, Redesign and Validate (13 Marks)
### A. Diagnose the Bottleneck
- In Q6 (`ways_memo`), although memoisation reduced time complexity from $O(\phi^n)$ to $O(n)$, top-down recursion still creates $n$ nested stack frames and stores $n$ dictionary entries in `@lru_cache`. At $n = 1,000$, stack depth exceeds `sys.getrecursionlimit()` (1000), causing a fatal `RecursionError`.
### B. Define the Design Objective
- Eliminate call-stack depth completely (`0` recursive frames) and reduce auxiliary memory from $O(n)$ to **$O(1)$ constant space** while maintaining $O(n)$ time complexity so inputs up to $n \ge 5,000$ execute without crashing.
### C. Design the Revised Solution
- **Exploited Property:** Optimal substructure with bounded dependency—computing `ways(i)` depends *only* on `ways(i - 1)` and `ways(i - 2)`, not the entire history $0 \dots i-3$.
- **Trade-off:** Individual intermediate values `ways(k)` are no longer cached for repeated random queries, trading multi-query cache hits for $O(1)$ space and crash-free execution.
- **Pseudocode:**
  ```text
  FUNCTION redesigned_ways_iter(n):
      IF n <= 1: RETURN 1
      prev2 <- 1, prev1 <- 1
      FOR i FROM 2 TO n:
          curr <- prev1 + prev2
          prev2 <- prev1
          prev1 <- curr
      RETURN prev1
  ```
### D. Predict Before Implementing
- `redesigned_ways_iter` will succeed at $n = 1,000$ and $n = 5,000$ where `original_ways_memo` raises `RecursionError`. The measured peak allocation for the iterative version at $n = 950$ is expected to be over 95% lower than the peak allocation recorded during the original version's failed run.
### E. Implement and Validate
- Executed in `Q7/q7_solution.py` (results recorded in `Q7/output.txt`). At $n = 950$, the original memoised implementation raises `RecursionError`; `tracemalloc` records a peak of 166,169 B during that failed run. The iterative redesign completes successfully with a peak of 424 B (about 99.7% lower measured peak allocation). The iterative version also completes at $n = 5,000$ with a measured peak of 1,552 B. Because the original measurement is from a failed run, this is a comparison of recorded peak allocations, not two successful executions.
### F. Defend the Final Design
- The objective was achieved for the tested sizes: the iterative design avoids recursive call-stack growth, uses $O(1)$ auxiliary space, and completes at $n = 5,000$. Its measured runtime and memory are reported in `Q7/output.txt`. The original memoised design is only preferable if the application must answer thousands of repeated queries for different values of $n$ within the valid recursion limit.
