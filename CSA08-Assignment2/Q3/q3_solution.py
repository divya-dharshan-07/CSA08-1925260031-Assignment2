"""
Q3 - Engineer a Vehicle Registration Number Validator
Toll Plaza Number-Plate Records
"""
import re

def normalise(text):
    """'tn 09 ab 1234' -> 'TN09AB1234' (spaces and hyphens removed, upper case)."""
    # TODO 1: Remove spaces and hyphens and convert to upper case using string methods
    return text.strip().replace(" ", "").replace("-", "").upper()

def is_valid(reg):
    """Valid form: 2 letters, 2 digits, 1 or 2 letters, 4 digits (e.g. TN09AB1234)."""
    # TODO 2: Check the length is 9 or 10, then check each part using slicing with
    # isalpha() and isdigit()
    if len(reg) not in (9, 10):
        return False
    state = reg[:2]
    district = reg[2:4]
    series = reg[4:-4]
    number = reg[-4:]
    return (
        state.isalpha()
        and district.isdigit()
        and (1 <= len(series) <= 2 and series.isalpha())
        and number.isdigit()
    )

def format_receipt(reg: str) -> str:
    """Formats a valid normalised registration number as 'TN 09 AB 1234'."""
    if not is_valid(reg):
        raise ValueError(f"Invalid vehicle registration: {reg}")
    return f"{reg[:2]} {reg[2:4]} {reg[4:-4]} {reg[-4:]}"

def is_valid_regex(reg: str) -> bool:
    """Alternative Concept: Validation via Regular Expression."""
    return bool(re.fullmatch(r"[A-Z]{2}[0-9]{2}[A-Z]{1,2}[0-9]{4}", reg))

if __name__ == "__main__":
    print("--- Complete the Code Verification ---")
    for raw in ["tn 09 ab 1234", "KA-01-M-0007", "TN9AB1234", "TN 22 1234 AB"]:
        reg = normalise(raw)
        valid = is_valid(reg)
        formatted = format_receipt(reg) if valid else "N/A"
        print(f"{raw:15} -> {reg:11} {'valid' if valid else 'INVALID':8} | Receipt: {formatted}")

    print("\n--- 6 Designed Test Cases ---")
    six_inputs = [
        "tn 09 ab 1234",     # Valid 10-char
        "KA-01-M-0007",      # Valid 9-char
        "  dl04caf9999  ",   # Valid 10-char with leading/trailing spaces
        "MH-12-Z-1001",      # Valid 9-char
        "TN9AB1234",         # Invalid: 1-digit district code
        "TN 22 1234 AB",     # Invalid: swapped series and number
    ]
    for raw in six_inputs:
        reg = normalise(raw)
        v_slice = is_valid(reg)
        v_regex = is_valid_regex(reg)
        assert v_slice == v_regex
        print(f"Input: {raw!r:<18} -> Normalised: {reg:<11} -> Valid: {v_slice}")
