#!/usr/bin/env python3
from functools import reduce

def atoi(s: str) -> int:
    return (
        0 if not s 
        else (lambda sign, start: (
            lambda body: (
                0 if any(not ('0' <= c <= '9') for c in body)
                else reduce(lambda res, c: res * 10 + (ord(c) - 48), body, 0) * sign
            )
        )(s[start:]) if len(s) > start else 0)(
            -1 if s[0] == '-' else 1, 
            1 if s[0] in ('-', '+') else 0
        )
    )

# Example to see it work when executed
if __name__ == "__main__":
    import sys
    # If an argument is passed, parse it; otherwise use a default
    input_str = sys.argv[1] if len(sys.argv) > 1 else "456"
    print(atoi(input_str))
