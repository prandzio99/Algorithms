# an implementation of recursive substring search

# match_type:   "simple"    - True if text contains pattern
#               "exact"     - True if text begins with pattern

def contains(text, pattern, match_type="simple", text_idx=0, pattern_idx=0):
    if match_type == "exact":
        if text_idx == len(text) and pattern_idx != len(pattern):
            return False
        if pattern_idx == len(pattern):
            return True
        if text[text_idx] == pattern[pattern_idx]:
            return contains(text, pattern, match_type, text_idx+1, pattern_idx+1)
        return False
    else:
        if text_idx == len(text):
            return False
        if text[text_idx] == pattern[pattern_idx]:
            if contains(text, pattern, "exact", text_idx, pattern_idx):
                return True
            else:
                contains(text, pattern, match_type, text_idx+1, pattern_idx)
        return contains(text, pattern, match_type, text_idx+1, pattern_idx)


# test code
if __name__ == '__main__':
    test_string_1 = "AABBBCCCC"
    test_string_2 = "BBC"
    test_string_3 = "ABBBCCC"
    print(contains(test_string_1, test_string_2))
    print(contains(test_string_1, test_string_3, "exact"))
