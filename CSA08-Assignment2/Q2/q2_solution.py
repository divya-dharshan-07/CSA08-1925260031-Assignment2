"""
Q2 - Loops that Count Attempts
OTP Verification at a Bank Kiosk

Concepts demonstrated:
while, for, range(), break, continue, pass,
loop else, dynamic attempts and recursion.
"""


# 1. OTP verification using while loop
def verify_otp_while(correct_otp: str, entries: list[str]) -> str:
    attempts = 0
    max_attempts = 3
    idx = 0

    while attempts < max_attempts:
        if idx >= len(entries):
            print("[while] No more OTP entries available.")
            return "NO_INPUT"

        entry = entries[idx].strip()
        idx += 1

        if entry == "":
            pass
            continue

        attempts += 1

        if entry == correct_otp:
            print(f"[while] Attempt {attempts}: OTP Verified!")
            break

        print(f"[while] Attempt {attempts}: Incorrect OTP.")

    else:
        print("[while] Account locked for 30 minutes.")
        return "LOCKED"

    return "VERIFIED"


# 2. OTP verification using for loop and range(3)
def verify_otp_for(correct_otp: str, entries: list[str]) -> str:
    idx = 0

    for attempt in range(1, 4):

        # Skip blank entries without counting an attempt
        while idx < len(entries) and entries[idx].strip() == "":
            idx += 1

        if idx >= len(entries):
            print("[for] No more OTP entries available.")
            return "NO_INPUT"

        entry = entries[idx].strip()
        idx += 1

        if entry == correct_otp:
            print(f"[for] Attempt {attempt}: OTP Verified!")
            break

        print(f"[for] Attempt {attempt}: Incorrect OTP.")

    else:
        print("[for] Account locked for 30 minutes.")
        return "LOCKED"

    return "VERIFIED"


# 3. Dynamic bonus attempts after security verification
def verify_otp_with_security_bonus(
    correct_otp: str,
    entries: list[str],
    security_passed: bool
) -> str:

    attempts = 0
    max_attempts = 3
    idx = 0
    bonus_used = False

    while attempts < max_attempts:

        if idx >= len(entries):
            return "NO_INPUT"

        entry = entries[idx].strip()
        idx += 1

        if entry == "":
            continue

        attempts += 1

        if entry == correct_otp:
            return f"VERIFIED on attempt {attempts}"

        print(f"[Bonus] Incorrect OTP on attempt {attempts}.")

        if attempts == 3 and security_passed and not bonus_used:
            print("[Bonus] Security question passed!")
            print("[Bonus] 2 extra attempts granted.")
            max_attempts += 2
            bonus_used = True

    return "LOCKED (30 mins)"


# 4. Recursive OTP verification
def verify_otp_recursive(
    correct_otp: str,
    entries: list[str],
    attempts_left: int = 3,
    idx: int = 0
) -> str:

    if attempts_left == 0:
        return "LOCKED"

    if idx >= len(entries):
        return "NO_INPUT"

    entry = entries[idx].strip()

    if entry == "":
        return verify_otp_recursive(
            correct_otp, entries, attempts_left, idx + 1
        )

    if entry == correct_otp:
        return "VERIFIED"

    return verify_otp_recursive(
        correct_otp, entries, attempts_left - 1, idx + 1
    )


# 5. Main testing section
if __name__ == "__main__":

    print("--- Case 1: Blank entries + 3 wrong attempts ---")

    print("While Result:",
          verify_otp_while(
              "482910",
              ["", "111111", "  ", "222222", "333333"]
          ))

    print()

    print("For Result:",
          verify_otp_for(
              "482910",
              ["", "111111", "222222", "333333"]
          ))

    print("\n--- Case 2: Correct OTP ---")

    print("While Result:",
          verify_otp_while("482910", ["", "482910"]))

    print("For Result:",
          verify_otp_for("482910", ["", "482910"]))

    print("\n--- Case 3: Input exhausted ---")

    print("While Result:",
          verify_otp_while("482910", ["111111"]))

    print("For Result:",
          verify_otp_for("482910", ["111111"]))

    print("\n--- Case 4: Security Bonus ---")

    print("Bonus Result:",
          verify_otp_with_security_bonus(
              "482910",
              ["111", "222", "333", "444", "482910"],
              True
          ))

    print("\n--- Case 5: Recursive OTP Check ---")

    print("Recursive Result:",
          verify_otp_recursive(
              "482910",
              ["", "123456", "482910"]
          ))
