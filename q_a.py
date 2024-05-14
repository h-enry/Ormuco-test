# A function that compares two lines with the coordinates (x1, x2) and (x3, x4) and see if they overlap.
def do_lines_overlap(x1, x2, x3, x4):
    # Sort the segments from left to right if not in order then compare
    if x1 > x2:
        x1, x2 = x2, x1
    if x3 > x4:
        x3, x4 = x4, x3
    
    return x1 <= x4 and x3 <= x2

# Test cases
test_cases = [
    ((1, 5), (2, 6), True),
    ((1, 5), (6, 8), False),
    ((1, 5), (5, 8), True),
    ((5, 1), (2, 6), True),
    ((1, 1), (1, 1), True),
    ((1, 3), (2, 2), True),
    ((2, 2), (1, 3), True),
    ((-5, -1), (-4, 0), True),
    ((-5, -1), (0, 4), False),
    ((0, 0), (0, 0), True), 
]

# Running tests
for i, (line1, line2, expected) in enumerate(test_cases):
    result = do_lines_overlap(*line1, *line2)
    print(f"{line1} and {line2} -> Expected: {expected}, Got: {result}, {'PASS' if result == expected else 'FAIL'}")