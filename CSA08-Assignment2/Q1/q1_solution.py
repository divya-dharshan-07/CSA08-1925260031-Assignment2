"""
Q1 - Decisions with Many Boundaries
State Electricity Subsidy Eligibility
"""

def check_subsidy_separate_if(units: int, has_ration_card: bool, has_senior_80_plus: bool) -> list[str]:
    """Buggy implementation using separate if statements (can grant multiple subsidies)."""
    decisions = []
    if units <= 100:
        decisions.append("Full Subsidy")
    if 101 <= units <= 200 and has_ration_card:
        decisions.append("Partial Subsidy")
    if units > 200 and has_senior_80_plus:
        decisions.append("Senior Citizen Special Subsidy")
    # Also demonstrating how poorly written separate ifs without upper bounds overlap:
    return decisions if decisions else ["No Subsidy"]

def check_subsidy_overlapping_ifs(units: int, has_ration_card: bool, has_senior_80_plus: bool) -> list[str]:
    """Classic developer bug: separate if statements missing upper bounds."""
    decisions = []
    if units <= 100:
        decisions.append("Full Subsidy")
    if units <= 200 and has_ration_card:  # Bug: units <= 100 also triggers this!
        decisions.append("Partial Subsidy")
    if units > 200 and has_senior_80_plus:
        decisions.append("Senior Citizen Special Subsidy")
    if not decisions:
        decisions.append("No Subsidy")
    return decisions

def check_subsidy_elif(units: int, has_ration_card: bool, has_senior_80_plus: bool) -> str:
    """Correct implementation using mutually exclusive if-elif-else and chained comparisons."""
    if units <= 100:
        return "Full Subsidy"
    elif 101 <= units <= 200 and has_ration_card:
        return "Partial Subsidy"
    elif units > 200 and has_senior_80_plus:
        return "Senior Citizen Special Subsidy"
    else:
        return "No Subsidy"

def check_subsidy_match(units: int, has_ration_card: bool, has_senior_80_plus: bool) -> str:
    """Alternative Concept 1: Python 3.10+ structural pattern matching (match-case)."""
    match (units, has_ration_card, has_senior_80_plus):
        case (u, _, _) if u <= 100:
            return "Full Subsidy"
        case (u, True, _) if 101 <= u <= 200:
            return "Partial Subsidy"
        case (u, _, True) if u > 200:
            return "Senior Citizen Special Subsidy"
        case _:
            return "No Subsidy"

def check_subsidy_lookup(units: int, has_ration_card: bool, has_senior_80_plus: bool) -> str:
    """Alternative Concept 2: Lookup table of (upper_limit, condition_fn, decision)."""
    slabs = [
        (100, lambda rc, sr: True, "Full Subsidy"),
        (200, lambda rc, sr: rc, "Partial Subsidy"),
        (float("inf"), lambda rc, sr: sr, "Senior Citizen Special Subsidy"),
    ]
    for upper_limit, cond, decision in slabs:
        if units <= upper_limit:
            return decision if cond(has_ration_card, has_senior_80_plus) else "No Subsidy"
    return "No Subsidy"

if __name__ == "__main__":
    # 8 Households covering every boundary (100, 101, 200, 201)
    test_households = [
        ("H1 (<=100, RC=True)", 85, True, False),
        ("H2 (Boundary 100, RC=True)", 100, True, False),
        ("H3 (Boundary 101, RC=True)", 101, True, False),
        ("H4 (Boundary 101, RC=False)", 101, False, False),
        ("H5 (Boundary 200, RC=True)", 200, True, False),
        ("H6 (Boundary 200, RC=False, Sr=True)", 200, False, True),
        ("H7 (Boundary 201, Sr=True)", 201, False, True),
        ("H8 (Boundary 201, Sr=False)", 201, True, False),
    ]

    print(f"{'Household':<36} | {'Overlapping Ifs':<32} | {'if-elif-else':<30}")
    print("-" * 105)
    for name, units, rc, sr in test_households:
        res_bug = ", ".join(check_subsidy_overlapping_ifs(units, rc, sr))
        res_elif = check_subsidy_elif(units, rc, sr)
        assert res_elif == check_subsidy_match(units, rc, sr) == check_subsidy_lookup(units, rc, sr)
        print(f"{name:<36} | {res_bug:<32} | {res_elif:<30}")
