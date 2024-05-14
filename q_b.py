
# Function that compares two version string. Returns 0 if equal, 1 if version1 is greater, -1 if version2 is greater

def compare(version1, version2):
    if version1 is None or version2 is None:
        raise ValueError("Versions cannot be None")
    
    if not version1 and not version2:
        return 0
    if not version1:
        return -1
    if not version2:
        return 1
    
    v1_components = version1.split('.')
    v2_components = version2.split('.')
    
    length = max(len(v1_components), len(v2_components))
    
    for i in range(length):
        v1_part = int(v1_components[i]) if i < len(v1_components) else 0
        v2_part = int(v2_components[i]) if i < len(v2_components) else 0
        if v1_part < v2_part:
            return -1
        elif v1_part > v2_part:
            return 1
    
    return 0

# Test cases
def run_tests():
    test_cases = [
        ("1.0", "1.0", 0),
        ("1.2", "1.1", 1),
        ("1.1", "1.2", -1),
        ("1.0.1", "1.0", 1),
        ("1.0", "1.0.1", -1),
        ("1.0.0", "1.0", 0),
        ("1.0", "1.0.0", 0),
        ("1.01", "1.1", 0),
        ("1.0", "1.00", 0),
        ("1.10", "1.2", 1),
        ("2.0", "10.0", -1),
        ("10.0", "2.0", 1),
        ("10.0.1", "10.0.0", 1),
        ("", "", 0),
        ("1.0", "", 1),
        ("", "1.0", -1),
        (None, "1.0", ValueError),
        ("1.0", None, ValueError)
    ]
    
    for version1, version2, expected in test_cases:
        try:
            result = compare(version1, version2)
            assert result == expected, f"Test failed: compare('{version1}', '{version2}') == {result}, expected {expected}"
        except ValueError as e:
            assert expected == ValueError, f"Test failed: compare('{version1}', '{version2}') raised ValueError, expected {expected}"
        except Exception as e:
            assert False, f"Test failed: compare('{version1}', '{version2}') raised an unexpected exception: {e}"

    print("All tests passed.")

run_tests()