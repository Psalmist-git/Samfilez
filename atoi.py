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
