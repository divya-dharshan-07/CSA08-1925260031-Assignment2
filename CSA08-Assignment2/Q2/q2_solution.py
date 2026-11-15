"""
Q2 - Loops that Count Attempts
OTP Verification at a Bank Kiosk
"""

def verify_otp_while(correct_otp: str, entries: list[str]) -> str:
    """OTP loop using while. Blank entries do not count; loop-else locks account."""
    attempts = 0
    max_attempts = 3
    idx = 0

    while attempts < max_attempts:
        if idx >= len(entries):
            pass  # Placeholder when waiting for live input stream
            break
        entry = entries[idx].strip()
        idx += 1

        if entry == "":
            # Blank entry: ignore and do NOT increment attempts
            continue

        attempts += 1
        if entry == correct_otp:
            print(f"[while] Attempt {attempts}: OTP Verified! Access Granted.")
            break
        else:
            print(f"[while] Attempt {attempts}: Incorrect OTP.")
    else:
        print("[while] Account locked for 30 minutes due to 3 failed attempts.")
        return "LOCKED"
    return "VERIFIED"

def verify_otp_for(correct_otp: str, entries: list[str]) -> str:
    """OTP loop using for with range(3). Note: blank inputs consume an iteration in range(3)."""
    idx = 0
    for attempt in range(1, 4):
        if idx >= len(entries):
            pass
            break
        entry = entries[idx].strip()
        idx += 1

        if entry == "":
            print(f"[for] Iteration {attempt}: Blank entry skipped (warning: range(3) still advances!).")
            continue

        if entry == correct_otp:
            print(f"[for] Attempt {attempt}: OTP Verified! Access Granted.")
            break
        else:
            print(f"[for] Attempt {attempt}: Incorrect OTP.")
    else:
        print("[for] Account locked for 30 minutes.")
        return "LOCKED"
    return "VERIFIED"

def verify_otp_with_security_bonus(correct_otp: str, entries: list[str], security_passed: bool) -> str:
    """Changed Condition: Allows 2 extra attempts if security question is answered correctly."""
    attempts = 0
    max_attempts = 3
    bonus_used = False
    idx = 0

    while attempts < max_attempts:
        if idx >= len(entries):
            break
        entry = entries[idx].strip()
        idx += 1

        if entry == "":
            continue

        attempts += 1
        if entry == correct_otp:
            return f"VERIFIED on attempt {attempts}"

        if attempts == max_attempts and not bonus_used and security_passed:
            print("[Bonus] Security question answered correctly! Granting 2 extra attempts.")
            max_attempts += 2
            bonus_used = True
    else:
        return "LOCKED (30 mins)"
    return "ABORTED"

def verify_otp_recursive(correct_otp: str, entries: list[str], attempts_left: int = 3, idx: int = 0) -> str:
    """Alternative Concept: Recursive OTP verification."""
    if attempts_left == 0:
        return "LOCKED"
    if idx >= len(entries):
        return "NO_INPUT"

    entry = entries[idx].strip()
    if entry == "":
        return verify_otp_recursive(correct_otp, entries, attempts_left, idx + 1)
    if entry == correct_otp:
        return "VERIFIED"
    return verify_otp_recursive(correct_otp, entries, attempts_left - 1, idx + 1)

if __name__ == "__main__":
    print("--- Case 1: Blank entries + 3 wrong attempts ---")
    verify_otp_while("482910", ["", "111111", "  ", "222222", "333333"])
    print()
    verify_otp_for("482910", ["", "111111", "222222", "333333"])

    print("\n--- Case 2: Changed Condition (2 extra attempts after security question) ---")
    print("Result:", verify_otp_with_security_bonus("482910", ["111", "222", "333", "444", "482910"], True))

    print("\n--- Case 3: Recursive OTP Check ---")
    print("Recursive Result:", verify_otp_recursive("482910", ["", "123456", "482910"]))
