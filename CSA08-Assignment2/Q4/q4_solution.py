"""
Q4 - Building Long Text: + or join()?
Monthly SMS Bill Statement
"""
import io
import time

items = [f"Item{i}:Rs{i % 50}" for i in range(200_000)]

def build_plus(parts):
    text = ""
    for p in parts:
        text += p + ";"
    return text

def build_join(parts):
    # TODO 1: Build the same text using a single str.join() call
    return ";".join(parts) + (";" if parts else "")

def build_fstring_join(parts):
    """Variant (c): formatting each line with an f-string inside a list comprehension + join."""
    return "".join([f"{p};" for p in parts])

def build_stringio(parts):
    """Alternative Concept: Using io.StringIO buffer."""
    buf = io.StringIO()
    for p in parts:
        buf.write(p)
        buf.write(";")
    return buf.getvalue()

if __name__ == "__main__":
    print("--- Complete the Code Benchmark (200,000 items, 3 runs) ---")
    plus_times = []
    join_times = []
    for run in range(1, 4):
        start = time.perf_counter(); a = build_plus(items); t_plus = time.perf_counter() - start
        start = time.perf_counter(); b = build_join(items); t_join = time.perf_counter() - start
        assert a == b
        plus_times.append(t_plus)
        join_times.append(t_join)
        print(f"Run {run}: same text: {a == b} | length: {len(b)} | += time: {t_plus:.4f} s | join time: {t_join:.4f} s")

    print(f"Average += time  : {sum(plus_times)/len(plus_times):.4f} s")
    print(f"Average join time: {sum(join_times)/len(join_times):.4f} s")

    print("\n--- Scaling Comparison across 1,000 | 10,000 | 200,000 lines ---")
    for n in [1_000, 10_000, 200_000]:
        subset = items[:n]
        t0 = time.perf_counter(); r1 = build_plus(subset); dt_plus = time.perf_counter() - t0
        t0 = time.perf_counter(); r2 = build_join(subset); dt_join = time.perf_counter() - t0
        t0 = time.perf_counter(); r3 = build_fstring_join(subset); dt_fstr = time.perf_counter() - t0
        t0 = time.perf_counter(); r4 = build_stringio(subset); dt_sio = time.perf_counter() - t0
        assert r1 == r2 == r3 == r4
        print(f"N={n:<7} | +=: {dt_plus:.5f}s | join: {dt_join:.5f}s | f-str+join: {dt_fstr:.5f}s | StringIO: {dt_sio:.5f}s")
