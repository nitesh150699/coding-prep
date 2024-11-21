def longest_substring_k_distinct(s, k):
    if k == 0 or not s:
        return ""

    left = 0  
    char_count = {}  
    max_length = 0  
    max_substring = ""  
    for right in range(len(s)):
        char_count[s[right]] = char_count.get(s[right], 0) + 1  

        while len(char_count) > k:
            char_count[s[left]] -= 1  
            if char_count[s[left]] == 0:
                del char_count[s[left]]  
            left += 1 

        if right - left + 1 > max_length:
            max_length = right - left + 1
            max_substring = s[left:right + 1]

    return max_substring

