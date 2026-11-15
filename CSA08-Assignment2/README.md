# CSA08 - Python Programming: Assignment 2 (CO2)

- **Student Name:** <Your Name>
- **Register Number:** <Your Register Number>
- **Course:** CSA08 – Python Programming
- **Python Version:** Python 3.10.16
- **External Libraries:** None (100% Python Standard Library: `time`, `sys`, `io`, `re`, `functools`, `tracemalloc`)

## Repository Structure
- `Q1/` – Decisions with Many Boundaries (`q1_solution.py`, `output.txt`)
- `Q2/` – Loops that Count Attempts (`q2_solution.py`, `output.txt`)
- `Q3/` – Vehicle Registration Number Validator (`q3_solution.py`, `sample_plates.txt`, `output.txt`)
- `Q4/` – Building Long Text: `+=` vs `join()` (`q4_solution.py`, `sample_items.txt`, `output.txt`)
- `Q5/` – Functions, Parameters and Scope (`q5_solution.py`, `output.txt`)
- `Q6/` – Recursion and Its Limits (`q6_solution.py`, `output.txt`)
- `Q7/` – Day-4 Design Challenge: Diagnose, Redesign and Validate (`q7_solution.py`, `output.txt`)
- `REPORT_ANSWERS.md` – Complete theoretical answers, predictions, complexity comparisons, and Day-4 design evaluation.

## Commands to Run Each Program
```bash
python Q1/q1_solution.py
python Q2/q2_solution.py
python Q3/q3_solution.py
python Q4/q4_solution.py
python Q5/q5_solution.py
python Q6/q6_solution.py
python Q7/q7_solution.py
```

## Summary of Results
- **Q1:** Demonstrated that separate `if` statements without mutually exclusive bounds cause households at `<= 100` units with a ration card to receive two subsidies, whereas `if-elif-else` guarantees a single mutually exclusive outcome.
- **Q2:** Implemented OTP verification using both `while` and `for` with `break`, `continue`, `pass`, and `loop-else`. Showed why `while` handles blank entries without wasting attempts and adapts cleanly to dynamic attempt extensions.
- **Q3:** Built normaliser, slicer-based validator, and receipt formatter without regex; verified all 6 test inputs and compared $O(L)$ slicing against `re.fullmatch`.
- **Q4:** Benchmarked `+=`, `"".join()`, f-string comprehension, and `io.StringIO` across 1,000, 10,000, and 200,000 lines, verifying $O(n)$ performance of `join()`.
- **Q5:** Resolved mutable default argument bug (`order=[]` $\rightarrow$ `order=None`), inspected `__defaults__`, demonstrated LEGB scope (`local`, `nonlocal`, `global`), and validated 3 independent canteen orders.
- **Q6:** Verified step-climbing combinations for $n=1\dots6$, compared naive $O(\phi^n)$ recursion (242,785 calls at $n=25$) against memoised $O(n)$ recursion (26 calls at $n=25$), and diagnosed `RecursionError` at $n=1000$.
- **Q7:** Redesigned Q6's recursive memoised solver into an $O(n)$ time, $O(1)$ space iterative rolling-variable solution, eliminating call-stack overflow and reducing peak memory overhead.
