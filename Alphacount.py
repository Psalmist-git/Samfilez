def alpha_count(s: str) -> int:
    count = 0
    
    for r in s:
        if ('a' <= r <= 'z') or ('A' <= r <= 'Z'):
            count += 1
            
    return count
